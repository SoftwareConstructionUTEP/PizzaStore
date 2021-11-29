#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.31.1.5860.78bb27cc6 modeling language!


from Employee import Employee
# line 103 "model.ump"
# line 192 "model.ump"
class Maintenance(Employee):

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

    # line 107 "model.ump"
    def __cleanStore(self):

        pass
