class AccountHandler:
    accounts = []

    def createNewAccount(self):
        accNo = int(input("Enter new account number: "))
        accName = input("Enter your name: ")
        accBal = int(input("Enter your opening balance: "))
        if(self.checkAccount(accNo) == False):
            self.accounts.append(Account(accNo, accName, accBal))
            print("Your account has been created!!!")
        else:
            print("Sorry!!! the account has been already created")
        print("********************************")

    def checkBalance(self):
        accNum = int(input("Please enter your account number: "))
        if(self.checkAccount(accNum)):
            print(
                f"Your current balance is: {self.checkAccount(accNum).accBal}")
        else:
            print("Sorry!!! We could not find this account.")

    def depositAmt(self):
        accNum = int(input("Please enter your account number: "))
        if(self.checkAccount(accNum)):
            addAmt = int(input("Enter the deposit amount: "))
            self.checkAccount(accNum).accBal += addAmt
            print("Your amount has been deposited!!!")

        else:
            print("Sorry!!! We could not find this account.")
    
    def withdrawAmt(self):
        accNum = int(input("Please enter your account number: "))
        if(self.checkAccount(accNum)):
            depAmt = int(input("Enter the amount you want to withdraw: "))
            if(self.checkAccount(accNum).accBal >= depAmt):
               self.checkAccount(accNum).accBal -= depAmt 
               print(f"You have withdrawn {depAmt} from your account.")
            else: 
                ("Sorry!!! You don't seem to have enough balace")

        else:
            print("Sorry!!! We could not find this account.")

    def transferAmt(self):
        accSender = int(input("Enter your account: "))
        if(self.checkAccount(accSender)):
            accReceiver = int(input("Enter the account number whom you want to transfer amount: "))
            if(self.checkAccount(accReceiver)):
                depAmt = int(input("Enter the amount you want to withdraw: "))
                if(self.checkAccount(accSender).accBal >= depAmt):
                    self.checkAccount(accSender).accBal -= depAmt 
                    self.checkAccount(accReceiver).accBal += depAmt
                    print(f"You have transfered {depAmt} from your account.")
                else: 
                    ("Sorry!!! You don't seem to have enough balace")
            else:
                print("Sorry!!! We could not find this account.")
        else:
            print("Sorry!!! We could not find this account.")
    
    def listAccount(self):
        for account in self.accounts:
            print(f'''Account Number: {account.accNo} \nAccount Name: {account.accName} \nAccount Balance: {account.accBal}''')
    
    def deleteAccount(self):
        accNo = int(input("Enter the account number you want to delete: "))
        if(self.checkAccount(accNo)):
            self.accounts.remove(self.checkAccount(accNo))
            print("Account has been deleted")
        else:
            print("Invalid Account!!!")

    def checkAccount(self, NewAccNo):
        for obj in self.accounts:
            if NewAccNo == obj.accNo:
                return obj
        return False

