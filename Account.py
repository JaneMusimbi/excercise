from datetime import datetime
class Account:
    def __init__(self,account_name, account_number,phone_number,id):
            self.account_name=account_name
            self.accountnumber=account_number
            self.phone_number=phone_number
            self.id=id
            self.balance=0
            self.deposits=[]
            self.withdrawals =[]
            self.transaction=100
            self.loan_balance=0
    def deposit(self,amount):
        date=datetime.now() 
        self.amount=amount 
        if amount<=0:
                return f"deposit amount must be greater than zero(0)"
        else:
            self.balance+=amount
            dct={"date":date.strftime("%d/%m/%Y"),"amount":amount,"narration":f'thank you for depositing {amount} on {date}'}
            self.deposits.append(dct)

        return f"You have deposited kshs.{amount} and your new balance is {self.balance})"
    def withdraw(self,amount):
        self.transaction=100
        date=datetime.now()
        if amount>self.balance:
           return f"Dear customer,you have insuffient funds in your M-pesa account to make withdraw"

        elif amount<=0:
           return f"Dear customer, you can't withdraw zero amount " 
        else:
            self.balance -=amount
            dct={"date":date.strftime("%d/%m/%Y"),"amount":amount,"narration":f'thank you for withdrawing {amount} on {date}'}
            self.withdrawals.append(dct)
        withdrawal_amount=self.balance-self.transaction
        if amount>withdrawal_amount:
          return "insufficient balance"
        self.balance-=amount+self.transaction
        return f"You have withdraw kshs.{self.withdrawals} and your new balance is {self.balance} on {date.strftime('%d/%m/%Y')})"
           
    def deposits_statement(self):
        for x in self.deposits: 
            print(x)
    def withdrawals_statement (self):
        for y in self.withdrawals:
            print(y)  
    def balance(self):
        return self.balance 
    def current_balance(self):
        return f"your current balance is{self.balance}"
    def full_balance(self):
        statement=self.deposits+self.withdrawals
        for x in statement:
            print(x["narration"])
    def borrow(self,amount):
            sum=0
            for y in self.deposits:
                sum+=y["amount"]
            if len(self.deposits) <10:
                return f"you are not eligible to borrow.make {10-len(self.deposits)} to borrow "
            if amount<100:
                return f"you can borrow atleast 100"  
            if amount>sum/3:
                return f"you can borrow upto {sum/3}" 
            if self.balance!=0:
                return f"you have Ugshs.{self.balance} you cant borrow yet you still have balance on your account"
            if self.loan_balance!=0:
                return f"you have a debt of {self.loan_balance} you have to pay first for you to borrow."
            else:

               interest= 3/100*(amount)
            self.loan_balance+=amount+interest
            return f"you have borrowed {amount} your loan is now at {self.loan_balance}"
    
    def loan_repayment(self,amount):
        
         if amount>self.loan_balance:
             self.balance+=amount-self.loan_balance
             self.loan_balance=0
             return f" thank you for paying the loan of {amount-self.loan_balance} your account balance is {self.balance}"
               
         else:
             self.loan_balance-=amount
             return f"thank you"
            
         
    def transfer(self,amount,new_account):
        if amount<=0:
            return "invalid amount"
        if amount>=self.balance:
            return f"insuficient funds"
        if isinstance(new_account,Account):
            self.balance-=amount
            new_account.balance+=amount
            return f"you have sent {amount} to {new_account} with the name {new_account.name}.your new balance is {self.balance}"        


        
# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance.  def withdraw (self,amount):

# Update the withdrawal method to store each withdrawal transaction as a dictionary like like this
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }
# Update the deposit method to store each deposit transaction as a dictionary like this
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }
# Add a new method  full_statement which combines both deposits and withdrawals into one list ordered by date and using a for loop prints each transaction in a new line like this
# 16/06/22 —----- Deposit —---- 1000
# Add a new attribute loan_balance which is zero by default.
# Add a borrow method which allows a customer to borrow if they meet these conditions:
# Customer has made at least 10 deposits.
# Loan amount requested must be more than 100
# A customer qualifies for a loan amount that is less than  or equal to 1/3 of their total sum of deposit history
# Customer account has no has no balance
# Customer has no outstanding loan
# The loan attracts  an interest of 3%.
# Add a loan repayment method with these conditions
# A customer can repay a loan to reduce the current loan balance
# Overpayment of a loan increases a customers current deposit
# Add a new method transfer which accepts two attributes (amount and instance of another account). If the amount is less than the current instances balance, the method transfers the requested amount from the current account to the passed account. The transfer is accomplished by reducing the current account balance and depositing the requested amount to the passed account
  
      
   


    



    