class Account:
    def __init__(self,accountname, accountnumber,balance,Amount):
            self.accountname=accountname
            self.accountnumber=accountnumber
            self.balance=balance
            self.Amount=Amount
    def deposit(self,Amount):
        self.balance+=Amount
        return f"Hello your account balance is{self.deposit}"
    def withdrawal(self,Amount):
        self.balance-=Amount
        return f"Hello  your account balance is {self.last_name}" 
    