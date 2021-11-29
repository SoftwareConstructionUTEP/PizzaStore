#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.31.1.5860.78bb27cc6 modeling language!


# line 66 "model.ump"
# line 169 "model.ump"
class Order(object):

    #------------------------
    # MEMBER VARIABLES
    #------------------------

    #Order Attributes

    #Order Associations

    #------------------------
    # CONSTRUCTOR
    #------------------------

    def __init__(self, aDelivery, aStore, aOrderManager):
        #instance fields found by Java to Python Converter:
        self.__delivery = None
        self.__store = None
        self.__orderManager = None
        self.__pizzas = None

        self.__delivery = aDelivery
        didAddStore = self.setStore(aStore)
        if not didAddStore:
            raise RuntimeException("Unable to create order due to store. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        didAddOrderManager = self.setOrderManager(aOrderManager)
        if not didAddOrderManager:
            raise RuntimeException("Unable to create order due to orderManager. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        self.__pizzas = []

    #------------------------
    # INTERFACE
    #------------------------

    def setDelivery(self, aDelivery):
        wasSet = False
        self.__delivery = aDelivery
        wasSet = True
        return wasSet

    def getDelivery(self):
        return self.__delivery
    # Code from template association_GetOne 
    def getStore(self):
        return self.__store
    # Code from template association_GetOne 
    def getOrderManager(self):
        return self.__orderManager
    # Code from template association_GetMany 
    def getPizza(self, index):
        aPizza = self.__pizzas[index]
        return aPizza

    def getPizzas(self):
        newPizzas = Collections.unmodifiableList(self.__pizzas)
        return newPizzas

    def numberOfPizzas(self):
        number = len(self.__pizzas)
        return number

    def hasPizzas(self):
        has = len(self.__pizzas) > 0
        return has

    def indexOfPizza(self, aPizza):
        index = (self.__pizzas.index(aPizza) if aPizza in self.__pizzas else -1)
        return index
    # Code from template association_SetOneToMany 
    def setStore(self, aStore):
        wasSet = False
        if aStore is None:
            return wasSet

        existingStore = self.__store
        self.__store = aStore
        if existingStore is not None and not existingStore is aStore:
            existingStore.removeOrder(self)
        self.__store.addOrder(self)
        wasSet = True
        return wasSet
    # Code from template association_SetOneToMany 
    def setOrderManager(self, aOrderManager):
        wasSet = False
        if aOrderManager is None:
            return wasSet

        existingOrderManager = self.__orderManager
        self.__orderManager = aOrderManager
        if existingOrderManager is not None and not existingOrderManager is aOrderManager:
            existingOrderManager.removeOrder(self)
        self.__orderManager.addOrder(self)
        wasSet = True
        return wasSet
    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfPizzas():
        return 0
    # Code from template association_AddManyToOne 
    def addPizza(self, aPepperoni, aCheese, aTomatoe, aPineapple, aMushrooms):
        return Pizza(aPepperoni, aCheese, aTomatoe, aPineapple, aMushrooms, self)

    def addPizza(self, aPizza):
        wasAdded = False
        if aPizza in self.__pizzas:
            return False
        existingOrder = aPizza.getOrder()
        isNewOrder = existingOrder is not None and not self is existingOrder
        if isNewOrder:
            aPizza.setOrder(self)
        else:
            self.__pizzas.append(aPizza)
        wasAdded = True
        return wasAdded

    def removePizza(self, aPizza):
        wasRemoved = False
        #Unable to remove aPizza, as it must always have a order
        if not self is aPizza.getOrder():
            self.__pizzas.remove(aPizza)
            wasRemoved = True
        return wasRemoved
    # Code from template association_AddIndexControlFunctions 
    def addPizzaAt(self, aPizza, index):
        wasAdded = False
        if self.addPizza(aPizza):
            if index < 0:
                index = 0
            if index > self.numberOfPizzas():
                index = self.numberOfPizzas() - 1
            self.__pizzas.remove(aPizza)
            self.__pizzas.insert(index, aPizza)
            wasAdded = True
        return wasAdded

    def addOrMovePizzaAt(self, aPizza, index):
        wasAdded = False
        if aPizza in self.__pizzas:
            if index < 0:
                index = 0
            if index > self.numberOfPizzas():
                index = self.numberOfPizzas() - 1
            self.__pizzas.remove(aPizza)
            self.__pizzas.insert(index, aPizza)
            wasAdded = True
        else:
            wasAdded = self.addPizzaAt(aPizza, index)
        return wasAdded

    def delete(self):
        placeholderStore = self.__store
        self.__store = None
        if placeholderStore is not None:
            placeholderStore.removeOrder(self)
        placeholderOrderManager = self.__orderManager
        self.__orderManager = None
        if placeholderOrderManager is not None:
            placeholderOrderManager.removeOrder(self)
        for i in range(len(self.__pizzas), 0, -1):
            aPizza = self.__pizzas[i - 1]
            aPizza.delete()


    # def toString(self):
    #     return super().toString() + "["+ "delivery" + ":" + self.getDelivery()+ "]" + System.getProperties().getProperty("line.separator") + "  " + "store = "+(Integer.toHexString(System.identityHashCode(self.getStore())) if self.getStore() is not None ) else "null") + System.getProperties().getProperty("line.separator") + "  " + "orderManager = "+(Integer.toHexString(System.identityHashCode(self.getOrderManager())) if self.getOrderManager() is not None ) else "null")