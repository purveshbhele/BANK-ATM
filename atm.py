print('Welcome to this Atm')
Name=input('what is your Name-')
print('Hello ' + Name)

class ATM(object):
    def cardNumber():
        num=input('Enter your card number - ')
        
    def pin():
        pin=input('Enter your pin number - ')
        
    def withdraw():
        balance=100000
        Money=int(input('How much money do you want to withdraw - '))
        if Money < balance:
            balance=int(balance)-Money
            print('Your balance is , '+str(balance))
        
        if Money>balance:
            print('Not enough money')

    def deposit():
        balance=100000
        Money=int(input('How much money do you want to deposit - '))       
        balance = balance+int(Money)
        print('Your balance is - '+str(balance))
    
    def CheckBalance():
        balance=str(100000)
        print('Your balance is - '+balance)

    cardNumber()
    pin()
    
    print("What do you want to do-")
    way=str(input('withdraw = press 1,deposit = press 2,Check Balance = press 3 -> '))
    
    if way=='1':
        withdraw()
    elif way=='2':
        deposit()
    elif way=='3':
        CheckBalance()
    elif transaction != ('1'or'2'or'3'):
        print('There is no transaction for the number '+ transaction)