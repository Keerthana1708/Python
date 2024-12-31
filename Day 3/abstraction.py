from abc import ABC, abstractmethod
class Accounts:
    def savings(self):
        print("Zero balance")
class Loans(ABC, Accounts):
    @abstractmethod
    def pl(self):
        print("Personal Loan")
'''class Final(Loans,Accounts):
    def pl(self):
        print("Personal Loan")'''

obj1 = Loans()
obj1.savings()
obj1.pl()