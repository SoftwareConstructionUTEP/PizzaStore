#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.31.1.5860.78bb27cc6 modeling language!

import FeedbackManager
import Order
from collections import OrderedDict
# line 43 "model.ump"
# line 157 "model.ump"
class OrderManager(object):

    def _initialize_instance_fields(self):
        #instance fields found by Java to Python Converter:
        self.__stores = None
        self.__feedbackManager = None
        self.__orders = None


    #------------------------
    # MEMBER VARIABLES
    #------------------------

    #OrderManager Associations

    #------------------------
    # CONSTRUCTOR
    #------------------------

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public OrderManager(FeedbackManager aFeedbackManager)
    def __init__(self, aFeedbackManager):
        self._initialize_instance_fields()

        self.__stores = []
        # if aFeedbackManager is None or aFeedbackManager.getOrderManager() is not None:
        #     raise RuntimeException("Unable to create OrderManager due to aFeedbackManager. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        self.__feedbackManager = aFeedbackManager
        self.__orders = []

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public OrderManager(String aFeedbackForFeedbackManager)
    def __init__(self, aFeedbackForFeedbackManager):
        self._initialize_instance_fields()

        self.__stores = []
        self.__feedbackManager = FeedbackManager(aFeedbackForFeedbackManager, self)
        self.__orders = []

    #------------------------
    # INTERFACE
    #------------------------
    # Code from template association_GetMany 
    def getStore(self, index):
        aStore = self.__stores[index]
        return aStore

    def getStores(self):
        newStores = self.__stores
        return newStores

    def numberOfStores(self):
        number = len(self.__stores)
        return number

    def hasStores(self):
        has = len(self.__stores) > 0
        return has

    def indexOfStore(self, aStore):
        index = (self.__stores.index(aStore) if aStore in self.__stores else -1)
        return index
    # Code from template association_GetOne 
    def getFeedbackManager(self):
        return self.__feedbackManager
    # Code from template association_GetMany 
    def getOrder(self, index):
        aOrder = self.__orders[index]
        return aOrder

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

    def getOrders(self):

        newOrders = self.nominalize(self.__orders)
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
    def minimumNumberOfStores():
        return 0
    # Code from template association_AddManyToOne 
    def addStore(self, aCity, aZipCode, aDeliveryHours, aDeliveryRules):
        return Store(aCity, aZipCode, aDeliveryHours, aDeliveryRules, self)

    def addStore(self, aStore):
        wasAdded = False
        if aStore in self.__stores:
            return False
        existingOrderManager = aStore.getOrderManager()
        isNewOrderManager = existingOrderManager is not None and not self is existingOrderManager
        if isNewOrderManager:
            aStore.setOrderManager(self)
        else:
            self.__stores.append(aStore)
        wasAdded = True
        return wasAdded

    def removeStore(self, aStore):
        wasRemoved = False
        #Unable to remove aStore, as it must always have a orderManager
        if not self is aStore.getOrderManager():
            self.__stores.remove(aStore)
            wasRemoved = True
        return wasRemoved
    # Code from template association_AddIndexControlFunctions 
    def addStoreAt(self, aStore, index):
        wasAdded = False
        if self.addStore(aStore):
            if index < 0:
                index = 0
            if index > self.numberOfStores():
                index = self.numberOfStores() - 1
            self.__stores.remove(aStore)
            self.__stores.insert(index, aStore)
            wasAdded = True
        return wasAdded

    def addOrMoveStoreAt(self, aStore, index):
        wasAdded = False
        if aStore in self.__stores:
            if index < 0:
                index = 0
            if index > self.numberOfStores():
                index = self.numberOfStores() - 1
            self.__stores.remove(aStore)
            self.__stores.insert(index, aStore)
            wasAdded = True
        else:
            wasAdded = self.addStoreAt(aStore, index)
        return wasAdded
    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfOrders():
        return 0
    # Code from template association_AddManyToOne 
    def addOrder(self, aDelivery, aStore):
        return Order(aDelivery, aStore, self)

    def addOrder(self, aOrder):
        wasAdded = False
        if aOrder in self.__orders:
            return False
        existingOrderManager = aOrder.getOrderManager()
        isNewOrderManager = existingOrderManager is not None and not self is existingOrderManager
        if isNewOrderManager:
            aOrder.setOrderManager(self)
        else:
            self.__orders.append(aOrder)
        wasAdded = True
        return wasAdded

    def removeOrder(self, aOrder):
        wasRemoved = False
        #Unable to remove aOrder, as it must always have a orderManager
        if not self is aOrder.getOrderManager():
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
        for i in range(len(self.__stores), 0, -1):
            aStore = self.__stores[i - 1]
            aStore.delete()
        existingFeedbackManager = self.__feedbackManager
        self.__feedbackManager = None
        if existingFeedbackManager is not None:
            existingFeedbackManager.delete()
        for i in range(len(self.__orders), 0, -1):
            aOrder = self.__orders[i - 1]
            aOrder.delete()

    # line 47 "model.ump"
    def __sendOrder(self):

        pass

    # line 50 "model.ump"
    def __processOrder(self):

        pass

    # line 53 "model.ump"
    def __askForFeedback(self):

        pass
