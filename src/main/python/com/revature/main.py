from service import service

def main():
    print("\n\n*****Welcome to Revature Bank******")

    #here code for authentification
    user = []
    result = service.authentification(user)
    
    x = '*'
    
    user = []
    account = []
    transactions = []
    i = 0

    while(result):


        print('\n\n How can I assist you\n\n')
        print('Press 1 to Create User')
        print('Press 2 to Create Account')
        print('Press 3 to Deposit')
        print('Press 4 to Withdrawal')
        print ('Press 5 to Balance')
        print ('Press 6 to Transaction')
        print ('Press 7 to Print User')
        print ('Press 8 to print Account')
        print ('\n    **************')
        print('What Would you like to choose?: ')


        x = input(    )
             
        if x=='1':
            print('\n    Creating a User\n')
            user.append(input('User name: '))
            user.append(input('Email: '))
            user.append(input('Phone number : '))
            user.append(input('SSN number: '))
            user = service.createUser(user)
           
        if x=='2':
            account.append(input('Account Name: '))
            account.append(input('Balance: '))
            account = service.createAccount(account)

        if x=='3':
            amount = input('Please Enter amount: ')
            account = service.deposit(amount, account)
            transactions.append("deposit made"+str(i))
            i += 1

        if x=='4':
            amount = input('Enter the Amount: ')
            account = service.withdraw(amount, account)
            transactions.append("withdraw made "+str(i))
            i += 1

        if x=='5':
            print('\nFind your balance below: \n')
            service.balance(account)

        if x=='6':
            print('\n   Find your transaction below: \n')
            service.transaction(transactions)   

        if x=='7':
            print('\nUser informations : \n')
            service.printUser(user)

        if x=='8':
            print('\nAccount information : \n')
            service.printAccount(account)

        if x=='no':
            result = False
            print('Thank you for visiting!')

if __name__ == "__main__":
     main()
