# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.2)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x00\x58\
\x3c\
\x52\x43\x43\x3e\x0a\x20\x20\x3c\x71\x72\x65\x73\x6f\x75\x72\x63\
\x65\x20\x70\x72\x65\x66\x69\x78\x3d\x22\x6e\x65\x77\x50\x72\x65\
\x66\x69\x78\x22\x3e\x0a\x20\x20\x20\x20\x3c\x66\x69\x6c\x65\x3e\
\x6d\x79\x72\x65\x73\x2e\x71\x72\x63\x3c\x2f\x66\x69\x6c\x65\x3e\
\x0a\x20\x20\x3c\x2f\x71\x72\x65\x73\x6f\x75\x72\x63\x65\x3e\x0a\
\x3c\x2f\x52\x43\x43\x3e\x0a\
"

qt_resource_name = b"\
\x00\x09\
\x0c\x78\x54\x88\
\x00\x6e\
\x00\x65\x00\x77\x00\x50\x00\x72\x00\x65\x00\x66\x00\x69\x00\x78\
\x00\x09\
\x08\xc6\xb2\x83\
\x00\x6d\
\x00\x79\x00\x72\x00\x65\x00\x73\x00\x2e\x00\x71\x00\x72\x00\x63\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x80\x16\xc3\xf7\x81\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
