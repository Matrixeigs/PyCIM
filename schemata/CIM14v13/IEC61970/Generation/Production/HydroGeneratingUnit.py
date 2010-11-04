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

from CIM14v13.IEC61970.Generation.Production.GeneratingUnit import GeneratingUnit

class HydroGeneratingUnit(GeneratingUnit):
    """A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)
    """

    def __init__(self, energyConversionCapability='generator', hydroUnitWaterCost=0.0, TailbayLossCurve=None, HydroPowerPlant=None, PenstockLossCurve=None, HydroGeneratingEfficiencyCurves=None, **kw_args):
        """Initializes a new 'HydroGeneratingUnit' instance.

        @param energyConversionCapability: Energy conversion capability for generating. Values are: "generator", "pumpAndGenerator"
        @param hydroUnitWaterCost: The equivalent cost of water that drives the hydro turbine, expressed as cost per volume. 
        @param TailbayLossCurve: A hydro generating unit has a tailbay loss curve
        @param HydroPowerPlant: The hydro generating unit belongs to a hydro power plant
        @param PenstockLossCurve: A hydro generating unit has a penstock loss curve
        @param HydroGeneratingEfficiencyCurves: A hydro generating unit has an efficiency curve
        """
        #: Energy conversion capability for generating.Values are: "generator", "pumpAndGenerator"
        self.energyConversionCapability = energyConversionCapability

        #: The equivalent cost of water that drives the hydro turbine, expressed as cost per volume.
        self.hydroUnitWaterCost = hydroUnitWaterCost

        self._TailbayLossCurve = []
        self.TailbayLossCurve = [] if TailbayLossCurve is None else TailbayLossCurve

        self._HydroPowerPlant = None
        self.HydroPowerPlant = HydroPowerPlant

        self._PenstockLossCurve = None
        self.PenstockLossCurve = PenstockLossCurve

        self._HydroGeneratingEfficiencyCurves = []
        self.HydroGeneratingEfficiencyCurves = [] if HydroGeneratingEfficiencyCurves is None else HydroGeneratingEfficiencyCurves

        super(HydroGeneratingUnit, self).__init__(**kw_args)

    def getTailbayLossCurve(self):
        """A hydro generating unit has a tailbay loss curve
        """
        return self._TailbayLossCurve

    def setTailbayLossCurve(self, value):
        for x in self._TailbayLossCurve:
            x._HydroGeneratingUnit = None
        for y in value:
            y._HydroGeneratingUnit = self
        self._TailbayLossCurve = value

    TailbayLossCurve = property(getTailbayLossCurve, setTailbayLossCurve)

    def addTailbayLossCurve(self, *TailbayLossCurve):
        for obj in TailbayLossCurve:
            obj._HydroGeneratingUnit = self
            self._TailbayLossCurve.append(obj)

    def removeTailbayLossCurve(self, *TailbayLossCurve):
        for obj in TailbayLossCurve:
            obj._HydroGeneratingUnit = None
            self._TailbayLossCurve.remove(obj)

    def getHydroPowerPlant(self):
        """The hydro generating unit belongs to a hydro power plant
        """
        return self._HydroPowerPlant

    def setHydroPowerPlant(self, value):
        if self._HydroPowerPlant is not None:
            filtered = [x for x in self.HydroPowerPlant.HydroGeneratingUnits if x != self]
            self._HydroPowerPlant._HydroGeneratingUnits = filtered

        self._HydroPowerPlant = value
        if self._HydroPowerPlant is not None:
            self._HydroPowerPlant._HydroGeneratingUnits.append(self)

    HydroPowerPlant = property(getHydroPowerPlant, setHydroPowerPlant)

    def getPenstockLossCurve(self):
        """A hydro generating unit has a penstock loss curve
        """
        return self._PenstockLossCurve

    def setPenstockLossCurve(self, value):
        if self._PenstockLossCurve is not None:
            self._PenstockLossCurve._HydroGeneratingUnit = None

        self._PenstockLossCurve = value
        if self._PenstockLossCurve is not None:
            self._PenstockLossCurve._HydroGeneratingUnit = self

    PenstockLossCurve = property(getPenstockLossCurve, setPenstockLossCurve)

    def getHydroGeneratingEfficiencyCurves(self):
        """A hydro generating unit has an efficiency curve
        """
        return self._HydroGeneratingEfficiencyCurves

    def setHydroGeneratingEfficiencyCurves(self, value):
        for x in self._HydroGeneratingEfficiencyCurves:
            x._HydroGeneratingUnit = None
        for y in value:
            y._HydroGeneratingUnit = self
        self._HydroGeneratingEfficiencyCurves = value

    HydroGeneratingEfficiencyCurves = property(getHydroGeneratingEfficiencyCurves, setHydroGeneratingEfficiencyCurves)

    def addHydroGeneratingEfficiencyCurves(self, *HydroGeneratingEfficiencyCurves):
        for obj in HydroGeneratingEfficiencyCurves:
            obj._HydroGeneratingUnit = self
            self._HydroGeneratingEfficiencyCurves.append(obj)

    def removeHydroGeneratingEfficiencyCurves(self, *HydroGeneratingEfficiencyCurves):
        for obj in HydroGeneratingEfficiencyCurves:
            obj._HydroGeneratingUnit = None
            self._HydroGeneratingEfficiencyCurves.remove(obj)

