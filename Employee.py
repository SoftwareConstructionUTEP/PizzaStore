#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.31.1.5860.78bb27cc6 modeling language!


employees = [[]]
# line 21 "model.ump"
# line 145 "model.ump"
class Employee(object):

    #------------------------
    # MEMBER VARIABLES
    #------------------------

    #Employee Attributes

    #Employee Associations

    #------------------------
    # CONSTRUCTOR
    #------------------------

    def __init__(self, aName, aSalary, aStore, aEmployeeManager):
        #instance fields found by Java to Python Converter:
        self.__name = None
        self.__salary = 0
        self.__store = None
        self.__employeeManager = None

        self.__name = aName
        self.__salary = aSalary
        didAddStore = self.setStore(aStore)
        # if not didAddStore:
        #     raise RuntimeException("Unable to create employee due to store. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        # didAddEmployeeManager = self.setEmployeeManager(aEmployeeManager)
        # if not didAddEmployeeManager:
        #     raise RuntimeException("Unable to create employee due to employeeManager. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

    #------------------------
    # INTERFACE
    #------------------------
    def addEmployee(self):

    def setName(self, aName):
        wasSet = False
        self.__name = aName
        wasSet = True
        return wasSet

    def setSalary(self, aSalary):
        wasSet = False
        self.__salary = aSalary
        wasSet = True
        return wasSet

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary
    # Code from template association_GetOne 
    def getStore(self):
        return self.__store
    # Code from template association_GetOne 
    def getEmployeeManager(self):
        return self.__employeeManager
    # Code from template association_SetOneToMany 
    def setStore(self, aStore):
        wasSet = False
        if aStore is None:
            return wasSet

        existingStore = self.__store
        self.__store = aStore
        if existingStore is not None and not existingStore is aStore:
            existingStore.removeEmployee(self)
        self.__store.addEmployee(self)
        wasSet = True
        return wasSet
    # Code from template association_SetOneToMany 
    def setEmployeeManager(self, aEmployeeManager):
        wasSet = False
        if aEmployeeManager is None:
            return wasSet

        existingEmployeeManager = self.__employeeManager
        self.__employeeManager = aEmployeeManager
        if existingEmployeeManager is not None and not existingEmployeeManager is aEmployeeManager:
            existingEmployeeManager.removeEmployee(self)
        self.__employeeManager.addEmployee(self)
        wasSet = True
        return wasSet

    def delete(self):
        placeholderStore = self.__store
        self.__store = None
        if placeholderStore is not None:
            placeholderStore.removeEmployee(self)
        placeholderEmployeeManager = self.__employeeManager
        self.__employeeManager = None
        if placeholderEmployeeManager is not None:
            placeholderEmployeeManager.removeEmployee(self)


    # def toString(self):
    #     return super().toString() + "["+ "name" + ":" + self.getName()+ "," + "salary" + ":" + self.getSalary()+ "]" + System.getProperties().getProperty("line.separator") + "  " + "store = "+(Integer.toHexString(System.identityHashCode(self.getStore())) if self.getStore() is not None ) else "null") + System.getProperties().getProperty("line.separator") + "  " + "employeeManager = "+(Integer.toHexString(System.identityHashCode(self.getEmployeeManager())) if self.getEmployeeManager() is not None ) else "null")