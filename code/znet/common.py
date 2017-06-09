from math import ceil
import numpy as np

#TODO: FIX FOR VARIABLE SIMD
S = 8

def round_to_simd(n):
    return int(ceil(float(n) / S) * S);

def block_kernel(kernel, lparam):
    blocked_kernel = np.array([0]*lparam['kernel_size'])

    def h5ker_to_znnphiker(ofm, ifm, kz, kx, ky):
        offset = ofm/S
        offset *= lparam["ifm"]/S
        offset += ifm/S
        offset *= lparam["kdim"][0]
        offset += kz
        offset *= lparam["kdim"][1]
        offset += kx
        offset *= lparam["kdim"][2]
        offset += ky
        offset *= S
        offset += ofm % S
        offset *= S
        offset += ifm % S
        return offset

    # h5 weight format: ofm-ifm-kz-kx-ky
    # output format: ofm/S-ifm/S-kz-kx-ky-ofm%S-ifm%S
    for ofm in range(lparam["ofm"]):
        for ifm in range(lparam["ifm"]):
            for kz in range(lparam["kdim"][0]):
                for kx in range(lparam["kdim"][1]):
                    for ky in range(lparam["kdim"][2]):
                        znnphi_index = h5ker_to_znnphiker(ofm, ifm, kz, kx, ky)
                        blocked_kernel[znnphi_index] = kernel[ofm][ifm][kz][kx][ky]

    return blocked_kernel


def block_bias(bias, lparam):
    blocked_bias = np.array([0]*lparam['bias_size'])
    for ofm in range(lparam["ofm"]):
        blocked_bias[ofm] = bias[ofm]

    return blocked_bias

