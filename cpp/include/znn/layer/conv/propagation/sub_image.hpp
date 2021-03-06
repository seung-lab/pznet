#pragma once

#include "znn/intrin.hpp"
#include "znn/types.hpp"
#include "znn/layer/activation_defs.hpp"
#include "znn/util/conditional_load.hpp"
#include <type_traits>
#include <math.h>

#ifdef ZNN_KNL
   #define _LOG_E_BASE_2 1.44269504089
   #define SIMD_EXP_M_INPL(a, m)asdf SIMD_E2A23_MASK(a, m, SIMD_MUL_MASK(a, m, a, SIMD_SET1(_LOG_E_BASE_2)))

   #define SIMD_SUBCONST_M_INPL(a, c, m) SIMD_SUB_MASK(a, m, a, SIMD_SET1(c))

   #define ELU(v) { SIMD_MASK ltz;\
                    ltz =  SIMD_LT(v, SIMD_SET1(0.0));\
                    v = SIMD_EXP_M_INPL(v, ltz);\
                    v = SIMD_SUBCONST_M_INPL(v, 1.0, ltz); }

#else
   #define ELU(base) {\
                        ZNN_PRAGMA(SIMD_WIDTH)\
                        for (long_t i = 0; i < SIMD_WIDTH; i++) {\
                           if (base[i] < 0.0f) {\
                              base[i] = std::exp(static_cast<float>(base[i])) - 1.0;\
                           }\
                        }\
                     }
   #define RELU(base) {\
                        ZNN_PRAGMA(SIMD_WIDTH)\
                        for (long_t i = 0; i < SIMD_WIDTH; i++) {\
                           if (base[i] < 0.0f) {\
                              base[i] = 0;\
                           }\
                        }\
                     }
#endif


