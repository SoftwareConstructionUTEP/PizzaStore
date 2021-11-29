#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.31.1.5860.78bb27cc6 modeling language!


# line 2 "model.ump"
# line 140 "model.ump"
class Store(object):

    #------------------------
    # MEMBER VARIABLES
    #------------------------

    #Store Attributes

    #Store Associations

    #------------------------
    # CONSTRUCTOR
    #------------------------

    def __init__(self, aCity, aZipCode, aDeliveryHours, aDeliveryRules, aOrderManager):
        #instance fields found by Java to Python Converter:
        self.__city = None
        self.__zipCode = None
        self.__management = None
        self.__deliveryHours = None
        self.__deliveryRules = None
        self.__employees = None
        self.__orderManager = None
        self.__orders = None
        self.__state = None

        self.__city = aCity
        self.__zipCode = aZipCode
        self.__management = []
        self.__deliveryHours = aDeliveryHours
        self.__deliveryRules = aDeliveryRules
        self.__employees = []
        didAddOrderManager = self.setOrderManager(aOrderManager)
        # if not didAddOrderManager:
        #     raise RuntimeException("Unable to create store due to orderManager. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        self.__orders = []

    #------------------------
    # INTERFACE
    #------------------------

    def setCity(self, aCity):
        wasSet = False
        self.__city = aCity
        wasSet = True
        return wasSet

    def setZipCode(self, aZipCode):
        wasSet = False
        self.__zipCode = aZipCode
        wasSet = True
        return wasSet
    # Code from template attribute_SetMany 
    def addManagement(self, aManagement):
        wasAdded = False
        wasAdded = self.__management.append(aManagement)
        return wasAdded

    def removeManagement(self, aManagement):
        wasRemoved = False
        wasRemoved = self.__management.remove(aManagement)
        return wasRemoved

    def setDeliveryHours(self, aDeliveryHours):
        wasSet = False
        self.__deliveryHours = aDeliveryHours
        wasSet = True
        return wasSet

    def setDeliveryRules(self, aDeliveryRules):
        wasSet = False
        self.__deliveryRules = aDeliveryRules
        wasSet = True
        return wasSet

    def getCity(self):
        return self.__city

    def getZipCode(self):
        return self.__zipCode
    # Code from template attribute_GetMany 
    def getManagement(self, index):
        aManagement = self.__management[index]
        return aManagement

    def getManagement(self):
        newManagement = self.__management.toArray([None for _ in range(len(self.__management))])
        return newManagement

    def numberOfManagement(self):
        number = len(self.__management)
        return number

    def hasManagement(self):
        has = len(self.__management) > 0
        return has

    def indexOfManagement(self, aManagement):
        index = (self.__management.index(aManagement) if aManagement in self.__management else -1)
        return index

    def getDeliveryHours(self):
        return self.__deliveryHours

    def getDeliveryRules(self):
        return self.__deliveryRules
    # Code from template association_GetMany 
    def getEmployee(self, index):
        aEmployee = self.__employees[index]
        return aEmployee

    def getEmployees(self):
        newEmployees = Collections.unmodifiableList(self.__employees)
        return newEmployees

    def numberOfEmployees(self):
        number = len(self.__employees)
        return number

    def hasEmployees(self):
        has = len(self.__employees) > 0
        return has

    def indexOfEmployee(self, aEmployee):
        index = (self.__employees.index(aEmployee) if aEmployee in self.__employees else -1)
        return index
    # Code from template association_GetOne 
    def getOrderManager(self):
        return self.__orderManager
    # Code from template association_GetMany 
    def getOrder(self, index):
        aOrder = self.__orders[index]
        return aOrder

    def getOrders(self):
        newOrders = Collections.unmodifiableList(self.__orders)
        return newOrders

    def numberOfOrders(self):
        number = len(self.__orders)
        return number

    def hasOrders(self):
        has = len(self.__orders) > 0
        return has

    def indexOfOrder(self, aOrder):
        index = (self.__orders.index(aOrder) if aOrder in self.__orders else -1)
        return index
    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfEmployees():
        return 0
    # Code from template association_AddManyToOne 
    def addEmployee(self, aName, aSalary, aEmployeeManager):
        return Employee(aName, aSalary, self, aEmployeeManager)

    def addEmployee(self, aEmployee):
        wasAdded = False
        if aEmployee in self.__employees:
            return False
        existingStore = aEmployee.getStore()
        isNewStore = existingStore is not None and not self is existingStore
        if isNewStore:
            aEmployee.setStore(self)
        else:
            self.__employees.append(aEmployee)
        wasAdded = True
        return wasAdded

    def removeEmployee(self, aEmployee):
        wasRemoved = False
        #Unable to remove aEmployee, as it must always have a store
        if not self is aEmployee.getStore():
            self.__employees.remove(aEmployee)
            wasRemoved = True
        return wasRemoved
    # Code from template association_AddIndexControlFunctions 
    def addEmployeeAt(self, aEmployee, index):
        wasAdded = False
        if self.addEmployee(aEmployee):
            if index < 0:
                index = 0
            if index > self.numberOfEmployees():
                index = self.numberOfEmployees() - 1
            self.__employees.remove(aEmployee)
            self.__employees.insert(index, aEmployee)
            wasAdded = True
        return wasAdded

    def addOrMoveEmployeeAt(self, aEmployee, index):
        wasAdded = False
        if aEmployee in self.__employees:
            if index < 0:
                index = 0
            if index > self.numberOfEmployees():
                index = self.numberOfEmployees() - 1
            self.__employees.remove(aEmployee)
            self.__employees.insert(index, aEmployee)
            wasAdded = True
        else:
            wasAdded = self.addEmployeeAt(aEmployee, index)
        return wasAdded
    # Code from template association_SetOneToMany 
    def setOrderManager(self, aOrderManager):
        wasSet = False
        if aOrderManager is None:
            return wasSet

        existingOrderManager = self.__orderManager
        self.__orderManager = aOrderManager
        if existingOrderManager is not None and not existingOrderManager is aOrderManager:
            existingOrderManager.removeStore(self)
        self.__orderManager.addStore(self)
        wasSet = True
        return wasSet
    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfOrders():
        return 0
    # Code from template association_AddManyToOne 
    def addOrder(self, aDelivery, aOrderManager):
        return Order(aDelivery, self, aOrderManager)

    def addOrder(self, aOrder):
        wasAdded = False
        if aOrder in self.__orders:
            return False
        existingStore = aOrder.getStore()
        isNewStore = existingStore is not None and not self is existingStore
        if isNewStore:
            aOrder.setStore(self)
        else:
            self.__orders.append(aOrder)
        wasAdded = True
        return wasAdded

    def removeOrder(self, aOrder):
        wasRemoved = False
        #Unable to remove aOrder, as it must always have a store
        if not self is aOrder.getStore():
            self.__orders.remove(aOrder)
            wasRemoved = True
        return wasRemoved
    # Code from template association_AddIndexControlFunctions 
    def addOrderAt(self, aOrder, index):
        wasAdded = False
        if self.addOrder(aOrder):
            if index < 0:
                index = 0
            if index > self.numberOfOrders():
                index = self.numberOfOrders() - 1
            self.__orders.remove(aOrder)
            self.__orders.insert(index, aOrder)
            wasAdded = True
        return wasAdded

    def addOrMoveOrderAt(self, aOrder, index):
        wasAdded = False
        if aOrder in self.__orders:
            if index < 0:
                index = 0
            if index > self.numberOfOrders():
                index = self.numberOfOrders() - 1
            self.__orders.remove(aOrder)
            self.__orders.insert(index, aOrder)
            wasAdded = True
        else:
            wasAdded = self.addOrderAt(aOrder, index)
        return wasAdded

    def delete(self):
        for i in range(len(self.__employees), 0, -1):
            aEmployee = self.__employees[i - 1]
            aEmployee.delete()
        placeholderOrderManager = self.__orderManager
        self.__orderManager = None
        if placeholderOrderManager is not None:
            placeholderOrderManager.removeStore(self)
        for i in range(len(self.__orders), 0, -1):
            aOrder = self.__orders[i - 1]
            aOrder.delete()

    # line 12 "model.ump"
    def __manageCost(self):

        pass

    # line 15 "model.ump"
    def __manageRevenue(self):

        pass

    # line 18 "model.ump"
    def __prepareOrder(self):

        pass


    # def toString(self):
    #     return super().toString() + "["+ "city" + ":" + self.getCity()+ "," + "zipCode" + ":" + self.getZipCode()+ "," + "deliveryHours" + ":" + self.getDeliveryHours()+ "," + "deliveryRules" + ":" + self.getDeliveryRules()+ "]" + System.getProperties().getProperty("line.separator") + "  " + "orderManager = "+(Integer.toHexString(System.identityHashCode(self.getOrderManager())) if self.getOrderManager() is not None ) else "null")
    #------------------------
    # DEVELOPER CODE - PROVIDED AS-IS
    #------------------------

    # line 4 "model.ump"

