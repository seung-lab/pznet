#!/usr/bin/python
import pznet
import os
import numpy as np
import h5py
import sys


input_dim    = [1, 8, 18, 192, 192]
ofm          = 28
kernel_dim   = [1, 3, 3]
layers       = ["conv", "elu"]

layers_prefix = '_'.join(layers)
base =     '/home/ubuntu/znnphi_interface/code/znet/reference/'
net_file = 'nets/{}_{}_{}_{}_{}_{}_x{}_{}_{}_o{}.prototxt'.format(layers_prefix,
                                                                    input_dim[0],
                                                                    input_dim[1],
                                                                    input_dim[2],
                                                                    input_dim[3],
                                                                    input_dim[4],
                                                                    kernel_dim[0],
                                                                    kernel_dim[1],
                                                                    kernel_dim[2],
                                                                    ofm)
weights_file = 'data/weights/weights_{}_{}_{}_{}_{}_r.h5'.format(
                                                                ofm,
                                                                input_dim[1], #ifm
                                                                kernel_dim[0],
                                                                kernel_dim[1],
                                                                kernel_dim[2])

input_file = 'data/inputs/input_{}_{}_{}_{}_{}_r.h5'.format(input_dim[0],
                                                            input_dim[1],
                                                            input_dim[2],
                                                            input_dim[3],
                                                            input_dim[4])

reference_file = 'data/reference/reference_{}_{}_{}_{}_{}_{}_x{}_{}_{}_o{}_r.h5'.format(layers_prefix,
                                                                                        input_dim[0],
                                                                                        input_dim[1],
                                                                                        input_dim[2],
                                                                                        input_dim[3],
                                                                                        input_dim[4],
                                                                                        kernel_dim[0],
                                                                                        kernel_dim[1],
                                                                                        kernel_dim[2],
                                                                                        ofm)
net_path       = os.path.join(base, net_file)
weights_path   = os.path.join(base, weights_file)
input_path     = os.path.join(base, input_file)
reference_path = os.path.join(base, reference_file)

#input_path  = sys.argv[1]
#output_path = sys.argv[2]

z = pznet.znet(net_path, weights_path)


in_file  = h5py.File(input_path)
in_a     = in_file["input"][:]
out_a    = z.forward(in_a)
reference_file = h5py.File(reference_path)
reference_a = reference_file["data"][:]

diff_a = reference_a - out_a
error = ssq = np.sum(diff_a**2)

fd = diff_a.flatten()
fo = out_a.flatten()
fr = reference_a.flatten()
boo = np.argmax(fd)
if error > 0.1:
    print "Not congrats! Error == {}".format(error)
    breakpoint() 
else:
    print "Congrats! All pass"
#out_file = h5py.File(output_path)
#out_file.create_dataset("data", data=out_a)
