Login_User_id = ''
Amount = 0.0  
def get_id():
    try:
        with open('Customer.txt', 'r') as file:
            lines = file.readlines()
            
            if not lines:
                return 1001
            line = lines[-1]
            #print(line)
            last_id = int(line.split(',')[2])
            return last_id + 1
            #print(lines)
            
    except FileNotFoundError:
        return 1001
#print(get_id())
#=============================================================================================================



def get_accountnumber():
    try:
        with open('Customer.txt', 'r') as file:
            lines = file.readlines()
            
            if not lines:
                return 100000001
            line = lines[-1]
            last_accountnumber = int(line.split(',')[1])
            return last_accountnumber + 1
            #print(lines)
            
    except FileNotFoundError:
        return 100000001
    

#=======================================================================================

def security():
    global Login_User_id
    while True:
        print('For customer security purpose enter your NIC number')
        ic = input('Enter your NIC number:')
        try:
            with open ('nic.txt','r')as file:
                user_found = False
                for line in file:
                    IC = line.strip().split(',')
                    if len(IC) >= 2:
                        user_id = IC[0]
                        NIC = IC[1]
                        if NIC == ic:
                                user_found = True
                                if user_id != Login_User_id:
                                    print("NIC dosen't match with your user_id:")
                                    continue

                                while True:
                                    new_password = input('Enter your new password:')
                                    confirm_password = input('Enter your confirm password again:')
                                    if new_password == confirm_password:
                                        updated = False
                                        with open ('Customer.txt','r')as ffile:
                                            rule = ffile.readlines()
                                            
                                            for i, line in enumerate(rule):
                                                datas = line.strip().split(',')
                                                if len(datas) >= 5:
                                                    name = datas[0]
                                                    accountnumber = datas[1]
                                                    userid = datas[2]
                                                    username = datas[3]
                                                    password = datas[4]
                                                    
                                                    if Login_User_id == userid:
                                                        password = new_password
                                                        updated = True
                                                        rule[i] = f'{name},{accountnumber},{userid},{username},{password},\n'
                                                        print('Your password has been changed.')
                                                        break
                                            if updated:
                                                with open('Customer.txt', 'w') as customer_file:
                                                    customer_file.writelines(rule)
                                                    return password
                                    else:
                                        print('Password do not match! Please try again.')         
                                        #break
            if not user_found:
                print('NIC not found. Please try again !')
                print('1. Try again')
                print('2. Create customer')
                print('3. Exit')
                choice = input('Enter your choice: ')
                if choice == '1':
                    continue
                elif choice == '2':
                    create_customer()
                elif choice == '3':
                    print('Exiting...')
                    return
                else:
                    print('Invalid input. Please enter 1, 2, or 3.')
                    continue         
        except Exception as e:
            print(f"An error occurred: {e}")
            return

#security()                                   
#=========================================================================================================

def check_username():
    global Login_User_id

    while True:

        user_name = input('Enter your username: ')
        user_found = False

        try:
            with open('Customer.txt', 'r') as file:
                for line in file:
                    details = line.strip().split(',')
                    if len(details) >= 5:
                        userid = details[2]
                        username = details[3]
                        password = details[4]
                        #while True:
                        if user_name == username:
                            user_found = True
                            Login_User_id = userid
                            for attempt in range(3):
                                print(' 1. Forgot Password')
                                user_password = input('Enter your password or Enter 1 to change password: ')
                                #c = input('Enter 1 to change password:')
                                if user_password == '1':
                                    #security()
                                    changed_password = security()
                                    if changed_password:
                                        p_word = input('Enter your changed password:')
                                        if changed_password == p_word:
                                            print('Access successful.')
                                            return
                                        else:
                                            print('Illegal activity!')
                                            exit()
                                    #break
                                elif user_password == password:
                                    print('Access Successful!')
                                    return
                                else:
                                    print(f'Incorrect password. Attempts left: {2 - attempt}')
                            print('Access Denied! Too many failed attempts.')
                            exit()
                            return  
            if not user_found:
                print('\nCustomer not found.')
                print('1. Try again')
                print('2. Create customer')
                print('3. Exit')
                choice = input('Enter your choice: ')
                if choice == '1':
                    continue
                elif choice == '2':
                    create_customer()
                elif choice == '3':
                    print('Exiting...')
                    return
                else:
                    print('Invalid input. Please enter 1, 2, or 3.')
                    continue
        except FileNotFoundError:
            print("Customer file not found.")
            exit()

        except Exception as e:
            print(f'error occurred{e}')
            return

