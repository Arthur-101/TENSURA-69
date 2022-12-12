import csv
import time
import random

def random_num():
    global r1
    r1 = str(random.randint(12345678,87654321))

def acc_num():
    with open('acc_num.csv','a',newline='') as k:
        writer2 = csv.writer(k,delimiter='-')
        with open('acc_num.csv','r') as f:
            reader2 = csv.reader(f,delimiter='-')
            rownum2 = 0
            for row2 in reader2:        
                if row2 == [r1]:
                    rownum2 = rownum2+1
                else:
                    continue
            if rownum2 == 1:
                random_num()
            else:
                writer2.writerow([username,r1])
                with open(username+'_customer.csv','a',newline='') as m:
                    writer3 = csv.writer(m,delimiter=':')
                    writer3.writerow([r1])
                    writer3.writerow(["^^^^^^^^ Your Account Number"])
                    writer3.writerow(["Your UserName Is  ",username])
                    writer3.writerow(["Your Password Is  ",password])
                    writer3.writerow(["Your Address Is  ",address])
                with open(username+'_employee.csv','a',newline='') as n:
                    writer4 = csv.writer(n,delimiter=':')
                    writer4.writerow([r1])
                    writer4.writerow(["^^^^^^^^ Account Number"])
                    writer4.writerow(["UserName  ",username])
                    writer4.writerow(["Address  ",address])
                acc_num_file()

def acc_num_file():
    with open(r1+'.csv','a',newline='') as l:
        writer5 = csv.writer(l,delimiter=',')
        first_money = input("How much money do you want to add for the first time? (in ₹) : ")
        writer5.writerow([first_money])

def register():
    global username
    global password
    global address
    with open('users.csv','a',newline='') as f:
        writer = csv.writer(f,delimiter=',')
        username = input("Create Username : ")
        password = input('Create Password : ')
        passwordc= input('Confirm Password : ')
        with open('users.csv','r') as f:
            reader = csv.reader(f,delimiter=',')
            rownum = 0
            for row in reader:        
                if row == [username, password]:
                    rownum = rownum+1
                else:
                    continue
            if rownum == 1:                               
                acc_exist()
                if inp == '1' or inp == 'login' or inp == 'Login' or inp == 'LOGIN':
                    login()
                elif inp == '2' or inp == 'new' or inp == 'New' or inp == 'NEW':
                    register()
                elif inp == '3' or inp == 'b' or inp == 'B' or inp == 'back' or inp == 'Back' or inp == 'BACK':
                    user_employee()
                else:
                    print("INVALID INPUT\nPlease choose correct options....\n..")
                    time.sleep(2)
                    acc_exist()
            else:
                if password == passwordc:
                    address = input("Enter Your Adderess : ")
                    random_num()
                    acc_num()
                    writer.writerow([username,password])
                    print("Your Registration is Succesful!!")
                else:
                    print("Passwords don't match\nTRY AGAIN !!\n..\n...")
                    register()

def login():
    usernamelog = input("Enter Your Username : ")
    passwordlog = input("Enter Your Password : ")
    with open('users.csv','r') as f:
        reader = csv.reader(f,delimiter=',')
        rownum = 0
        for row in reader:        
            if row == [usernamelog, passwordlog]:
                rownum = rownum+1
            else:
                continue
        if rownum == 1:                               
            print("Login Succesfully")
        else:
            print("Incorrect Username or Password\nTry one more Time....\n...")
            usernamelog = input("Enter Your Username : ")
            passwordlog = input("Enter Your Password : ")
            with open('users.csv','r') as f:
                reader = csv.reader(f,delimiter=',')
                rownum = 0
                for row in reader:        
                    if row == [usernamelog, passwordlog]:
                        rownum = rownum+1
                    else:
                        continue
                if rownum == 1:                               
                    print("Login Succesfully")
                else:
                    print("Incorrect Username or Password")

def acc_exist():
    global inp
    print("Account Already Exists!\n....")
    inp=input("Do you wanna login? Or wanna create a new Account? Or wanna go back?\n1. login\n2. new\n3. back\nChoose : ")

def user_employee():
    global choose
    choose = input("Choose your Occupation : \n--> 1. Customer\n--> 2. Employee\nChoose : ")
    if choose == '2' or choose == 'Employee' or choose == 'employee' or choose == 'EMPLOYEE':
        employee_login()
        time.sleep(0.8)
    else:
        old_new_user()
        time.sleep(0.8)

