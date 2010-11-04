# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61968.Informative.InfTypeAsset.StructureTypeAsset import StructureTypeAsset

class PoleTypeAsset(StructureTypeAsset):
    """Documentation for a generic pole that may be used for various purposes such as work planning. A pole typically has a single Connection with 1,2 or 3 mounting points.
    """

    def __init__(self, length=0.0, diameter=0.0, PoleModels=None, **kw_args):
        """Initializes a new 'PoleTypeAsset' instance.

        @param length: Length of the pole (inclusive of any section of the pole that may be underground post-installation). 
        @param diameter: Diameter of the pole. 
        @param PoleModels:
        """
        #: Length of the pole (inclusive of any section of the pole that may be underground post-installation).
        self.length = length

        #: Diameter of the pole.
        self.diameter = diameter

        self._PoleModels = []
        self.PoleModels = [] if PoleModels is None else PoleModels

        super(PoleTypeAsset, self).__init__(**kw_args)

    def getPoleModels(self):
        
        return self._PoleModels

    def setPoleModels(self, value):
        for x in self._PoleModels:
            x._PoleTypeAsset = None
        for y in value:
            y._PoleTypeAsset = self
        self._PoleModels = value

    PoleModels = property(getPoleModels, setPoleModels)

    def addPoleModels(self, *PoleModels):
        for obj in PoleModels:
            obj._PoleTypeAsset = self
            self._PoleModels.append(obj)

    def removePoleModels(self, *PoleModels):
        for obj in PoleModels:
            obj._PoleTypeAsset = None
            self._PoleModels.remove(obj)

