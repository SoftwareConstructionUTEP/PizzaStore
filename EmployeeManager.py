#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.31.1.5860.78bb27cc6 modeling language!

from Employee import Employee
# line 29 "model.ump"
# line 152 "model.ump"
class EmployeeManager(object):

    #------------------------
    # MEMBER VARIABLES
    #------------------------

    #EmployeeManager Associations

    #------------------------
    # CONSTRUCTOR
    #------------------------

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.__employees = None

        self.__employees = []

    #------------------------
    # INTERFACE
    #------------------------
    # Code from template association_GetMany 
    def getEmployee(self, index):
        aEmployee = self.__employees[index]
        return aEmployee

    def nominalize(self, strList):
        # Key: value
        # string(i.e "127.0.0.1") : int (1)
        knownVals = {}

        intList = []
        i = 0
        for str in strList:
            if str in knownVals.keys():
                intList.append(knownVals[str])
            else:
                knownVals[str] = i
                intList.append(i)
                i = i + 1
        return knownVals


    def getEmployees(self):

        # newEmployees = Collections.unmodifiableList(self.__employees)
        newEmployees = self.nominalize(self.__employees)
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
    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfEmployees():
        return 0
    # Code from template association_AddManyToOne 
    def addEmployee(self, aName, aSalary, aStore):
        return Employee(aName, aSalary, aStore, self)

    def addEmployee(self, aEmployee):
        wasAdded = False
        if aEmployee in self.__employees:
            return False
        existingEmployeeManager = aEmployee.getEmployeeManager()
        isNewEmployeeManager = existingEmployeeManager is not None and not self is existingEmployeeManager
        if isNewEmployeeManager:
            aEmployee.setEmployeeManager(self)
        else:
            self.__employees.append(aEmployee)
        wasAdded = True
        return wasAdded

    def removeEmployee(self, aEmployee):
        wasRemoved = False
        #Unable to remove aEmployee, as it must always have a employeeManager
        if not self is aEmployee.getEmployeeManager():
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

    def delete(self):
        for i in range(len(self.__employees), 0, -1):
            aEmployee = self.__employees[i - 1]
            aEmployee.delete()

    # line 33 "model.ump"
    def __trackSalaries(self):

        pass

    # line 36 "model.ump"
    def __manageTimeSchedule(self):

        pass

    # line 39 "model.ump"
    def __trackHoursWorked(self):

        pass
