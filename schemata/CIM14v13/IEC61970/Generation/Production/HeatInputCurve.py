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

from CIM14v13.IEC61970.Core.Curve import Curve

class HeatInputCurve(Curve):
    """Relationship between unit heat input in energy per time for main fuel (Y1-axis) and supplemental fuel (Y2-axis) versus unit output in active power (X-axis). The quantity of main fuel used to sustain generation at this output level is prorated for throttling between definition points. The quantity of supplemental fuel used at this output level is fixed and not prorated.
    """

    def __init__(self, heatInputEff=0.0, auxPowerOffset=0.0, heatInputOffset=0.0, isNetGrossP=False, auxPowerMult=0.0, ThermalGeneratingUnit=None, **kw_args):
        """Initializes a new 'HeatInputCurve' instance.

        @param heatInputEff: Heat input - efficiency multiplier adjustment factor. 
        @param auxPowerOffset: Power output - auxiliary power offset adjustment factor 
        @param heatInputOffset: Heat input - offset adjustment factor. 
        @param isNetGrossP: Flag is set to true when output is expressed in net active power 
        @param auxPowerMult: Power output - auxiliary power multiplier adjustment factor. 
        @param ThermalGeneratingUnit: A thermal generating unit may have a heat input curve
        """
        #: Heat input - efficiency multiplier adjustment factor.
        self.heatInputEff = heatInputEff

        #: Power output - auxiliary power offset adjustment factor
        self.auxPowerOffset = auxPowerOffset

        #: Heat input - offset adjustment factor.
        self.heatInputOffset = heatInputOffset

        #: Flag is set to true when output is expressed in net active power
        self.isNetGrossP = isNetGrossP

        #: Power output - auxiliary power multiplier adjustment factor.
        self.auxPowerMult = auxPowerMult

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(HeatInputCurve, self).__init__(**kw_args)

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may have a heat input curve
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._HeatInputCurve = None

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._HeatInputCurve = self

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)

