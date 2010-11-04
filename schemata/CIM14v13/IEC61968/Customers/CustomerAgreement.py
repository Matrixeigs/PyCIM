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

from CIM14v13.IEC61968.Common.Agreement import Agreement

class CustomerAgreement(Agreement):
    """Agreement between the Customer and the ServiceSupplier to pay for service at a specific ServiceLocation. It records certain billing information about the type of service provided at the ServiceLocation and is used during charge creation to determine the type of service.
    """

    def __init__(self, ServiceSupplier=None, ServiceLocations=None, ServiceCategory=None, ServiceDeliveryPoints=None, DemandResponseProgram=None, MeterReadings=None, AuxiliaryAgreements=None, Equipments=None, EndDeviceControls=None, CustomerAccount=None, Customer=None, StandardIndustryCode=None, PricingStructures=None, **kw_args):
        """Initializes a new 'CustomerAgreement' instance.

        @param ServiceSupplier: Service supplier for this customer agreement.
        @param ServiceLocations: All service locations regulated by this customer agreement.
        @param ServiceCategory:
        @param ServiceDeliveryPoints: All service delivery points regulated by this customer agreement.
        @param DemandResponseProgram: Demand response program for this customer agreement.
        @param MeterReadings: (could be deprecated in the future) All meter readings for this customer agreement.
        @param AuxiliaryAgreements: All (non-service related) auxiliary agreements that refer to this customer agreement.
        @param Equipments:
        @param EndDeviceControls: Could be deprecated in the future.
        @param CustomerAccount: Customer account owning this agreement.
        @param Customer: Customer for this agreement.
        @param StandardIndustryCode:
        @param PricingStructures: All pricing structures applicable to this customer agreement.
        """
        self._ServiceSupplier = None
        self.ServiceSupplier = ServiceSupplier

        self._ServiceLocations = []
        self.ServiceLocations = [] if ServiceLocations is None else ServiceLocations

        self._ServiceCategory = None
        self.ServiceCategory = ServiceCategory

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        self._DemandResponseProgram = None
        self.DemandResponseProgram = DemandResponseProgram

        self._MeterReadings = []
        self.MeterReadings = [] if MeterReadings is None else MeterReadings

        self._AuxiliaryAgreements = []
        self.AuxiliaryAgreements = [] if AuxiliaryAgreements is None else AuxiliaryAgreements

        self._Equipments = []
        self.Equipments = [] if Equipments is None else Equipments

        self._EndDeviceControls = []
        self.EndDeviceControls = [] if EndDeviceControls is None else EndDeviceControls

        self._CustomerAccount = None
        self.CustomerAccount = CustomerAccount

        self._Customer = None
        self.Customer = Customer

        self._StandardIndustryCode = None
        self.StandardIndustryCode = StandardIndustryCode

        self._PricingStructures = []
        self.PricingStructures = [] if PricingStructures is None else PricingStructures

        super(CustomerAgreement, self).__init__(**kw_args)

    def getServiceSupplier(self):
        """Service supplier for this customer agreement.
        """
        return self._ServiceSupplier

    def setServiceSupplier(self, value):
        if self._ServiceSupplier is not None:
            filtered = [x for x in self.ServiceSupplier.CustomerAgreements if x != self]
            self._ServiceSupplier._CustomerAgreements = filtered

        self._ServiceSupplier = value
        if self._ServiceSupplier is not None:
            self._ServiceSupplier._CustomerAgreements.append(self)

    ServiceSupplier = property(getServiceSupplier, setServiceSupplier)

    def getServiceLocations(self):
        """All service locations regulated by this customer agreement.
        """
        return self._ServiceLocations

    def setServiceLocations(self, value):
        for p in self._ServiceLocations:
            filtered = [q for q in p.CustomerAgreements if q != self]
            self._ServiceLocations._CustomerAgreements = filtered
        for r in value:
            if self not in r._CustomerAgreements:
                r._CustomerAgreements.append(self)
        self._ServiceLocations = value

    ServiceLocations = property(getServiceLocations, setServiceLocations)

    def addServiceLocations(self, *ServiceLocations):
        for obj in ServiceLocations:
            if self not in obj._CustomerAgreements:
                obj._CustomerAgreements.append(self)
            self._ServiceLocations.append(obj)

    def removeServiceLocations(self, *ServiceLocations):
        for obj in ServiceLocations:
            if self in obj._CustomerAgreements:
                obj._CustomerAgreements.remove(self)
            self._ServiceLocations.remove(obj)

    def getServiceCategory(self):
        
        return self._ServiceCategory

    def setServiceCategory(self, value):
        if self._ServiceCategory is not None:
            filtered = [x for x in self.ServiceCategory.CustomerAgreements if x != self]
            self._ServiceCategory._CustomerAgreements = filtered

        self._ServiceCategory = value
        if self._ServiceCategory is not None:
            self._ServiceCategory._CustomerAgreements.append(self)

    ServiceCategory = property(getServiceCategory, setServiceCategory)

    def getServiceDeliveryPoints(self):
        """All service delivery points regulated by this customer agreement.
        """
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for x in self._ServiceDeliveryPoints:
            x._CustomerAgreement = None
        for y in value:
            y._CustomerAgreement = self
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj._CustomerAgreement = self
            self._ServiceDeliveryPoints.append(obj)

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj._CustomerAgreement = None
            self._ServiceDeliveryPoints.remove(obj)

    def getDemandResponseProgram(self):
        """Demand response program for this customer agreement.
        """
        return self._DemandResponseProgram

    def setDemandResponseProgram(self, value):
        if self._DemandResponseProgram is not None:
            filtered = [x for x in self.DemandResponseProgram.CustomerAgreements if x != self]
            self._DemandResponseProgram._CustomerAgreements = filtered

        self._DemandResponseProgram = value
        if self._DemandResponseProgram is not None:
            self._DemandResponseProgram._CustomerAgreements.append(self)

    DemandResponseProgram = property(getDemandResponseProgram, setDemandResponseProgram)

    def getMeterReadings(self):
        """(could be deprecated in the future) All meter readings for this customer agreement.
        """
        return self._MeterReadings

    def setMeterReadings(self, value):
        for x in self._MeterReadings:
            x._CustomerAgreement = None
        for y in value:
            y._CustomerAgreement = self
        self._MeterReadings = value

    MeterReadings = property(getMeterReadings, setMeterReadings)

    def addMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            obj._CustomerAgreement = self
            self._MeterReadings.append(obj)

    def removeMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            obj._CustomerAgreement = None
            self._MeterReadings.remove(obj)

    def getAuxiliaryAgreements(self):
        """All (non-service related) auxiliary agreements that refer to this customer agreement.
        """
        return self._AuxiliaryAgreements

    def setAuxiliaryAgreements(self, value):
        for x in self._AuxiliaryAgreements:
            x._CustomerAgreement = None
        for y in value:
            y._CustomerAgreement = self
        self._AuxiliaryAgreements = value

    AuxiliaryAgreements = property(getAuxiliaryAgreements, setAuxiliaryAgreements)

    def addAuxiliaryAgreements(self, *AuxiliaryAgreements):
        for obj in AuxiliaryAgreements:
            obj._CustomerAgreement = self
            self._AuxiliaryAgreements.append(obj)

    def removeAuxiliaryAgreements(self, *AuxiliaryAgreements):
        for obj in AuxiliaryAgreements:
            obj._CustomerAgreement = None
            self._AuxiliaryAgreements.remove(obj)

    def getEquipments(self):
        
        return self._Equipments

    def setEquipments(self, value):
        for p in self._Equipments:
            filtered = [q for q in p.CustomerAgreements if q != self]
            self._Equipments._CustomerAgreements = filtered
        for r in value:
            if self not in r._CustomerAgreements:
                r._CustomerAgreements.append(self)
        self._Equipments = value

    Equipments = property(getEquipments, setEquipments)

    def addEquipments(self, *Equipments):
        for obj in Equipments:
            if self not in obj._CustomerAgreements:
                obj._CustomerAgreements.append(self)
            self._Equipments.append(obj)

    def removeEquipments(self, *Equipments):
        for obj in Equipments:
            if self in obj._CustomerAgreements:
                obj._CustomerAgreements.remove(self)
            self._Equipments.remove(obj)

    def getEndDeviceControls(self):
        """Could be deprecated in the future.
        """
        return self._EndDeviceControls

    def setEndDeviceControls(self, value):
        for x in self._EndDeviceControls:
            x._CustomerAgreement = None
        for y in value:
            y._CustomerAgreement = self
        self._EndDeviceControls = value

    EndDeviceControls = property(getEndDeviceControls, setEndDeviceControls)

    def addEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj._CustomerAgreement = self
            self._EndDeviceControls.append(obj)

    def removeEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj._CustomerAgreement = None
            self._EndDeviceControls.remove(obj)

    def getCustomerAccount(self):
        """Customer account owning this agreement.
        """
        return self._CustomerAccount

    def setCustomerAccount(self, value):
        if self._CustomerAccount is not None:
            filtered = [x for x in self.CustomerAccount.CustomerAgreements if x != self]
            self._CustomerAccount._CustomerAgreements = filtered

        self._CustomerAccount = value
        if self._CustomerAccount is not None:
            self._CustomerAccount._CustomerAgreements.append(self)

    CustomerAccount = property(getCustomerAccount, setCustomerAccount)

    def getCustomer(self):
        """Customer for this agreement.
        """
        return self._Customer

    def setCustomer(self, value):
        if self._Customer is not None:
            filtered = [x for x in self.Customer.CustomerAgreements if x != self]
            self._Customer._CustomerAgreements = filtered

        self._Customer = value
        if self._Customer is not None:
            self._Customer._CustomerAgreements.append(self)

    Customer = property(getCustomer, setCustomer)

    def getStandardIndustryCode(self):
        
        return self._StandardIndustryCode

    def setStandardIndustryCode(self, value):
        if self._StandardIndustryCode is not None:
            filtered = [x for x in self.StandardIndustryCode.CustomerAgreements if x != self]
            self._StandardIndustryCode._CustomerAgreements = filtered

        self._StandardIndustryCode = value
        if self._StandardIndustryCode is not None:
            self._StandardIndustryCode._CustomerAgreements.append(self)

    StandardIndustryCode = property(getStandardIndustryCode, setStandardIndustryCode)

    def getPricingStructures(self):
        """All pricing structures applicable to this customer agreement.
        """
        return self._PricingStructures

    def setPricingStructures(self, value):
        for p in self._PricingStructures:
            filtered = [q for q in p.CustomerAgreements if q != self]
            self._PricingStructures._CustomerAgreements = filtered
        for r in value:
            if self not in r._CustomerAgreements:
                r._CustomerAgreements.append(self)
        self._PricingStructures = value

    PricingStructures = property(getPricingStructures, setPricingStructures)

    def addPricingStructures(self, *PricingStructures):
        for obj in PricingStructures:
            if self not in obj._CustomerAgreements:
                obj._CustomerAgreements.append(self)
            self._PricingStructures.append(obj)

    def removePricingStructures(self, *PricingStructures):
        for obj in PricingStructures:
            if self in obj._CustomerAgreements:
                obj._CustomerAgreements.remove(self)
            self._PricingStructures.remove(obj)

