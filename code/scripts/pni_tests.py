/usr/local/lib/python2.7/dist-packages/h5py/__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  from ._conv import register_converters as _register_converters
make: Entering directory '/opt/znnphi_interface/code/znet'
rm -rf out
mkdir -p out
mkdir -p out/weights
python src/znet_generator/main.py /opt/znnphi_interface/code/znet/src/python/pznet/.tmp/net.json /tests/pni_unet/weights.h5 src/generated/znet.cpp AVX2 1 2 0 all
/usr/local/lib/python2.7/dist-packages/h5py/__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  from ._conv import register_converters as _register_converters
Parsing the network spec...
Loading the weights...
Optimizing the net...
Removing Sum1!
Removing Sum2!
Removing Sum3!
Removing Sum4!
Removing Sum5!
Removing Sum6!
Removing Merge1!
Removing Sum7!
Removing Merge2!
Removing Sum8!
Removing Merge3!
Removing Sum9!
Removing Merge4!
Removing Sum10!
Removing Merge5!
Removing Sum11!
Removing ELU1!
Removing BN1!
Removing Scale1!
Removing ELU2!
Removing BN2!
Removing Scale2!
Removing ELU3!
Removing BN3!
Removing Scale3!
Removing ELU4!
Removing BN4!
Removing Scale4!
Removing ELU5!
Removing BN5!
Removing Scale5!
Removing ELU6!
Removing BN6!
Removing Scale6!
Removing ELU7!
Removing BN7!
Removing Scale7!
Removing ELU8!
Removing BN8!
Removing Scale8!
Removing ELU9!
Removing BN9!
Removing Scale9!
Removing ELU10!
Removing BN10!
Removing Scale10!
Removing ELU11!
Removing BN11!
Removing Scale11!
Removing ELU12!
Removing BN12!
Removing Scale12!
Removing ELU13!
Removing BN13!
Removing Scale13!
Removing ELU14!
Removing BN14!
Removing Scale14!
Removing ELU15!
Removing BN15!
Removing Scale15!
Removing ELU16!
Removing BN16!
Removing Scale16!
Removing ELU17!
Removing BN17!
Removing Scale17!
Removing ELU18!
Removing BN18!
Removing Scale18!
Removing ELU19!
Removing BN19!
Removing Scale19!
Removing ELU20!
Removing BN20!
Removing Scale20!
Removing ELU21!
Removing BN21!
Removing Scale21!
Removing ELU22!
Removing BN22!
Removing Scale22!
Removing ELU23!
Removing BN23!
Removing Scale23!
Removing ELU24!
Removing BN24!
Removing Scale24!
Removing ELU25!
Removing BN25!
Removing Scale25!
Removing ELU26!
Removing BN26!
Removing Scale26!
Removing ELU27!
Removing BN27!
Removing Scale27!
Removing ELU28!
Removing BN28!
Removing Scale28!
Removing ELU29!
Removing BN29!
Removing Scale29!
Removing ELU30!
Removing BN30!
Removing Scale30!
Removing ELU31!
Removing BN31!
Removing Scale31!
Removing ELU32!
Removing BN32!
Removing Scale32!
Removing ELU33!
Removing BN33!
Removing Scale33!
Removing ELU34!
Removing BN34!
Removing Scale34!
Removing ELU35!
Removing BN35!
Removing Scale35!
Removing ELU36!
Removing BN36!
Removing Scale36!
Removing ELU37!
Removing BN37!
Removing Scale37!
Removing ELU38!
Removing BN38!
Removing Scale38!
Removing ELU39!
Removing ELU40!
Output paddinig for Conv1!
Output paddinig for Conv3!
Output paddinig for Conv6!
Output paddinig for Conv9!
Output paddinig for Conv12!
Output paddinig for Conv15!
Output paddinig for Conv18!
Output paddinig for Conv22!
Output paddinig for Conv26!
Output paddinig for Conv30!
Output paddinig for Conv34!
Output paddinig for Conv38!
Generating the network...
   Generating constructors...
   Generating foward pass...
