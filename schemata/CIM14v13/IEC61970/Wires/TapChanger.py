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

from CIM14v13.IEC61970.Core.PowerSystemResource import PowerSystemResource

class TapChanger(PowerSystemResource):
    """Mechanism for changing transformer winding tap positions.
    """

    def __init__(self, neutralStep=0, subsequentDelay=0.0, neutralU=0.0, stepVoltageIncrement=0.0, lowStep=0, normalStep=0, regulationStatus=False, highStep=0, initialDelay=0.0, ltcFlag=False, RegulatingControl=None, ImpedanceVariationCurve=None, SvTapStep=None, TapSchedules=None, **kw_args):
        """Initializes a new 'TapChanger' instance.

        @param neutralStep: The neutral tap step position for this winding. 
        @param subsequentDelay: For an LTC, the delay for subsequent tap changer operation (second and later step changes) 
        @param neutralU: Voltage at which the winding operates at the neutral tap setting. 
        @param stepVoltageIncrement: Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step. 
        @param lowStep: Lowest possible tap step position, retard from neutral 
        @param normalStep: The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting. 
        @param regulationStatus: Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating. 
        @param highStep: Highest possible tap step position, advance from neutral 
        @param initialDelay: For an LTC, the delay for initial tap changer operation (first step change) 
        @param ltcFlag: Specifies whether or not a TapChanger has load tap changing capabilities. 
        @param RegulatingControl:
        @param ImpedanceVariationCurve: A TapChanger can have an associated ImpedanceVariationCurve to define impedance variations with tap step changes.
        @param SvTapStep: The tap step state associated with the tap changer.
        @param TapSchedules: A TapChanger can have TapSchedules.
        """
        #: The neutral tap step position for this winding.
        self.neutralStep = neutralStep

        #: For an LTC, the delay for subsequent tap changer operation (second and later step changes)
        self.subsequentDelay = subsequentDelay

        #: Voltage at which the winding operates at the neutral tap setting.
        self.neutralU = neutralU

        #: Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.
        self.stepVoltageIncrement = stepVoltageIncrement

        #: Lowest possible tap step position, retard from neutral
        self.lowStep = lowStep

        #: The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
        self.normalStep = normalStep

        #: Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating.
        self.regulationStatus = regulationStatus

        #: Highest possible tap step position, advance from neutral
        self.highStep = highStep

        #: For an LTC, the delay for initial tap changer operation (first step change)
        self.initialDelay = initialDelay

        #: Specifies whether or not a TapChanger has load tap changing capabilities.
        self.ltcFlag = ltcFlag

        self._RegulatingControl = None
        self.RegulatingControl = RegulatingControl

        self._ImpedanceVariationCurve = None
        self.ImpedanceVariationCurve = ImpedanceVariationCurve

        self._SvTapStep = None
        self.SvTapStep = SvTapStep

        self._TapSchedules = []
        self.TapSchedules = [] if TapSchedules is None else TapSchedules

        super(TapChanger, self).__init__(**kw_args)

    def getRegulatingControl(self):
        
        return self._RegulatingControl

    def setRegulatingControl(self, value):
        if self._RegulatingControl is not None:
            filtered = [x for x in self.RegulatingControl.TapChanger if x != self]
            self._RegulatingControl._TapChanger = filtered

        self._RegulatingControl = value
        if self._RegulatingControl is not None:
            self._RegulatingControl._TapChanger.append(self)

    RegulatingControl = property(getRegulatingControl, setRegulatingControl)

    def getImpedanceVariationCurve(self):
        """A TapChanger can have an associated ImpedanceVariationCurve to define impedance variations with tap step changes.
        """
        return self._ImpedanceVariationCurve

    def setImpedanceVariationCurve(self, value):
        if self._ImpedanceVariationCurve is not None:
            self._ImpedanceVariationCurve._TapChanger = None

        self._ImpedanceVariationCurve = value
        if self._ImpedanceVariationCurve is not None:
            self._ImpedanceVariationCurve._TapChanger = self

    ImpedanceVariationCurve = property(getImpedanceVariationCurve, setImpedanceVariationCurve)

    def getSvTapStep(self):
        """The tap step state associated with the tap changer.
        """
        return self._SvTapStep

    def setSvTapStep(self, value):
        if self._SvTapStep is not None:
            self._SvTapStep._TapChanger = None

        self._SvTapStep = value
        if self._SvTapStep is not None:
            self._SvTapStep._TapChanger = self

    SvTapStep = property(getSvTapStep, setSvTapStep)

    def getTapSchedules(self):
        """A TapChanger can have TapSchedules.
        """
        return self._TapSchedules

    def setTapSchedules(self, value):
        for x in self._TapSchedules:
            x._TapChanger = None
        for y in value:
            y._TapChanger = self
        self._TapSchedules = value

    TapSchedules = property(getTapSchedules, setTapSchedules)

    def addTapSchedules(self, *TapSchedules):
        for obj in TapSchedules:
            obj._TapChanger = self
            self._TapSchedules.append(obj)

    def removeTapSchedules(self, *TapSchedules):
        for obj in TapSchedules:
            obj._TapChanger = None
            self._TapSchedules.remove(obj)

