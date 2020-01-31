class AccountHolder:
    def __init__(self, fname, lname, mname, atype, balance, status):
        self.first_name = fname
        self.last_name = lname
        self.middle_name = mname
        self.account_type = atype
        self.balance = balance
        self.status = status

class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.account = []
    def open_new_account(self, fname, lname, mname, atype, balance, status):
        if balance >= 100:
            # creat an account holder
            temp = AccountHolder(fname, lname, mname, atype, balance, status)

            # store new account holder in accounts list
            self.account.append(temp)
           
            # return a message, "Account created for fname, lname"
            return (f"A {atype} was created for {fname} {lname} with a balance of {balance}")
           
        else:
            #return "Insufficent deposit amouint"
            return ("Insufficent funds to create a new account")
            # main()
    def show_account_holders(self):
        for account_holder_obj in self.account:
            print(f"{account_holder_obj.first_name} {account_holder_obj.last_name} {account_holder_obj.balance}")

    def withdraw_funds(self, balance):
        for balance in self.account:
            withdrawl = print(input(int("How much would you like to withdraw?")))
            new_balance = withdrawl - self.balance
            if new_balance < 0:
                print("You don't have that much money!")
            else:
                print(int(balance))     

# defintion of a main that includes a while loop with a menu of things the user wants to do

def main():
    wellsfargo = Bank("Wells Fargo", "123 Sesame Street")
    action = 1

    while action != 6:
        print("1. Create an account")
        print("2. Print list of all account holders")
        print("3. Withdraw money from your account")
        print("6. Exit application")

        action = int(input("What would you like to do?"))

        if (action == 1):
            fname = input("What is your first name")
            mname = input("what is your middle name")
            lname = input("What is your last name?")
            atype = input("What would you like to open: Checking or Savings?")
            deposit = int(input("How much would you like to deposit?"))
            wellsfargo.open_new_account(fname, mname, lname, atype, "pending", deposit)
            print()

        elif (action == 2):
            wellsfargo.show_account_holders()

        elif (action == 3):
            wellsfargo.withdraw_funds()


        elif (action == 6):
            break





# main()
main()