Done!
icpc: command line warning #10006: ignoring unknown option '-Wdate-time'
icpc: warning #10315: specifying -lm before files may supersede the Intel(R) math library and affect performance
icpc: command line remark #10411: option '-openmp' is deprecated and will be removed in a future release. Please use the replacement option '-qopenmp'
make: Leaving directory '/opt/znnphi_interface/code/znet'
make: Entering directory '/opt/znnphi_interface/code/znet'
rm -rf out
mkdir -p out
mkdir -p out/weights
python src/znet_generator/main.py /opt/znnphi_interface/code/znet/src/python/pznet/.tmp/net.json /tests/pni_unet/weights.h5 src/generated/znet.cpp AVX2 1 2 0 ,no_pad,
/usr/local/lib/python2.7/dist-packages/h5py/__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  from ._conv import register_converters as _register_converters
Parsing the network spec...
Loading the weights...
Optimizing the net...
Removing Sum1!
Removing Sum2!
Removing Sum3!
Removing Sum4!
Removing Sum5!
Removing Sum6!
Removing Merge1!
Removing Sum7!
Removing Merge2!
Removing Sum8!
Removing Merge3!
Removing Sum9!
Removing Merge4!
Removing Sum10!
Removing Merge5!
Removing Sum11!
Removing ELU1!
Removing BN1!
Removing Scale1!
Removing ELU2!
Removing BN2!
Removing Scale2!
Removing ELU3!
Removing BN3!
Removing Scale3!
Removing ELU4!
Removing BN4!
Removing Scale4!
Removing ELU5!
Removing BN5!
Removing Scale5!
Removing ELU6!
Removing BN6!
Removing Scale6!
Removing ELU7!
Removing BN7!
Removing Scale7!
Removing ELU8!
Removing BN8!
Removing Scale8!
Removing ELU9!
Removing BN9!
Removing Scale9!
Removing ELU10!
Removing BN10!
Removing Scale10!
Removing ELU11!
Removing BN11!
Removing Scale11!
Removing ELU12!
Removing BN12!
Removing Scale12!
Removing ELU13!
Removing BN13!
Removing Scale13!
Removing ELU14!
Removing BN14!
Removing Scale14!
Removing ELU15!
Removing BN15!
Removing Scale15!
Removing ELU16!
Removing BN16!
Removing Scale16!
Removing ELU17!
Removing BN17!
Removing Scale17!
Removing ELU18!
Removing BN18!
Removing Scale18!
Removing ELU19!
Removing BN19!
Removing Scale19!
Removing ELU20!
Removing BN20!
Removing Scale20!
Removing ELU21!
Removing BN21!
Removing Scale21!
Removing ELU22!
Removing BN22!
Removing Scale22!
Removing ELU23!
Removing BN23!
Removing Scale23!
Removing ELU24!
Removing BN24!
Removing Scale24!
Removing ELU25!
Removing BN25!
Removing Scale25!
Removing ELU26!
Removing BN26!
Removing Scale26!
Removing ELU27!
Removing BN27!
Removing Scale27!
Removing ELU28!
Removing BN28!
Removing Scale28!
Removing ELU29!
Removing BN29!
Removing Scale29!
Removing ELU30!
Removing BN30!
Removing Scale30!
Removing ELU31!
Removing BN31!
Removing Scale31!
Removing ELU32!
Removing BN32!
Removing Scale32!
Removing ELU33!
Removing BN33!
Removing Scale33!
Removing ELU34!
Removing BN34!
Removing Scale34!
Removing ELU35!
Removing BN35!
Removing Scale35!
Removing ELU36!
Removing BN36!
Removing Scale36!
Removing ELU37!
Removing BN37!
Removing Scale37!
Removing ELU38!
Removing BN38!
Removing Scale38!
Removing ELU39!
Removing ELU40!
Generating the network...
   Generating constructors...
   Generating foward pass...