class UserHandler:
    users = []
    blockedUsers = []
    
    def checkUser(self, username, password):
        for user in self.users:
            if(user.username == username):
                return True
        if(username == "admin" and password == "admin"):
            return True
        else:
            return False

    def checkBlockedUser(self, username):
        if(username in self.blockedUsers):
            return True
        else:
            return False
    
    def createNewUser(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        confirmPassword = input("Confirm passwrod: ")
        if(not self.checkUser(username, password) and password == confirmPassword):
            self.users.append(User(username, password))
            print("Account created successfully!!!")
        else: 
            print("Username already exists!!!")
    
    def listUser(self):
        print(f"The list of users are: \n")
        for user in self.users:
            print(user.username)
    
    def listBlockedUsers(self):
        print(f"The list of blocked users are: \n")
        for user in self.blockedUsers:
            print(user)
    
    def blockUser(self, username = None):
        if (username == None ):
            username = input("Enter username: ")
            if(not self.checkBlockedUser(username)):
                self.blockedUsers.append(username)    
                print("Account has been blocked!!!")
        else:
            if(not self.checkBlockedUser(username)):
                self.blockedUsers.append(username)
                print("This account has been blocked. Please contact admin for more info!!!")
    
    def unblockUser(self):
        username = input("Enter username: ")
        if(self.checkBlockedUser(username)):
            self.blockedUsers.remove(username)
        else:
            print("This user is not blocked")

    def deleteUser(self):
        username = input("Enter username: ")
        if(self.checkUser(username)):
            self.Users.remove(username)
        else:
            print("This username doesnot exits!!!")
    
    def checkAdmin(self, username, password):
        if(username == "admin" and password == "admin"):
            return True
        else:
            return False
    

    def adminMode(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if self.checkAdmin(username, password):
            isAdmin = True
        else:
            print("Login failed!!!")
            isAdmin = False
        while isAdmin:
                print("\t*****Welcome admin*****")
                ain = int(input('''\ta. Press 1 to create new user 
                b. Press 2 to list user
                c. Press 3 to block user
                d. Press 4 to unblock user
                e. Press 5 to list blocked user
                f. Press 6 to delete user
                g. Press 7 to exit admin mode: \n'''))
                if ain == 1:
                    self.createNewUser()
                elif ain == 2:
                    self.listUser()
                elif ain == 3:
                    self.blockUser()
                elif ain == 4:
                    self.unblockUser()
                elif ain == 5:
                    self.listBlockedUsers()
                elif ain == 6:
                    self.deleteUser()
                elif ain == 7:
                    isAdmin = False
                else:
                    print("Enter appropriate choice!!!")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Account:
    def __init__(self, accNo, accName, accBal):
        self.accNo = accNo
        self.accName = accName
        self.accBal = accBal


if __name__ == "__main__":
    isRunning = True
    account = AccountHandler()
    user = UserHandler()
    x = 0
    y = 0
    while isRunning:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if(not user.checkBlockedUser(username) and  user.checkUser(username, password)):
            while (y< 3):
                print("\t*****Welcome to our Bank*****")
                uin = int(input('''\ta. Press 1 to create new account 
                b. Press 2 to check Balance+
                c. Press 3 to deposit Balance
                d. Press 4 to withdraw Balance
                e. Press 5 to transfer Balance
                f. Press 6 to list all accounts
                g. Press 7 to delete account
                h. press 8 to enter admin mode
                i. Press 9 to exit: \n'''))
                if uin == 1:
                    account.createNewAccount()
                elif uin == 2:
                    account.checkBalance()
                elif uin == 3:
                    account.depositAmt()
                elif uin == 4:
                    account.withdrawAmt()
                elif uin == 5:
                    account.transferAmt()
                elif uin == 6:
                    account.listAccount()
                elif uin == 7:
                    account.deleteAccount()
                elif uin == 8:
                    user.adminMode()
                elif uin == 9:
                    adin = input("Would you like to relogin? Y/N: ")
                    if(adin.lower() == "y"):
                        y = 3
                    else:
                        print("Thanks for using!!!")
                        y = 9
                        isRunning = False
                else:
                    print("Please input valid options.")          
            
        elif(user.checkBlockedUser(username)):
            print("This account has been blocked. Please contact admin for more info!!!")
            uin = input("Would you like to continue? Y/N: ")
            if(uin == "y" or uin == "Y"):
                    x = 0
                    y = 0
            else:
                print("Thanks for using!!!")
                y = 4
                isRunning = False 
        else:
            print("Invalid username/password!!!")
            print(f"Attempts left: {(2-x)}")
            x+=1
            if (x==3):
                user.blockUser(username)
                uin = input("Would you like to continue? Y/N: ")
                if(uin == "y" or uin == "Y"):
                    x = 0
                    y = 0
                else:
                    print("Thanks for using!!!")
                    y = 4
                    isRunning = False