class Account:
    def __init__(self,accountname, accountnumber):
            self.accountname=accountname
            self.accountnumber=accountnumber
            self.balance=0
            self.deposits=[]
            self.withdrawals =[]
    def deposit(self,Amount):
        if Amount<=0:
            return f"Deposit must be positive amount"
        else:
            self.balance+=Amount
            self.deposits.append(Amount)

        return f"Hello {self.accountname} you have deposited{Amount} and your account balance is{self.balance} and have successful deposit {self.deposits}"
    def withdraw(self,Amount):
        self.transaction=100

        if Amount<=0:
           return f"withdrawal should be greater that zero"
        elif Amount>self.balance:
           

           return f"your balance is {self.balance},you can't withdraw{Amount}"
        else:
           self.balance-=Amount+self.transaction 
           self.withdrawals.append(Amount)

           return f"Hello {self.accountname} you have withdrawal  {Amount} your new balance is {self.balance} and you have successful withdrawal {self.withdrawals}" 
    def deposits_statement(self):
        for x in self.deposits: 
            print(x,end="\n")
    def withdrawals_statement (self):
        for y in self.withdrawals:
            print(y,end="\n")  
    def balance():
        return self.balance              
        



         


    



    