Done!
icpc: command line warning #10006: ignoring unknown option '-Wdate-time'
icpc: warning #10315: specifying -lm before files may supersede the Intel(R) math library and affect performance
icpc: command line remark #10411: option '-openmp' is deprecated and will be removed in a future release. Please use the replacement option '-qopenmp'
make: Leaving directory '/opt/znnphi_interface/code/znet'
make: Entering directory '/opt/znnphi_interface/code/znet'
rm -rf out
mkdir -p out
mkdir -p out/weights
python src/znet_generator/main.py /opt/znnphi_interface/code/znet/src/python/pznet/.tmp/net.json /tests/pni_unet/weights.h5 src/generated/znet.cpp AVX2 1 2 0 ,no_add,
/usr/local/lib/python2.7/dist-packages/h5py/__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  from ._conv import register_converters as _register_converters
Parsing the network spec...
Loading the weights...
Optimizing the net...
Removing ELU1!
Removing BN1!
Removing Scale1!
Removing ELU2!
Removing BN2!
Removing Scale2!
Removing ELU3!
Removing BN4!
Removing Scale4!
Removing ELU5!
Removing BN5!
Removing Scale5!
Removing ELU6!
Removing BN7!
Removing Scale7!
Removing ELU8!
Removing BN8!
Removing Scale8!
Removing ELU9!
Removing BN10!
Removing Scale10!
Removing ELU11!
Removing BN11!
Removing Scale11!
Removing ELU12!
Removing BN13!
Removing Scale13!
Removing ELU14!
Removing BN14!
Removing Scale14!
Removing ELU15!
Removing BN16!
Removing Scale16!
Removing ELU17!
Removing BN17!
Removing Scale17!
Removing ELU18!
Removing BN20!
Removing Scale20!
Removing ELU21!
Removing BN21!
Removing Scale21!
Removing ELU22!
Removing BN24!
Removing Scale24!
Removing ELU25!
Removing BN25!
Removing Scale25!
Removing ELU26!
Removing BN28!
Removing Scale28!
Removing ELU29!
Removing BN29!
Removing Scale29!
Removing ELU30!
Removing BN32!
Removing Scale32!
Removing ELU33!
Removing BN33!
Removing Scale33!
Removing ELU34!
Removing BN36!
Removing Scale36!
Removing ELU37!
Removing BN37!
Removing Scale37!
Removing ELU38!
Removing ELU40!
Output paddinig for Conv1!
Output paddinig for Conv3!
Output paddinig for Conv6!
Output paddinig for Conv9!
Output paddinig for Conv12!
Output paddinig for Conv15!
Output paddinig for Conv18!
Output paddinig for Conv22!
Output paddinig for Conv26!
Output paddinig for Conv30!
Output paddinig for Conv34!
Output paddinig for Conv38!
Generating the network...
   Generating constructors...
   Generating foward pass...
Done!
icpc: command line warning #10006: ignoring unknown option '-Wdate-time'
icpc: warning #10315: specifying -lm before files may supersede the Intel(R) math library and affect performance
icpc: command line remark #10411: option '-openmp' is deprecated and will be removed in a future release. Please use the replacement option '-qopenmp'
make: Leaving directory '/opt/znnphi_interface/code/znet'
make: Entering directory '/opt/znnphi_interface/code/znet'
rm -rf out
mkdir -p out
mkdir -p out/weights
python src/znet_generator/main.py /opt/znnphi_interface/code/znet/src/python/pznet/.tmp/net.json /tests/pni_unet/weights.h5 src/generated/znet.cpp AVX2 1 2 0 ,no_act,
/usr/local/lib/python2.7/dist-packages/h5py/__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  from ._conv import register_converters as _register_converters
Parsing the network spec...
Loading the weights...
Optimizing the net...
Removing Sum1!
Removing Sum2!
Removing Sum3!
Removing Sum4!
Removing Sum5!
Removing Sum6!
Removing Merge1!
Removing Sum7!
Removing Merge2!
Removing Sum8!
Removing Merge3!
Removing Sum9!
Removing Merge4!
Removing Sum10!
Removing Merge5!
Removing Sum11!
Removing BN1!
Removing Scale1!
Removing BN2!
Removing Scale2!
Removing BN3!
Removing Scale3!
Removing BN4!
Removing Scale4!
Removing BN5!
Removing Scale5!
Removing BN6!
Removing Scale6!
Removing BN7!
Removing Scale7!
Removing BN8!
Removing Scale8!
Removing BN9!
Removing Scale9!
Removing BN10!
Removing Scale10!
Removing BN11!
Removing Scale11!
Removing BN12!
Removing Scale12!
Removing BN13!
Removing Scale13!
Removing BN14!
Removing Scale14!
Removing BN15!
Removing Scale15!
Removing BN16!
Removing Scale16!
Removing BN17!
Removing Scale17!
Removing BN18!
Removing Scale18!
Removing BN19!
Removing Scale19!
Removing BN20!
Removing Scale20!
Removing BN21!
Removing Scale21!
Removing BN22!
Removing Scale22!
Removing BN23!
Removing Scale23!
Removing BN24!
Removing Scale24!
Removing BN25!
Removing Scale25!
Removing BN26!
Removing Scale26!
Removing BN27!
Removing Scale27!
Removing BN28!
Removing Scale28!
Removing BN29!
Removing Scale29!
Removing BN30!
Removing Scale30!
Removing BN31!
Removing Scale31!
Removing BN32!
Removing Scale32!
Removing BN33!
Removing Scale33!
Removing BN34!
Removing Scale34!
Removing BN35!
Removing Scale35!
Removing BN36!
Removing Scale36!
Removing BN37!
Removing Scale37!
Removing BN38!
Removing Scale38!
Generating the network...
   Generating constructors...
   Generating foward pass...
