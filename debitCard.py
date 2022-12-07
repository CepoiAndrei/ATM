class DebitCard:
    def __init__(self, number, pin, expirationDate, cvv):
        self.__number = number
        self.__pin = pin
        self.__expirationDate = expirationDate
        self.__cvv = cvv

    def getNumber(self):
        return self.__number

    def getPin(self):
        return self.__pin