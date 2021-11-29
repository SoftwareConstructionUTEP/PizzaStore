#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.31.1.5860.78bb27cc6 modeling language!

import OrderManager

# line 57 "model.ump"
# line 163 "model.ump"
class FeedbackManager(object):

    def _initialize_instance_fields(self):
        #instance fields found by Java to Python Converter:
        self.__feedback = None
        self.__orderManager = None


    #------------------------
    # MEMBER VARIABLES
    #------------------------

    #FeedbackManager Attributes

    #FeedbackManager Associations

    #------------------------
    # CONSTRUCTOR
    #------------------------

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public FeedbackManager(String aFeedback, OrderManager aOrderManager)
    def __init__(self, aFeedback, aOrderManager):
        self._initialize_instance_fields()

        self.__feedback = aFeedback
        if aOrderManager is None or aOrderManager.getFeedbackManager() is not None:
            raise RuntimeException("Unable to create FeedbackManager due to aOrderManager. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        self.__orderManager = aOrderManager

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public FeedbackManager(String aFeedback)
    def __init__(self, aFeedback):
        self._initialize_instance_fields()

        self.__feedback = aFeedback
        self.__orderManager = OrderManager(self)

    #------------------------
    # INTERFACE
    #------------------------

    def setFeedback(self, aFeedback):
        wasSet = False
        self.__feedback = aFeedback
        wasSet = True
        return wasSet

    def getFeedback(self):
        return self.__feedback
    # Code from template association_GetOne 
    def getOrderManager(self):
        return self.__orderManager

    def delete(self):
        existingOrderManager = self.__orderManager
        self.__orderManager = None
        if existingOrderManager is not None:
            existingOrderManager.delete()

    # line 62 "model.ump"
    def __storeFeedback(self):

        pass


    # def toString(self):
    #     return super().toString() + "["+ "feedback" + ":" + self.getFeedback()+ "]" + System.getProperties().getProperty("line.separator") + "  " + "orderManager = "+(Integer.toHexString(System.identityHashCode(self.getOrderManager())) if self.getOrderManager() is not None ) else "null")