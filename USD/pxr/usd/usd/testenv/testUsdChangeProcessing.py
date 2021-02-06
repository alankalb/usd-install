#!/pxrpythonsubst
#
# Copyright 2017 Pixar
#
# Licensed under the Apache License, Version 2.0 (the "Apache License")
# with the following modification; you may not use this file except in
# compliance with the Apache License and the following modification to it:
# Section 6. Trademarks. is deleted and replaced with:
#
# 6. Trademarks. This License does not grant permission to use the trade
#    names, trademarks, service marks, or product names of the Licensor
#    and its affiliates, except as required to comply with Section 4(c) of
#    the License and to reproduce the content of the NOTICE file.
#
# You may obtain a copy of the Apache License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the Apache License with the above modification is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the Apache License for the specific
# language governing permissions and limitations under the Apache License.

from __future__ import print_function

import sys
from pxr import Sdf,Usd,Tf

def RenamingSpec():
    '''Test renaming a SdfPrimSpec.'''
    stage = Usd.Stage.CreateInMemory()
    layer = stage.GetRootLayer()

    parent = stage.DefinePrim("/parent")
    child = stage.DefinePrim("/parent/child")

    assert stage.GetPrimAtPath('/parent')
    assert stage.GetPrimAtPath('/parent/child')
    layer.GetPrimAtPath(parent.GetPath()).name = "parent_renamed"
    assert stage.GetPrimAtPath('/parent_renamed')
    assert stage.GetPrimAtPath('/parent_renamed/child')

def ChangeInsignificantSublayer():
    '''Test making changes after adding an insignificant sublayer.'''
    stage = Usd.Stage.CreateInMemory()
    layer = stage.GetRootLayer()

    insignificantSublayer = Sdf.Layer.CreateAnonymous(".usda")
    assert insignificantSublayer.empty

    layer.subLayerPaths.append(insignificantSublayer.identifier)
    assert insignificantSublayer in stage.GetUsedLayers()

    with Usd.EditContext(stage, insignificantSublayer):
        prim = stage.DefinePrim("/Foo")
        assert prim

def Main(argv):
    RenamingSpec()
    ChangeInsignificantSublayer()

if __name__ == "__main__":
    Main(sys.argv)
    print('OK')