#print(get_accountnumber())


#=======================================================================================================

def unique_username():
    while True:
        try:
            use_name = input('Enter username: ')
            username_exists = False

            try:
                with open('user_name.txt', 'r') as file:
                    for line in file:
                        user_name = line.strip().split(',')
                        if use_name == user_name[0]:
                            username_exists = True
                            break
            except FileNotFoundError:
                # If file doesn't exist, assume no users yet
                pass

            if username_exists:
                print('Username already exists! Enter another username.')
            else:
                with open('user_name.txt','a')as file:
                    file.write(f'{use_name}\n')
                    return use_name

        except Exception as e:
            print(f"An error occurred: {e}")
            break

#=======================================================================================================
       





def create_customer():
    name = input('Enter name:')
    nic_number = input('Enter your NIC_Number:')
    user_id = get_id()
    accountnumber = get_accountnumber()
    use_name =unique_username()
    password = input('Enter user password: ')
    
    while True:
        try:
            balance = float(input('Enter initial balance: '))
            if balance <= 0:
                print('Balance must be greater than 0!')
            else:
                break
        except ValueError:
            print('Enter number only!')

        
    while True:
        account_type = input('Enter account_type as(savings_account or current_account: )').strip().lower()
        if account_type == 'savings_account':
            statement = 'savings_account'
            break
        elif account_type == 'current_account':
            statement = 'current_account'
            break
        else:
            print("Invalid account type. Please enter 'savings_account' or 'current_account'.")
 
    with open('Customer.txt', 'a') as file:
        file.write(f'{name},{accountnumber},{user_id},{use_name},{password},\n')
    with open('balance.txt','a')as file:
        file.write(f'{user_id},{balance},{statement}\n')
    with open('nic.txt','a')as file:
        file.write(f'{user_id},{nic_number},\n')
    
    print(f"Customer account created successfully. Assigned accountnumber: {accountnumber}.Assigned user_ID:{user_id}")


#==================================================================================================



def action_deposit():
    global Login_User_id
    if Login_User_id is None:
        print("Please log in first!")
        return

    action = 'deposit'
    while True:
        try:
            amount = float(input('Enter the deposit amount: '))
            if amount <= 0:
                print('Deposit amount must be greater than 0.')
            else:
                break
        except ValueError:
            print('Invalid input! Please enter a valid number for the deposit.')

    try:
        # Read balance file and update the balance
        with open('balance.txt', 'r') as ffile:
            lines = ffile.readlines()
        
        updated = False
        for i, line in enumerate(lines):
            datas = line.strip().split(',')
            if len(datas) >= 3:
                bal_user_id = datas[0]
                balance = float(datas[1])
                statement = datas[2]
                
                if Login_User_id == bal_user_id:
                    balance += amount
                    lines[i] = f'{bal_user_id},{balance},{statement}\n'
                    updated = True
                    print('Deposit successful!')
                    break
        
        # If the user was found, write the updated data back to balance.txt
        if updated:
            with open('balance.txt', 'w') as ffile:
                ffile.writelines(lines)
            
            # Write the transaction to the transaction file
            from datetime import datetime
            with open('transactions.txt', 'a') as file:
                date_time = datetime.now().strftime('%d-%m-%Y %A %I.%M %p')
                file.write(f'{Login_User_id},{date_time},{action},{amount}\n')
        else:
            print('User not found in balance file.')

    except Exception as e:
        print(f"An error occurred: {e}")
        

#==============================================================================================================


def action_withdraw():
    global Amount
    while True:
        try:
            amount = float(input('Enter the withdrawal amount: '))
            if amount <= 0:
                print('Withdrawal amount must be greater than 0.')
                continue
            else:
                Amount = amount  # Save as float globally
                check_amount()
                break  # Exit after one transaction
        except ValueError:
            print('Please enter a valid number.')
        except Exception as e:
            print(f'An error occurred: {e}')


#=============================================================================================