def employee_login():
    global emp_name
    global emp_password
    a=0
    if choose == '2' or choose == 'Employee' or choose == 'employee' or choose == 'EMPLOYEE':
        emp_name = input("Enter Your Name : ")
        emp_password = input("Enter Your Password : ")
        with open('employee_list.csv','r') as f:
            reader2 = csv.reader(f,delimiter=',')
            rownum2 = 0
            for row2 in reader2:        
                if row2 == [emp_name, emp_password]:
                    rownum2 = rownum2+1
                else:
                    continue
            if rownum2 == 1:
                print("Welcome Mr./Mrs. ",emp_name,"\nYour Attendece has been recorded.\n...")
                emp_work()
            else:
                print(f"Name --> {emp_name} with Password --> {emp_password} doesn't exist.")
                a=a+1
                if a==1:
                    print("Try Once more....\nRemember that this is your last chance, So enter carefully...\n...")
                    emp_name = input("Enter Your Name : ")
                    emp_password = input("Enter Your Password : ")
                    with open('employee_list.csv','r') as f:
                        reader2 = csv.reader(f,delimiter=',')
                        rownum2 = 0
                        for row2 in reader2:        
                            if row2 == [emp_name, emp_password]:
                                rownum2 = rownum2+1
                            else:
                                continue
                        if rownum2 == 1:
                            print("Welcome Mr./Mrs. ",emp_name,"\nYour Attendece has been recorded.\n...")
                            emp_work()
                        else:
                            print(f"Name --> {emp_name} with Password --> {emp_password} doesn't exist.")
                            print("You are not an Employee of PCB !!\nTurn Off your computer before I call the Police!!\n..\n...")

def emp_work():
    global emp_ask
    print(f"Mr./Mrs. {emp_name}, Choose your work :\n1. All Accounts \n2. Account Info \n3. back")
    emp_ask = input("Choose : ")
    if emp_ask == '2' or emp_ask == 'account info' or emp_ask == 'Account Info' or emp_ask == 'ACCOUNT INFO' or emp_ask == 'Account info':
        emp_ask_2()
    elif emp_ask == 'b' or emp_ask == 'B' or emp_ask == 'back' or emp_ask == 'Back' or emp_ask == 'BACK':
        employee_login()
    else:
        emp_ask_1()

def emp_ask_1():
    if emp_ask == '1' or emp_ask == 'all accounts' or emp_ask == 'All Accounts' or emp_ask == 'ALL ACCOUNTS':
        with open('acc_num.csv','r') as f:
            cust_acc = csv.reader(f,delimiter='-')
            print("These are all Registered Accounts : ")
            for row in cust_acc:
                print(row)
            ask = input("Do you want to proceed to 'Account Info'? (yes /no /back) : ")
            if ask=='y'or ask=='Y' or ask=='yes'or ask=='Yes'or ask=='YES':
                emp_ask_2()
            elif ask=='n'or ask=='N' or ask=='no'or ask=='No'or ask=='NO':
                print("..\nThanks for using this system.!\nYour work details has been Recorded and will be sent to Boss, Mr. SAURAV KUMAR")
            elif ask=='b'or ask=='B' or ask=='back'or ask=='Back'or ask=='BACK':
                print("Going back...\n...")
                emp_work()
            else:
                print("INVALID INPUT\n...Try Again...")
                emp_ask_1()
    else:
        print("INVALID INPUT\n...Try Again...\n...\n....")
        emp_work()

def emp_ask_2():
    ask_username = input("Enter Customer Username : ")
    ask_acc_num = input("Enter Account Number : ")
    with open('acc_num.csv','r') as f:
        reader5 = csv.reader(f,delimiter='-')
        rownum3 = 0
        for row3 in reader5:        
            if row3 == [ask_username,ask_acc_num]:
                rownum3 = rownum3+1
            else:
                continue
        if rownum3 == 1:
            with open(ask_username+'_employee.csv','r') as f:
                reader6 = csv.reader(f,delimiter=',')
                print(f"These are {ask_username}'s Information....")
                for row1 in reader6:
                    print(row1)
            with open(ask_acc_num+'.csv','r') as g:
                reader7 = csv.reader(g,delimiter=',')
                for row2 in reader7:
                    print(f"current Balance : ₹{row2}")
        else:
            print("---->>>>  ERROR!!!  <<<<----")
            print(f"Usename -- {ask_username} and Account number -- {ask_acc_num} Doesn't Exists!\n....")
            a=0
            while True:
                ent = input("1. Try again\n2. Back\nYour Choise? : ")
                if ent == '2' or ent == 'b' or ent == 'B' or ent == 'back' or ent == 'Back' or ent == 'BACK':
                    emp_work()
                elif ent == '1' or ent == 't' or ent == 'T' or ent == 'try again' or ent == 'Try again' or ent == 'Try Again' or ent == 'TRY AGAIN':
                    emp_ask_2()
                else:
                    print("INVALID INPUT\n...\nTry Again\n....")
                    a=a+1
                    if a==2:
                        print("No!! No more chances!")
                        break

