import database

class ATM:
    def __init__(self):
        self.__database = database.atmDatabase
        self.__currentBankAccount = None

    def run(self):
        debitCard = None
        while (not debitCard):
            debitCardNumber = input("Insert your debit card.\n")
            debitCardMatcher = [debitCard for debitCard in self.__database.getDebitCardToBankAccountDict().keys()
                if debitCard.getNumber() == debitCardNumber]
            
            if (len(debitCardMatcher) > 0):
                debitCard = debitCardMatcher[0]
                self.__currentBankAccount = self.__database.getDebitCardToBankAccountDict()[debitCard]
            else:
                print("[error] Invalid debit card.\n")

        validDebitCardPIN = False
        while (not validDebitCardPIN):
            debitCardPIN = int(input("\nInsert your debit card PIN.\n"))
            if (debitCard.getPin() == debitCardPIN):
                ownerFirstName = self.__currentBankAccount.getOwner().getFirstName()
                ownerLastName = self.__currentBankAccount.getOwner().getLastName()
                print("[info] Hello,", ownerFirstName, ownerLastName + "!\n")
                validDebitCardPIN = True
            else:
                print("[error] Invalid debit card PIN.")

        closeSession = False
        while (not closeSession):
            self.printOperations()

            chosenOperation = int(input())
            if (chosenOperation == 1):
                sum = int(input("Enter the sum to be deposited, then insert the bills.\n"))
                self.deposit(sum)
            elif (chosenOperation == 2):
                sum = int(input("Enter the sum to be withdrawn.\n"))
                self.withdraw(sum)
            elif (chosenOperation == 3):
                self.checkBalance()
            elif (chosenOperation == 4):
                sum = int(input("Enter the sum to be transfered.\n"))
                balance = self.__currentBankAccount.getBalance()
                if (sum > balance):
                    print("[error] Insufficient funds.\n")
                    continue
                toIban = input("Enter the IBAN to transfer the funds to.\n")
                self.transfer(sum, toIban)
            elif (chosenOperation == 5):
                print("[info] Session closed.")
                closeSession = True

    def deposit(self, sum):
        self.__currentBankAccount.setBalance(self.__currentBankAccount.getBalance() + sum)
        currency = self.__currentBankAccount.getCurrency()
        print("[info] Successfully deposited " + str(sum) + " " + currency + ".")
        self.checkBalance()

    def withdraw(self, sum):
        self.__currentBankAccount.setBalance(self.__currentBankAccount.getBalance() - sum)
        currency = self.__currentBankAccount.getCurrency()
        print("[info] Successfully withdrawn " + str(sum) + " " + currency + ".")
        self.checkBalance()

    def checkBalance(self):
        balance = self.__currentBankAccount.getBalance()
        currency = self.__currentBankAccount.getCurrency()
        print("[info] Available balance -", str(balance), currency + ".\n")

    def transfer(self, sum, toIban):
        receivingBankAccount = None
        bankAccountMatcher = [bankAccount for bankAccount in self.__database.getDebitCardToBankAccountDict().values()
            if bankAccount.getIban() == toIban]
        if (len(bankAccountMatcher) > 0):
            receivingBankAccount = bankAccountMatcher[0]
            if (self.__currentBankAccount.getCurrency() != receivingBankAccount.getCurrency()):
                print("[error] Receiving bank account currency does not match yours.\n")
        else:
            print("[error] Invalid IBAN.\n")
            return
        
        self.__currentBankAccount.setBalance(self.__currentBankAccount.getBalance() - sum)
        receivingBankAccount.setBalance(receivingBankAccount.getBalance() + sum)
        
        transferedCurrency = self.__currentBankAccount.getCurrency()
        receiverFirstName = receivingBankAccount.getOwner().getFirstName()
        receiverLastName = receivingBankAccount.getOwner().getLastName()
        print("[info] Successfully transfered", str(sum), transferedCurrency, "to", receiverFirstName, receiverLastName + ".")
        self.checkBalance()


    def printOperations(self):
        print("Choose the desired operation.")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Transfer funds")
        print("5. Exit")
        print()