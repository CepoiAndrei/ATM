class BankAccount:
    def __init__(self, owner, iban, balance, currency, associatedCard):
        self.__owner = owner
        self.__iban = iban
        self.__balance = balance
        self.__currency = currency
        self.__associatedCard = associatedCard

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def getCurrency(self):
        return self.__currency

    def getIban(self):
        return self.__iban

    def getOwner(self):
        return self.__owner