namespace znn
{
namespace phi
{
namespace propagation
{

/*******************************************************************************
*
* Kernel shape is:
        Activation = false;
*      k[D][H][W][IN_FMAP][OUT_FMAP] with IN_FMAP=OUT_FMAP=SIMD_WIDTH
*
* input and output shapes are
*      i/o[D][H][W][FMAP] with FMAP=SIMD_WIDTH
*
* if FIRST
*      o[:][:][:][of] is initialized to b[of]
* for of in [0,SIMD_WIDTH), and then
* for all valid d, h, w, kd, kh, kw, if, of
*      o[d][h][w][of] += k[kd][kh][kw][if][of] * i[d+kd][h+kh][w+kw][if];
*
*******************************************************************************/

template <bool   Bias,                    // load or set to bias
          int   Activation,
          bool   AddOrOverwrite,
          long_t IFMs,                    // number of input images
          class ID, class IH, class IW,   // image traits
          class CD, class CH, class CW,   // convolution traits
          long_t RD, long_t RH, long_t RW // register blocking
          >
struct sub_image;

struct sub_image_dummy
{
    static void execute(float const* __restrict, float* __restrict,
                        float const* __restrict, float const* __restrict, 
                        float const* __restrict)
    {
    }
};

template <bool   Bias,                  // load or set to bias
          int   Activation,
          bool   AddOrOverwrite,
          long_t IFMs,                  // number of input images
          class ID, class IH, class IW, // image traits
          class CD, class CH, class CW, // convolution traits
          long_t RW                     // register blocking
          >
struct sub_image_1d
{
    static void execute(float const* __restrict i, float* __restrict o,
                        float const* __restrict k, float const* __restrict b,
                        float const* __restrict scale)// scale factor for values initially in o 
    {
        SIMD_FLOAT vout[RW], vwt; // Expected to be in the register file

        // load initial values to vout
        ZNN_PRAGMA(unroll(RW))
        for (long_t rw = 0; rw < RW; ++rw)
        {
            vout[rw] = load_or_set_initial_value<Bias, AddOrOverwrite>(o + rw * IW::out_stride, b, scale);
        }

        for (long_t kd = 0; kd < CD::size; ++kd)
        {
            for (long_t kh = 0; kh < CH::size; ++kh)
            {
                for (long_t s = 0; s < IFMs; ++s)
                {
                    for (long_t kw = 0; kw < CW::size; ++kw)
                    {
                        vwt = SIMD_LOAD(
                            k +
                            ((kd * CD::ker_stride + kh * CH::ker_stride +
                              kw * CW::ker_stride) *
                                 SIMD_WIDTH +
                             s) *
                                SIMD_WIDTH);

                        ZNN_PRAGMA(unroll(RW))
                        for (long_t rw = 0; rw < RW; ++rw)
                        {
                            vout[rw] = SIMD_FMADD(
                                vwt,
                                SIMD_SET1(
                                    i[kd * ID::in_stride + kh * IH::in_stride +
                                      (kw + rw * CW::conv_stride) *
                                          IW::in_stride +
                                      s]),
                                vout[rw]);
                        }
                    }
                }
            }
        }
        

        ZNN_PRAGMA(unroll(RW))
        for (long_t rw = 0; rw < RW; ++rw)
        {
#ifdef ZNN_KNL
            if (Activation) 
            {
                SIMD_ELU(vout[rw]); 
            }
#endif
            auto base = o + rw * IW::out_stride;
            SIMD_STORE(base, vout[rw]);
#ifndef ZNN_KNL
            if (Activation == ELU_ACT) 
            {
               ELU(base);
            }
            else if (Activation == RELU_ACT) 
            {
               RELU(base);
            }
#endif
        }
    }
};

template <bool   Bias,                  // load or set to bias
          int   Activation,
          bool   AddOrOverwrite,
          long_t IFMs,                  // number of input images
          class ID, class IH, class IW, // image traits
          class CD, class CH, class CW, // convolution traits
          long_t RH, long_t RW          // register blocking
          >
struct sub_image_2d
{
    static void execute(float const* __restrict i, float* __restrict o,
                        float const* __restrict k, float const* __restrict b,
                        float const* __restrict scale)// scale factor for values initially in o 
    {
        SIMD_FLOAT vout[RH][RW], vwt; // Expected to be in the register file

        ZNN_PRAGMA(unroll(RH))
        for (long_t rh = 0; rh < RH; ++rh)
        {
            ZNN_PRAGMA(unroll(RW))
            for (long_t rw = 0; rw < RW; ++rw)
            {
                vout[rh][rw] = load_or_set_initial_value<Bias, AddOrOverwrite>(
                                   o + rh * IH::out_stride + rw * IW::out_stride, b, scale);
            }
        }

        for (long_t kd = 0; kd < CD::size; ++kd)
        {
            for (long_t kh = 0; kh < CH::size; ++kh)
            {
                for (long_t s = 0; s < IFMs; ++s)
                {
                    for (long_t kw = 0; kw < CW::size; ++kw)
                    {
                        vwt = SIMD_LOAD(
                            k +
                            ((kd * CD::ker_stride + kh * CH::ker_stride +
                              kw * CW::ker_stride) *
                                 SIMD_WIDTH +
                             s) *
                                SIMD_WIDTH);

                        ZNN_PRAGMA(unroll(RH))
                        for (long_t rh = 0; rh < RH; ++rh)
                        {
                            ZNN_PRAGMA(unroll(RW))
                            for (long_t rw = 0; rw < RW; ++rw)
                            {
                                vout[rh][rw] = SIMD_FMADD(
                                    vwt,
                                    SIMD_SET1(i[kd * ID::in_stride +
                                                (kh + rh * CH::conv_stride) *
                                                    IH::in_stride +
                                                (kw + rw * CW::conv_stride) *
                                                    IW::in_stride +
                                                s]),
                                    vout[rh][rw]);
                            }
                        }
                    }
                }
            }
        }

        ZNN_PRAGMA(unroll(RH))
        for (long_t rh = 0; rh < RH; ++rh)
        {
            ZNN_PRAGMA(unroll(RW))
            for (long_t rw = 0; rw < RW; ++rw)
            {
#ifdef ZNN_KNL
                if (Activation) 
                {
                    SIMD_ELU(vout[rh][rw]); 
                }
#endif
                auto base = o + rh * IH::out_stride + rw * IW::out_stride;
                SIMD_STORE(base, vout[rh][rw]);
#ifndef ZNN_KNL
                if (Activation == ELU_ACT) 
                {
                   ELU(base);
                }
                else if (Activation == RELU_ACT) 
                {
                   RELU(base);
                }
#endif
            }
        }
    }
};

template <bool   Bias,                    // load or set to bias
          int   Activation,
          bool   AddOrOverwrite,
          long_t IFMs,                    // number of input images
          class ID, class IH, class IW,   // image traits
          class CD, class CH, class CW,   // convolution traits
          long_t RD, long_t RH, long_t RW // register blocking
          >
struct sub_image_3d
{
    static void execute(float const* __restrict i, float* __restrict o,
                        float const* __restrict k, float const* __restrict b,
                        float const* __restrict scale)// scale factor for values initially in o 
    {
        SIMD_FLOAT vout[RD][RH][RW], vwt; // Expected to be in the register file
         
        znn_pragma(unroll(rd))
        for (long_t rd = 0; rd < rd; ++rd)
        {
            znn_pragma(unroll(rh))
            for (long_t rh = 0; rh < rh; ++rh)
            {
                znn_pragma(unroll(rw))
                for (long_t rw = 0; rw < rw; ++rw)
                {
                    vout[rd][rh][rw] = load_or_set_initial_value<Bias, AddOrOverwrite>(
                        o + rd * id::out_stride + rh * ih::out_stride +
                            rw * iw::out_stride,
                        b, scale);
                }
            }
        }

        for (long_t kd = 0; kd < CD::size; ++kd)
        {
            for (long_t kh = 0; kh < CH::size; ++kh)
            {
                for (long_t s = 0; s < IFMs; ++s)
                {
                    for (long_t kw = 0; kw < CW::size; ++kw)
                    {
                        vwt = SIMD_LOAD(
                            k +
                            ((kd * CD::ker_stride + kh * CH::ker_stride +
                              kw * CW::ker_stride) *
                                 SIMD_WIDTH +
                             s) *
                                SIMD_WIDTH);

                        ZNN_PRAGMA(unroll(RD))
                        for (long_t rd = 0; rd < RD; ++rd)
                        {
                            ZNN_PRAGMA(unroll(RH))
                            for (long_t rh = 0; rh < RH; ++rh)
                            {
                                ZNN_PRAGMA(unroll(RW))
                                for (long_t rw = 0; rw < RW; ++rw)
                                {
                                    vout[rd][rh][rw] = SIMD_FMADD(
                                        vwt, SIMD_SET1(
                                                 i[(kd + rd * CD::conv_stride) *
                                                       ID::in_stride +
                                                   (kh + rh * CH::conv_stride) *
                                                       IH::in_stride +
                                                   (kw + rw * CW::conv_stride) *
                                                       IW::in_stride +
                                                   s]),
                                        vout[rd][rh][rw]);
                                }
                            }
                        }
                    }
                }
            }
        }

        ZNN_PRAGMA(unroll(RD))
        for (long_t rd = 0; rd < RD; ++rd)
        {
            ZNN_PRAGMA(unroll(RH))
            for (long_t rh = 0; rh < RH; ++rh)
            {
                ZNN_PRAGMA(unroll(RW))
                for (long_t rw = 0; rw < RW; ++rw)
                {
#ifdef ZNN_KNL
                    if (Activation) 
                    {
                        SIMD_ELU(vout[rd][rh][rw]); 
                    }
#endif
                    auto base = o + rd * ID::out_stride + rh * IH::out_stride + rw * IW::out_stride; 
                    SIMD_STORE(base, vout[rd][rh][rw]);
#ifndef ZNN_KNL
                    if (Activation == ELU_ACT) 
                    {
                       ELU(base);
                    }
                    else if (Activation == RELU_ACT) 
                    {
                       RELU(base);
                    }
#endif
                }
            }
        }
    }
};

template <bool   Bias,                    // load or set to bias
          int   Activation,
          bool   AddOrOverwrite,
          long_t IFMs,                    // number of input images
          class ID, class IH, class IW,   // image traits
          class CD, class CH, class CW,   // convolution traits
          long_t RD, long_t RH, long_t RW // register blocking
          >
struct sub_image
    : std::conditional_t<
          RD == 0 || RH == 0 || RW == 0, sub_image_dummy,
          std::conditional_t<
              RD == 1 && RH == 1,
              sub_image_1d<Bias, Activation, AddOrOverwrite, IFMs, ID, IH, IW, CD, CH, CW, RW>,
              std::conditional_t<RD == 1, sub_image_2d<Bias, Activation, AddOrOverwrite, IFMs, ID, IH, IW,
                                                       CD, CH, CW, RH, RW>,
                                 sub_image_3d<Bias, Activation, AddOrOverwrite, IFMs, ID, IH, IW, CD, CH,
                                              CW, RD, RH, RW>>>>
{
};

} // namespace propagation
} // namespace phi
} // namespace znn
