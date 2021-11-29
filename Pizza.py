#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.31.1.5860.78bb27cc6 modeling language!



# line 122 "model.ump"
# line 202 "model.ump"
class Pizza(object):

    #------------------------
    # MEMBER VARIABLES
    #------------------------

    #Pizza Attributes

    #Pizza Associations

    #------------------------
    # CONSTRUCTOR
    #------------------------

    def __init__(self, aPepperoni, aCheese, aTomatoe, aPineapple, aMushrooms, aOrder):
        #instance fields found by Java to Python Converter:
        self.__pepperoni = None
        self.__cheese = None
        self.__tomatoe = None
        self.__pineapple = None
        self.__mushrooms = None
        self.__order = None

        self.__pepperoni = aPepperoni
        self.__cheese = aCheese
        self.__tomatoe = aTomatoe
        self.__pineapple = aPineapple
        self.__mushrooms = aMushrooms
        didAddOrder = self.setOrder(aOrder)
        # if not didAddOrder:
        #     raise RuntimeException("Unable to create pizza due to order. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

    #------------------------
    # INTERFACE
    #------------------------

    def setPepperoni(self, aPepperoni):
        wasSet = False
        self.__pepperoni = aPepperoni
        wasSet = True
        return wasSet

    def setCheese(self, aCheese):
        wasSet = False
        self.__cheese = aCheese
        wasSet = True
        return wasSet

    def setTomatoe(self, aTomatoe):
        wasSet = False
        self.__tomatoe = aTomatoe
        wasSet = True
        return wasSet

    def setPineapple(self, aPineapple):
        wasSet = False
        self.__pineapple = aPineapple
        wasSet = True
        return wasSet

    def setMushrooms(self, aMushrooms):
        wasSet = False
        self.__mushrooms = aMushrooms
        wasSet = True
        return wasSet

    def getPepperoni(self):
        return self.__pepperoni

    def getCheese(self):
        return self.__cheese

    def getTomatoe(self):
        return self.__tomatoe

    def getPineapple(self):
        return self.__pineapple

    def getMushrooms(self):
        return self.__mushrooms
    # Code from template association_GetOne 
    def getOrder(self):
        return self.__order
    # Code from template association_SetOneToMany 
    def setOrder(self, aOrder):
        wasSet = False
        if aOrder is None:
            return wasSet

        existingOrder = self.__order
        self.__order = aOrder
        if existingOrder is not None and not existingOrder is aOrder:
            existingOrder.removePizza(self)
        self.__order.addPizza(self)
        wasSet = True
        return wasSet

    def delete(self):
        placeholderOrder = self.__order
        self.__order = None
        if placeholderOrder is not None:
            placeholderOrder.removePizza(self)

    # line 132 "model.ump"
    def __addIngredients(self):

        pass


    # def toString(self):
    #     return super().toString() + "["+ "pepperoni" + ":" + self.getPepperoni()+ "," + "cheese" + ":" + self.getCheese()+ "," + "tomatoe" + ":" + self.getTomatoe()+ "," + "pineapple" + ":" + self.getPineapple()+ "," + "mushrooms" + ":" + self.getMushrooms()+ "]" + System.getProperties().getProperty("line.separator") + "  " + "order = "+(Integer.toHexString(System.identityHashCode(self.getOrder())) if self.getOrder() is not None ) else "null")