Done!
icpc: command line warning #10006: ignoring unknown option '-Wdate-time'
icpc: warning #10315: specifying -lm before files may supersede the Intel(R) math library and affect performance
icpc: command line remark #10411: option '-openmp' is deprecated and will be removed in a future release. Please use the replacement option '-qopenmp'
make: Leaving directory '/opt/znnphi_interface/code/znet'
make: Entering directory '/opt/znnphi_interface/code/znet'
rm -rf out
mkdir -p out
mkdir -p out/weights
python src/znet_generator/main.py /opt/znnphi_interface/code/znet/src/python/pznet/.tmp/net.json /tests/pni_unet/weights.h5 src/generated/znet.cpp AVX2 1 2 0 ,no_lin,no_pad,
/usr/local/lib/python2.7/dist-packages/h5py/__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  from ._conv import register_converters as _register_converters
Parsing the network spec...
Loading the weights...
Optimizing the net...
Removing Sum1!
Removing Sum2!
Removing Sum3!
Removing Sum4!
Removing Sum5!
Removing Sum6!
Removing Merge1!
Removing Sum7!
Removing Merge2!
Removing Sum8!
Removing Merge3!
Removing Sum9!
Removing Merge4!
Removing Sum10!
Removing Merge5!
Removing Sum11!
Removing ELU1!
Removing ELU40!
Generating the network...
   Generating constructors...
   Generating foward pass...