def old_new_user():
    global acc
    if choose == '1' or choose == 'Customer' or choose == 'customer' or choose == 'CUSTOMER':
        naam = input("Please Enter Your Good Name Sir : ")
        time.sleep(1)
        print(f"Hello Mr. {naam}, WELCOME in 'PAISA CHORE BANK' '(PCB)'")
        acc = input("Do you have an account? (yes /no /back) : ")          # Asking user if  he have a account.
        if acc == 'yes' or acc == 'Yes' or acc == 'YES' or acc == 'y' or acc == 'Y':
            acc_yes()
        elif acc == 'back' or acc == 'Back' or acc == 'BACK' or acc == 'b' or acc == 'B':
            user_employee()
        else:
            acc_no()
        time.sleep(0.8)
    else:
        print("INVALID INPUT\nPlease choose correct options....\n..\n...\n....")
        time.sleep(2)
        user_employee()

def acc_yes():
    global yes1
    if acc == 'yes' or acc == 'Yes' or acc == 'YES' or acc == 'y' or acc == 'Y':
        yes1 = input("Do you want to login (yes / no): ")
        if yes1 == 'yes' or yes1 == 'Yes' or yes1 == 'YES' or yes1 == 'y' or yes1 == 'Y':
            login_system_yes()
        else:
            login_system_no()
        time.sleep(0.8)

def login_system_yes():
    if yes1 == 'yes' or yes1 == 'Yes' or yes1 == 'YES' or yes1 == 'y' or yes1 == 'Y':
        print("Fetching the Login System for you......")
        time.sleep(0.8)
        print("Please Wait......")
        time.sleep(1)
        login()

def login_system_no():
    if yes1 == 'no' or yes1 == 'No' or yes1 == 'NO' or yes1 == 'n' or yes1 == 'N':
        print("...")
        time.sleep(1)
        print("Then what are you here for?\nDon't waste your and my time.\nGo and study.\nIDIOT!!\n...")
    else:
        time.sleep(0.8)
        print("INVALID INPUT\nPlease choose correct options....\n..\n...\n....")
        time.sleep(2)
        acc_yes()

def acc_no():
    global yes2
    if acc == 'no' or acc == 'No' or acc == 'NO' or acc == 'n' or acc == 'N':
        yes2 = input("Do you want to Register sir? (yes / no) : ")
        if yes2 == 'yes' or yes2 == 'Yes' or yes2 == 'YES' or yes2 == 'y' or yes2 == 'Y':
            register_system_yes()
        else:
            register_system_no()
        time.sleep(0.8)
    else:
        print("INVALID INPUT\nPlease choose correct options....\n..\n...\n....")
        old_new_user()

def register_system_yes():
    if yes2 == 'yes' or yes2 == 'Yes' or yes2 == 'YES' or yes2 == 'y' or yes2 == 'Y':
        print("Fetching the Customer Registration System for you......")
        time.sleep(0.8)
        print("Please Wait......")
        time.sleep(1)
        register()
        time.sleep(1)
        login_want()

def register_system_no():
    if yes2 == 'no' or yes2 == 'No' or yes2 == 'NO' or yes2 == 'n' or yes2 == 'N':
        print("...")
        print("If You are not a customer and don't want to register then don't come.\nIDIOT!!\nEveryone now-a-days are useless people.\nHmph!\n..\n...")
    else:
        print("INVALID INPUT\nPlease choose correct options....\n..\n...\n....")
        acc_no()

def login_want():
    global olog
    olog = input("Do You Want To Login Now? (yes / no) : ")
    if olog == 'yes' or olog == 'Yes' or olog == 'YES' or olog == 'Y' or olog == 'y':
        login_want_yes()
    else:
        login_want_no()
    time.sleep(0.8)

def login_want_yes():
    if olog == 'yes' or olog == 'Yes' or olog == 'YES' or olog == 'Y' or olog == 'y':
        print("Fetching the Login System for you......")
        time.sleep(0.8)
        print("Please Wait......")
        time.sleep(1)
        login()

def login_want_no():
    if olog == 'no' or olog == 'No' or olog == 'NO' or olog == 'n' or olog == 'N':
        print("Thanks for registering in 'PAISA CHORE BANK' '(PCB)'")
    else:
        print("INVALID INPUT\nPlease choose correct options....\n..\n...\n....")
        login_want()

# OUTPUT CODE --->
user_employee()
