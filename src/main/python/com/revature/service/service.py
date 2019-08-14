

def authentification(user):
    login = input('Login : ')
    user.append(login)
    password = input('Password : ')
    user.append(password)
    print("\n    Login success!")
    return True

    
def balance(account): 
	#here code check balance
    print('your balance is',account[1])

def printAccount(account):
    print("Name : %s " % (account[0]))
    print("Account number : %s " % (account[1]))


def createUser(user):
    print("\n        Thank you! You've successfully signed up." )
    return user

def createAccount(account):
    return account


def deposit(amount, account):
	#here code deoisit
    newbalance =  0
    newbalance = int(amount) +  int(account[1])
    account[1] = newbalance
    return account
        
def withdraw(amount, account):
	#here code withdraw
    newbalance =  0
    newbalance = int(account[1]) -  int(amount)
    account[1] = newbalance
    return account


def transaction(transactions):
	#here code transaction
    for t in transactions:
        print(t)
    return transaction

def logout(user):
	#here code logout
    return


def printUser(user):
    print("Name : {0}".format(user[0]))
    print("Email : {0}".format(user[1]))
    print("P Number : {0}".format(user[2]))





