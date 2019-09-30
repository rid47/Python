class Bankaccount():
    def __init__(self,account_name = "Current Account", balance = 200):
#__ (double underscore) hides the variable outside the class
        self.__account_name = account_name
        self.__balance = balance
    def balanceGetter(self):
        print(self.__balance)
        self.__hidden() # private method accessible within the class
    def balanceSetter_withdraw(self,value):
        if value <= self.__balance:
            self.__balance = self.__balance -value
            print(f"New balace: {self.__balance}")
        else:
            print("You do not have enough funds!")
    def __hidden(self):
        print("I'm hidden outside this class")

# Creating an object of Bankaccount class
accountObject = Bankaccount("Mizan",500)

# Trying to access hidden attribute; which returns
#Bankaccount' object has no attribute '__balance'
#Bankaccount' object has no attribute '__hidden

#print(accountObject.__balance)
# accountObject.__hidden()

# This works! but why? __balance is supposed to be hidden
accountObject.__balance = 2000000000
# Well When you write to an attribute of an object, that does not exist,
# the python system will normally not complain,
# but just create a new attribute. So here a new attribute to the object
#accountObject created...
print(accountObject.__balance)

# When you chek the balanceGetter you'll find out the private __balance
# hasn't changed at all
accountObject.balanceGetter()

# while True:
#     print("1. Check account Balance")
#     print("2. Withdraw funds")
#     menu_option = int(input())
#     if menu_option == 1:
#         accountObject.balanceGetter()
#     elif menu_option ==2:
#         value = int(input("How much would you like to withdraw?"))
#         accountObject.balanceSetter_withdraw(value)
#     else:
#         print("Wrond menu choice!")