Done!
icpc: command line warning #10006: ignoring unknown option '-Wdate-time'
icpc: warning #10315: specifying -lm before files may supersede the Intel(R) math library and affect performance
icpc: command line remark #10411: option '-openmp' is deprecated and will be removed in a future release. Please use the replacement option '-qopenmp'
make: Leaving directory '/opt/znnphi_interface/code/znet'
Creating nets...
Running nets...
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=72 OFM=48 ID=22 IHW=56 KD=1 KHW=1 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_22_72_56_1_1_48_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=48 OFM=48 ID=24 IHW=58 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_48_58_3_3_48_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=104 OFM=104 ID=24 IHW=16 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_104_16_3_3_104_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=104 OFM=104 ID=24 IHW=16 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_24_104_16_3_3_104_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=144 OFM=104 ID=22 IHW=14 KD=1 KHW=1 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_22_144_14_1_1_104_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=104 OFM=104 ID=24 IHW=16 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_104_16_3_3_104_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=72 OFM=72 ID=24 IHW=30 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_72_30_3_3_72_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=72 OFM=72 ID=24 IHW=30 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_24_72_30_3_3_72_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=104 OFM=72 ID=22 IHW=28 KD=1 KHW=1 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_22_104_28_1_1_72_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=72 OFM=72 ID=24 IHW=30 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_72_30_3_3_72_0_0_0_0_1_1_0.so
1 2
1 2
1 2
1 2
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=24 OFM=24 ID=24 IHW=226 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_24_24_226_3_3_24_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=24 OFM=24 ID=24 IHW=226 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_24_226_3_3_24_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=48 OFM=48 ID=24 IHW=58 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_24_48_58_3_3_48_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=48 OFM=48 ID=24 IHW=58 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_48_58_3_3_48_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=32 OFM=32 ID=24 IHW=114 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_32_114_3_3_32_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=48 OFM=32 ID=22 IHW=112 KD=1 KHW=1 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_22_48_112_1_1_32_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=32 OFM=32 ID=24 IHW=114 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_24_32_114_3_3_32_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=32 OFM=32 ID=24 IHW=114 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_32_114_3_3_32_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=24 OFM=24 ID=24 IHW=226 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_24_226_3_3_24_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=32 OFM=24 ID=22 IHW=224 KD=1 KHW=1 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_22_32_224_1_1_24_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=24 OFM=24 ID=24 IHW=226 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_24_226_3_3_24_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=24 OFM=24 ID=24 IHW=226 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_24_226_3_3_24_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=8 OFM=24 ID=22 IHW=228 KD=1 KHW=5 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_22_8_228_1_5_24_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=32 OFM=32 ID=24 IHW=114 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_24_32_114_3_3_32_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=32 OFM=32 ID=24 IHW=114 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_32_114_3_3_32_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=24 OFM=32 ID=24 IHW=114 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_24_114_3_3_32_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=24 OFM=24 ID=24 IHW=226 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_24_24_226_3_3_24_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=48 OFM=48 ID=24 IHW=58 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_48_58_3_3_48_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=32 OFM=48 ID=24 IHW=58 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_32_58_3_3_48_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=72 OFM=72 ID=24 IHW=30 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_24_72_30_3_3_72_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=72 OFM=72 ID=24 IHW=30 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_72_30_3_3_72_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=48 OFM=72 ID=24 IHW=30 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_48_30_3_3_72_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=48 OFM=48 ID=24 IHW=58 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_24_48_58_3_3_48_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=104 OFM=144 ID=24 IHW=9 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_104_9_3_3_144_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=104 OFM=104 ID=24 IHW=16 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_24_104_16_3_3_104_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=104 OFM=104 ID=24 IHW=16 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_104_16_3_3_104_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=72 OFM=104 ID=24 IHW=16 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_72_16_3_3_104_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=144 OFM=144 ID=24 IHW=9 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_true_AVX2_1_1_0_2_24_144_9_3_3_144_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=144 OFM=144 ID=24 IHW=9 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_24_144_9_3_3_144_0_0_1_1_1_1_0.so
1 2
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=24 OFM=24 ID=22 IHW=228 KD=1 KHW=5 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_1_false_AVX2_1_1_0_2_22_24_228_1_5_24_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_all/lib BN=1 IFM=24 OFM=16 ID=22 IHW=224 KD=1 KHW=1 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=0 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_all/lib/conv_0_false_AVX2_1_1_0_2_22_24_224_1_1_16_0_0_0_0_1_1_0.so
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.50863
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.50662
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.50724
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.50813
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.50823
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.51424
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.51024
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.50562
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.50432
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.5101
Forward Finished
all: 5.51344738007sec
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=72 OFM=48 ID=22 IHW=56 KD=1 KHW=1 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_22_72_56_1_1_48_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=48 OFM=48 ID=24 IHW=58 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_48_58_3_3_48_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=104 OFM=104 ID=24 IHW=16 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_104_16_3_3_104_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=104 OFM=104 ID=24 IHW=16 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_24_104_16_3_3_104_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=144 OFM=104 ID=22 IHW=14 KD=1 KHW=1 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_22_144_14_1_1_104_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=104 OFM=104 ID=24 IHW=16 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_104_16_3_3_104_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=72 OFM=72 ID=24 IHW=30 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_72_30_3_3_72_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=72 OFM=72 ID=24 IHW=30 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_24_72_30_3_3_72_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=104 OFM=72 ID=22 IHW=28 KD=1 KHW=1 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_22_104_28_1_1_72_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=72 OFM=72 ID=24 IHW=30 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_72_30_3_3_72_0_0_0_0_1_1_0.so
1 2
1 2
1 2
1 2
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=24 OFM=24 ID=24 IHW=226 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_24_24_226_3_3_24_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=24 OFM=24 ID=24 IHW=226 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_24_226_3_3_24_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=48 OFM=48 ID=24 IHW=58 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_24_48_58_3_3_48_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=48 OFM=48 ID=24 IHW=58 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_48_58_3_3_48_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=32 OFM=32 ID=24 IHW=114 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_32_114_3_3_32_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=48 OFM=32 ID=22 IHW=112 KD=1 KHW=1 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_22_48_112_1_1_32_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=32 OFM=32 ID=24 IHW=114 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_24_32_114_3_3_32_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=32 OFM=32 ID=24 IHW=114 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_32_114_3_3_32_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=24 OFM=24 ID=24 IHW=226 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_24_226_3_3_24_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=32 OFM=24 ID=22 IHW=224 KD=1 KHW=1 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_22_32_224_1_1_24_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=24 OFM=24 ID=24 IHW=226 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_24_226_3_3_24_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=24 OFM=24 ID=24 IHW=226 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_24_226_3_3_24_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=8 OFM=24 ID=22 IHW=228 KD=1 KHW=5 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_22_8_228_1_5_24_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=32 OFM=32 ID=24 IHW=114 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_24_32_114_3_3_32_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=32 OFM=32 ID=24 IHW=114 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_32_114_3_3_32_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=24 OFM=32 ID=24 IHW=114 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_24_114_3_3_32_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=24 OFM=24 ID=24 IHW=226 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_24_24_226_3_3_24_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=48 OFM=48 ID=24 IHW=58 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_48_58_3_3_48_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=32 OFM=48 ID=24 IHW=58 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_32_58_3_3_48_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=72 OFM=72 ID=24 IHW=30 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_24_72_30_3_3_72_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=72 OFM=72 ID=24 IHW=30 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_72_30_3_3_72_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=48 OFM=72 ID=24 IHW=30 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_48_30_3_3_72_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=48 OFM=48 ID=24 IHW=58 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_24_48_58_3_3_48_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=104 OFM=144 ID=24 IHW=9 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_104_9_3_3_144_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=104 OFM=104 ID=24 IHW=16 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_24_104_16_3_3_104_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=104 OFM=104 ID=24 IHW=16 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_104_16_3_3_104_0_0_1_1_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=72 OFM=104 ID=24 IHW=16 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_72_16_3_3_104_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=144 OFM=144 ID=24 IHW=9 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_true_AVX2_1_1_0_2_24_144_9_3_3_144_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=144 OFM=144 ID=24 IHW=9 KD=3 KHW=3 OUT_D_SKIP=0 OUT_PADD=1 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=1 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_24_144_9_3_3_144_0_0_1_1_1_1_0.so
1 2
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=24 OFM=24 ID=22 IHW=228 KD=1 KHW=5 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_1_false_AVX2_1_1_0_2_22_24_228_1_5_24_0_0_0_0_1_1_0.so
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_pad/lib BN=1 IFM=24 OFM=16 ID=22 IHW=224 KD=1 KHW=1 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=0 ADDOROVERWRITE=false ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
dl_filename: /opt/znets/pni_unet_1cores_opt_no_pad/lib/conv_0_false_AVX2_1_1_0_2_22_24_224_1_1_16_0_0_0_0_1_1_0.so
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.53509
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.5131
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.50991
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.51328
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.51058
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.51392
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.5124
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.515
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.52067
Forward Finished
Copying 4415488 bytes into the user input. 
Starting Forward Pass
average:5.52503
Forward Finished
no_pad: 5.52361650467sec
/opt/znnphi_interface/code/include/znn/jit/jit.py LAYER=conv LIB_FOLDER=/opt/znets/pni_unet_1cores_opt_no_add/lib BN=1 IFM=72 OFM=48 ID=22 IHW=56 KD=1 KHW=1 OUT_D_SKIP=0 OUT_PADD=0 OUT_H_SKIP=0 OUT_W_SKIP=0 OUT_PADHW=0 OUT_STRIDE_D=1 OUT_STRIDE_HW=1 ACTIVATION=1 ADDOROVERWRITE=true ARCH=AVX2 CORES=1 HT=2 CPU_OFFSET=0
Calling jit.py failed
