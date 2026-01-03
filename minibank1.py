#This is a simple minibank project. (3.1.2026)
#This includes Three main sessions for every user: Transfer money, withdraw money, and update user info.
#For data record, only dictionary is used whil the program running.
#In the next project, this minibank will be implemented by using file handling processes.

class MiniBank:

    main_userInfo: dict = {}

    def firstOption(self):
        while True:
            try:
                option: int = int(input("\nPress 1 to log in.\nPress 2 to Register.\nPress 0 to exit."))
                print("User choice: ", option)

                if option == 1:
                    self.login()
                elif option == 2:
                    self.register()
                elif option == 0:
                    print("Bye Bye...")
                    exit(option)
                else:
                    print("Invalid Input. Try again.")
            except ValueError:
                print("Invalid Input. Try again.")
                
    def returnId (self, transfer_username):
        userInfoLength :int = len(self.main_userInfo)
        for i in range (1, userInfoLength+1):
            if self.main_userInfo[i]['r_username'] == transfer_username:
                return i
        return None
        
    def menu(self, loginID):
        menu_input: int = int(input("Press 1 to Transfer.\nPress 2 to Withdraw.\nPress 3 to update user data."))

        #Transfer
        if menu_input==1:
            print("\n_____Transfer Session_____\n")
            transfer_username: str = input('Please enter username to transfer: ')
            transfer_id : int = self.returnId(transfer_username)
            print("Transfer ID: ",transfer_id)
            print("Your ID: ", loginID)
            while True:
                try:
                    amount: int = int(input("Enter amount to transfer: "))
                    if amount > self.main_userInfo[loginID]['amount']:
                        print("Insufficient balance...")
                        continue
                    break
                except ValueError:
                    print("Invalid Input. Try again.")
            print("Check the following details and confirm again:\nTransfer ID ={0}\nYour ID = {1}\n" \
                    "Amount to transfer = {2}".format(transfer_id, loginID, amount))
            while True:
                finalDecision = input("Enter 1 to confirm tranfer process.\nEnter 0 to cancel.")
                if finalDecision=='1':
                    while True:
                        passCheck = input("Enter passcode again to complete transfer: ")
                        if passCheck == self.main_userInfo[loginID]['r_passcode']:
                            break
                        else:
                            print("Wrong passcode... Try again.")
                            continue
                    self.main_userInfo[loginID]['amount'] = self.main_userInfo[loginID]['amount']-amount
                    self.main_userInfo[transfer_id]['amount']=self.main_userInfo[transfer_id]['amount']+amount
                    print("Transfer complete!")
                    print(f'Your amount: {self.main_userInfo[loginID]['amount']}')
                    print(f"Receiver amount: {self.main_userInfo[transfer_id]['amount']}")
                    break
                    
                elif finalDecision == '0':
                    print("Transfer cancelled.")
                    break
                else:
                    print("Invalid Input. Try again.")

        #Withdraw money
        elif menu_input == 2:
            print("\n_____Withdrawal Session_____\n")
            while True:
                try:
                    withdrawAmount = int(input("Enter amount to withdraw: "))
                    if withdrawAmount > self.main_userInfo[loginID]['amount']:
                        print("Insufficient balance...")
                        continue
                    break
                except ValueError:
                    print("Invalid Input. Try again.")
            while True:
                finalDecision = input("Enter 1 to confirm withdrawl process.\nEnter 0 to cancel.")
                if finalDecision == '1':
                    while True:
                        passCheck = input("Enter passcode again to complete withdrawl: ")
                        if passCheck == self.main_userInfo[loginID]['r_passcode']:
                            break
                        else:
                            print("Wrong passcode... Try again.")
                            continue
                    self.main_userInfo[loginID]['amount'] = self.main_userInfo[loginID]['amount']-withdrawAmount
                    print(f"Your left amount : {self.main_userInfo[loginID]['amount']}")
                    break
                elif finalDecision == '0':
                    print("Withdrawl cancelled...")
                    break
                    
                else:
                    print("Invalid Input. Try again")
        
        #Update user data
        elif menu_input == 3:
            while True:
                print("\n_____Updating User Data_____\n")
                updateChoice = input("Enter 1 to change name.\nEnter 2 to change passcode.\nEnter 3 to add more money.\n" \
                                    "Enter here: ")
                if updateChoice == '1':
                    newName = input("Enter new name: ")
                    while True:
                        passCheck = input("Enter passcode to proceed: ")
                        if passCheck == self.main_userInfo[loginID]['r_passcode']:
                            break
                        else:
                            continue
                    self.main_userInfo[loginID]['r_username'] = newName
                    print(f"Name has been updated...New details : {self.main_userInfo[loginID]}")
                    
                elif updateChoice == '2':
                    newPasscode = input("Enter new passcode: ")
                    while True:
                        passCheck = input("Enter passcode to proceed: ")
                        if passCheck == self.main_userInfo[loginID]['r_passcode']:
                            break
                        else:
                            print("Wrong passcode... Try again.")
                            continue
                    self.main_userInfo[loginID]['r_passcode'] = newPasscode
                    print(f"Password has been updated...New details : {self.main_userInfo[loginID]}")
                                        
                elif updateChoice == '3':
                    while True:
                        try:
                            addBalance = int(input("Enter amount to add: "))
                            break
                        except ValueError:
                            print("Invalid Input. Try again.")
                    while True:
                        passCheck = input("Enter passcode to proceed: ")
                        if passCheck == self.main_userInfo[loginID]['r_passcode']:
                            break
                        else:
                            continue   
                    self.main_userInfo[loginID]['amount'] = self.main_userInfo[loginID]['amount']+addBalance
                    print(f"Balance has been updated...New details : {self.main_userInfo[loginID]}")                  

                else:
                    print("Invalid Input. Try again.")
                    
    def login(self):
        print("\n_______This is login________\n")
        l_username: str = input("Please enter username: ")
        l_userpasscode: str = input("Please enter passcode to log in: ")
        existUser = self.existUser(l_username, l_userpasscode)
        if existUser:
            print("\n_______Log in successful._______\n")
            loginID : int = self.returnId(l_username)
            self.menu(loginID)
        else: 
            print("You cannot log in.")

    def existUser(self, l_username, l_userpasscode):
        usercount = len(self.main_userInfo)
        for i in range (1, usercount+1):
            if self.main_userInfo[i]["r_username"] == l_username and self.main_userInfo[i]["r_passcode"] == l_userpasscode:
                return True
        return False


    def register(self):
        print("\n_________This is register________\n")
        r_username: str = input("Please enter username to register: ")
        while True:
            try:
                r_amount: int = int(input("Enter amount: "))
                break
            except ValueError:
                print("Invalid Input. Try again.")
        r_passcode1: str = input("Please enter passcode to register: ")
        r_passcode2: str = input("Please enter passcode to confirm: ")
        if r_passcode1 == r_passcode2:
            id: int = self.CheckingUserCount()
            userInfoForm : dict = {id: {"r_username": r_username, "r_passcode": r_passcode2, "amount": r_amount}}
            self.main_userInfo.update(userInfoForm)
            print("#### Success Register ####")

    def CheckingUserCount(self):
        count = len(self.main_userInfo)
        return count+1
             
if __name__=="__main__":
    miniBank: MiniBank = MiniBank()
    while True:

        miniBank.firstOption()
