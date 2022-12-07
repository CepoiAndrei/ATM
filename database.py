import debitCard
import datetime
import person
import bankAccount

class Database:
    def __init__(self):
        self.__debitCardToBankAccountDict = dict()

        debitCard1 = debitCard.DebitCard('1111 1111 1111 1111', 1111,
            datetime.datetime(2026, 1, 1), 111)
        debitCard2 = debitCard.DebitCard('2222 2222 2222 2222', 2222,
            datetime.datetime(2026, 1, 1), 222)
        debitCard3 = debitCard.DebitCard('3333 3333 3333 3333', 3333,
            datetime.datetime(2026, 1, 1), 333)
        debitCard4 = debitCard.DebitCard('4444 4444 4444 4444', 4444,
            datetime.datetime(2026, 1, 1), 444)

        person1 = person.Person('Ion', 'Popescu', '1990101999999')
        person2 = person.Person('George', 'Mihailescu', '1990101888888')
        person3 = person.Person('Tudor', 'Ionescu', '1990101777777')
        person4 = person.Person('Dumitru', 'Florescu', '1990101666666')

        bankAccount1 = bankAccount.BankAccount(person1, 'RO96BTRLRONCRT1111111111',
            100, 'RON', debitCard1);
        bankAccount2 = bankAccount.BankAccount(person2, 'RO96BTRLRONCRT2222222222',
            100, 'RON', debitCard2);
        bankAccount3 = bankAccount.BankAccount(person3, 'RO96BTRLRONCRT3333333333',
            100, 'RON', debitCard3);
        bankAccount4 = bankAccount.BankAccount(person4, 'RO96BTRLRONCRT4444444444',
            100, 'RON', debitCard4);

        self.__debitCardToBankAccountDict[debitCard1] = bankAccount1
        self.__debitCardToBankAccountDict[debitCard2] = bankAccount2
        self.__debitCardToBankAccountDict[debitCard3] = bankAccount3
        self.__debitCardToBankAccountDict[debitCard4] = bankAccount4

    def getDebitCardToBankAccountDict(self):
        return self.__debitCardToBankAccountDict

atmDatabase = Database()