""" Simple script to load from GDB to import all components

===============================================================================

This file is part of PyCortexMDebug

PyCortexMDebug is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PyCortexMDebug is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PyCortexMDebug.  If not, see <http://www.gnu.org/licenses/>.
"""
import os

# add path to cmedebug and lxml packages
sys.path.insert(0,'/home/leroy/gdbTest/PyCortexMDebug')
sys.path.insert(0,'/usr/lib/python2.7/dist-packages/')


from cmdebug.svd_gdb import LoadSVD
from cmdebug.dwt_gdb import DWT

DWT()
LoadSVD()
