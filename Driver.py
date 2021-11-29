#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.31.1.5860.78bb27cc6 modeling language!

from Employee import Employee

# line 86 "model.ump"
# line 182 "model.ump"
class Driver(Employee):

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

    # line 92 "model.ump"
    def __deliverOrder(self):

        pass
