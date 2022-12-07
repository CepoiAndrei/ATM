class Person:
    def __init__(self, firstName, lastName, personalIdNumber):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__personalIdNumber = personalIdNumber

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName