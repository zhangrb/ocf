#
# Copyright(c) 2019 Intel Corporation
# SPDX-License-Identifier: BSD-3-Clause-Clear
#
from ctypes import *

lib = None


class OcfLib:
    __lib__ = None

    @classmethod
    def getInstance(cls):
        if cls.__lib__ is None:
            lib = cdll.LoadLibrary("./pyocf/libocf.so")
            lib.ocf_volume_get_uuid.restype = c_void_p
            lib.ocf_volume_get_uuid.argtypes = [c_void_p]

            lib.ocf_core_get_front_volume.restype = c_void_p
            lib.ocf_core_get_front_volume.argtypes = [c_void_p]

            cls.__lib__ = lib

        return cls.__lib__
