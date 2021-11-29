#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.31.1.5860.78bb27cc6 modeling language!

from Employee import Employee

# line 74 "model.ump"
# line 177 "model.ump"
class Manager(Employee):

    #------------------------
    # MEMBER VARIABLES
    #------------------------

    #------------------------
    # CONSTRUCTOR
    #------------------------

    def __init__(self, aName, aSalary, aStore, aEmployeeManager):
        super().__init__(aName, aSalary, aStore, aEmployeeManager)

    #------------------------
    # INTERFACE
    #------------------------

    def delete(self):
        super().delete()

    # line 80 "model.ump"
    def __includeMenuItems(self):

        pass

    # line 83 "model.ump"
    def __excludeMenuItems(self):

        pass