def check_amount():
    global Login_User_id
    global Amount
    action = 'withdraw'
    
    try:
        with open('balance.txt', 'r') as ffile:
            lines = ffile.readlines()

        updated = False
        for i, line in enumerate(lines):
            datas = line.strip().split(',')
            if len(datas) >= 3:
                bal_user_id = datas[0]
                balance = float(datas[1])
                statement = datas[2]

                if Login_User_id == bal_user_id:
                    if Amount > balance:
                        print('Invalid Withdrawal! Your withdrawal amount is greater than your balance.')
                        return
                    else:
                        balance -= Amount
                        lines[i] = f'{bal_user_id},{balance},{statement}\n'
                        updated = True
                        print('Withdrawal successful!')
                        break

        if updated:
            with open('balance.txt', 'w') as ffile:
                ffile.writelines(lines)

            # Log the transaction
            from datetime import datetime
            with open('transactions.txt', 'a') as file:
                date_time = datetime.now().strftime('%d-%m-%Y %A %I:%M %p')
                file.write(f'{Login_User_id},{date_time},{action},{Amount}\n')
        else:
            print('User not found in balance file.')

    except Exception as e:
        print(f'An error occurred while checking amount: {e}')


#==========================================================================================
        

def view_balance():
    global Login_User_id
    try:
        with open('balance.txt','r')as ffile:
            for file_line in ffile:
                datas = file_line.strip().split(',')
                if len(datas) >= 3:
                    bal_user_id = datas[0]
                    balance = datas[1]
                    statement = datas[2]
                    if Login_User_id == bal_user_id:
                        print(f'Your balance is {balance} in {statement}\n')
                        return
        print('User data not found!')
    except FileNotFoundError:
        return None

#==============================================================================================



def transaction_history():
    global Login_User_id
    try:
        with open('transactions.txt','r')as file:
            details = file.readlines()
            for i, line in enumerate(details):
                data = line.strip().split(',')
                if len(data) >= 4:
                    userid = data[0]
                    date = data[1]
                    action = data[2]
                    amount = data[3]
                    if Login_User_id in userid:
                        print(f'{date} : {action} : {amount}\n')
    except FileNotFoundError:
        return None

#========================================================================================================



def admin_menu():
    while True:
        print('\nADMIN MENU')
        print('1. Create Customer')
        print('2. Deposit Money')
        print('3. Withdraw Money')
        print('4. View Balance')
        print('5. View Transactions')
        print('6. Exit')
        choice = input('Enter a number (1-6): ')
        if choice == '1':
            create_customer()
        elif choice == '2':
            check_username()
            action_deposit()
        elif choice == '3':
            check_username()
            action_withdraw()
        elif choice == '4':
            check_username()
            view_balance()
        elif choice == '5':
            check_username()
            transaction_history()
        elif choice == '6':
            print('Exiting...')
            login()
            break
        else:
            print('Invalid option. Please enter a number from 1 to 6.')

#===================================================================================================


def customer_menu():
    while True:
        print('\nCUSTOMER MENU')
        print('1. Deposit Money')
        print('2. Withdraw Money')
        print('3. View Balance')
        print('4. View Transactions')
        print('5. Exit')
        choice = input('Enter a number (1-5): ')
        if choice == '1':
            action_deposit()

        elif choice == '2':
            action_withdraw()

        elif choice == '3':
            view_balance()
        
        elif choice == '4':
            transaction_history()
            
        elif choice == '5':
            print('Exiting...')
            login()
            break
           
        else:
            print('Invalid option. Please enter a number from 1 to 5.')
                           

#===============================================================================================                          



with open('user.txt','w')as file:
    file.write(f'admin,1234\n')



def login():
    print('======login======')
    print('1. Admin')
    print('2. Customer')      
    print('3. Exit') 

    login = input('Enter number(1-3):').strip()
    while True:
        if login == '1':
            user_name = input('Enter user name:')
            user_password = input('Enter password:')
            log_in = False
            with open ('user.txt','r')as file:
                for line in file:
                    username,password = line.strip().split(',')
                    if username == user_name and password == user_password:
                        print('Admin login sucessful!')
                        log_in = True
                        admin_menu()
                        break
                        
            if not log_in:
                print('Admin login failed. Invalid username or password.')

        elif login == '2':
            check_username()
            customer_menu()
            break
        elif login == '3':
            print('Exiting...')
            exit()
            break
        
login()
                    




    





        
