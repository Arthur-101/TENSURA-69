import csv
import time
import random
from datetime import date
from playsound import playsound

def hello():
    print("..\n...")
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    playsound('keyboard.mp3',block=False)
    print("HELLO!!")
    time.sleep(0.65)
    print("My name is SYLPHI ^_^")
    time.sleep(0.65)
    print("I am a banking bot of 'PAISA CHOR BANK' '(PCB)'")
    time.sleep(0.65)
    print("And I will be helping you with your work.")
    time.sleep(0.65)
    question=input("Should we start? (yes/no) : ")
    print("///////////////////////////////////////////////////////////////////////////////")
    if question=='yes'or question=='Yes'or question=='YES'or question=='y'or question=='Y':
        playsound('confirmation.wav',block=False)
        user_employee()
    elif question=='no'or question=='No'or question=='NO'or question=='n'or question=='N':
        exit()
    elif question=='time':
        Time=time.localtime()
        ctime=time.strftime("%H:%M:%S",Time)
        playsound('pop-alert.mp3',block=False)
        print("..\n...")
        print("Current time is -- ",ctime)
        time.sleep(1.4)
        hello()
    elif question=='date':
        today=date.today()
        playsound('pop-alert.mp3',block=False)
        print("..\n...")
        print("Today's date is -- ",today)
        time.sleep(1.4)
        hello()
    elif question=='epoch':
        playsound('pop-alert.mp3',block=False)
        print("..\n...")
        print("Epoch time is : ",time.time())
        time.sleep(1.4)
        hello()
    elif question=='your name?':
        playsound('pop-alert.mp3',block=False)
        print("Hi!!\nMy name is SYLPHI and i am a bot created by a group of Students.\nI will be taking your requests in this 'BANK SYSTEM'")
        time.sleep(4)
        hello()
    else:
        playsound('error-2.mp3',block=False)
        print("..\nINVALID INPUT\nTry again...")
        time.sleep(1.8)
        hello()

def user_employee():
    global choose
    print("..\n...")
    time.sleep(1.5)
    print("===============================================================================")
    choose = input("Choose your Occupation : \n--> 1. Customer\n--> 2. Employee\n--> 3. back\nChoose : ")
    print("===============================================================================")
    if choose == '1' or choose == 'Customer' or choose == 'customer' or choose == 'CUSTOMER':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        old_new_user()
    elif choose == '2' or choose == 'Employee' or choose == 'employee' or choose == 'EMPLOYEE':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        employee_login()
    elif choose == '3' or choose == 'Back' or choose == 'back' or choose == 'BACK' or choose=='b' or choose=='B':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        hello()
    else:
        playsound('error-2.mp3',block=False)
        print("..\nINVALID INPUT\nPlease choose correct options....")
        time.sleep(1.8)
        user_employee()

def old_new_user():
    global acc
    print("..\n...")
    time.sleep(1.5)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    naam = input("Please Enter Your Good Name Sir : ")
    time.sleep(1)
    print(f"Hello Mr./Mrs. {naam}, WELCOME in 'PAISA CHORE BANK' '(PCB)'")
    acc = input("Do you have an account? (yes /no /back) : ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if acc == 'yes' or acc == 'Yes' or acc == 'YES' or acc == 'y' or acc == 'Y':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        acc_yes()
    elif acc == 'no' or acc == 'No' or acc == 'NO' or acc == 'n' or acc == 'N':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        acc_no()
    elif acc == 'back' or acc == 'Back' or acc == 'BACK' or acc == 'b' or acc == 'B':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        user_employee()
    else:
        time.sleep(1.5)
        playsound('error-2.mp3',block=False)
        print("..\nINVALID INPUT\nPlease choose correct options....\n..")
        time.sleep(1.8)
        old_new_user()

def acc_yes():
    global yes1
    print("..\n...")
    time.sleep(1.5)
    yes1 = input("Do you want to login (yes/no/back/home): ")
    if yes1 == 'yes' or yes1 == 'Yes' or yes1 == 'YES' or yes1 == 'y' or yes1 == 'Y':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        login_system_yes()
    elif yes1 == 'no' or yes1 == 'No' or yes1 == 'NO' or yes1 == 'n' or yes1 == 'N':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        login_system_no()
    elif yes1 == 'back' or yes1 == 'Back' or yes1 == 'BACK' or yes1 == 'b' or yes1 == 'B':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        old_new_user()
    elif yes1 == 'home' or yes1 == 'Home' or yes1 == 'HOME' or yes1 == 'h' or yes1 == 'H':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        hello()
    else:
        time.sleep(1.5)
        playsound('error-2.mp3',block=False)
        print("..\nINVALID INPUT\nPlease choose correct options....\n..")
        time.sleep(1.8)
        acc_yes()

def login_system_yes():
    print("..\n...")
    time.sleep(1.5)
    print("Fetching the Login System for you......")
    time.sleep(1)
    print("Please Wait......")
    time.sleep(1)
    playsound('pop-alert.mp3',block=False)
    login()

def login():
    global usernamelog
    time.sleep(1)
    print("..\n...")
    time.sleep(1)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    playsound('pop-alert.mp3',block=False)
    print(" \n                  LOGIN HERE\n ")
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
            playsound('confirmation.wav',block=False)
            print("..\n                  LOGIN SUCCSESSFULY\n..")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            playsound('pop-alert.mp3',block=False)
            after_login()
        else:
            playsound('error-1.mp3',block=False)
            print("..\nIncorrect Username or Password\nTry one more Time....\n...")
            time.sleep(1.8)
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
                    playsound('confirmation.wav',block=False)
                    print("..\n                  LOGIN SUCCSESSFULY\n..")
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    playsound('pop-alert.mp3',block=False)
                    after_login()
                else:
                    playsound('error-2.mp3',block=False)
                    print("..\nINVALID INPUT\nPlease choose correct options....\n..")
                    time.sleep(1.8)
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def after_login():
    print("..\n...")
    time.sleep(1.5)
    what=input("What do you wanna do next?\n1. profile\n2. home\n3. exit\nChoose : ")
    if what=='1'or what=='profile'or what=='Profile'or what=='PROFILE':
        playsound('pop-alert.mp3',block=False)
        cust_profile()
    elif what=='2'or what=='home'or what=='Home'or what=='HOME'or what=='h'or what=='H':
        playsound('pop-alert.mp3',block=False)
        hello()
    elif what=='3'or what=='exit'or what=='Exit'or what=='EXIT'or what=='e'or what=='E':
        playsound('pop-alert.mp3',block=False)
        thankyou()
    else:
        playsound('error-2.mp3',block=False)
        print("..\nINVALID INPUT\nPlease choose correct options....\n..")
        time.sleep(1.8)
        after_login()

def cust_profile():
    global mo
    global acc_no
    print("..\n...")
    time.sleep(1.5)
    print("Fetching your User Profile for you...\nPlease wait...\n...")
    time.sleep(2)
    print(f"These are {usernamelog}'s Information....")
    with open(usernamelog+'_customer.csv','r') as a:
        reader = csv.reader(a,delimiter=',')
        array1=[]
        for row in reader:
            array1.append(row)
            print(row)
        acc_no=str(array1[0])
        with open(acc_no+'.csv','r') as a:
            reader1 = csv.reader(a)
            for row1 in reader1:
                for i in row1:
                    mo=float(i[0:16])
                    print(f" \nYour Current Account Balance is ₹{mo}")
        time.sleep(4)
        playsound('pop-alert.mp3',block=False)
        add_diff()

def add_diff():
    print("..\n...")
    time.sleep(1.5)
    what=input("What do you wanna do next?\n1. add money\n2. withdraw\n3. loan\n4. home\n5. exit\nChoose : ")
    if what=='1'or what=='add money'or what=='Add money'or what=='Add Money'or what=='ADD MONEY'or what=='add'or what=='Add'or what=='a'or what=='A':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        money_add()
    elif what=='2'or what=='withdraw'or what=='Withdraw'or what=='WITHDRAW'or what=='w'or what=='W':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        money_diff()
    elif  what=='3'or what=='loan'or what=='Loan'or what=='LOAN'or what=='l'or what=='L':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        loan()
    elif  what=='4'or what=='home'or what=='Home'or what=='HOME'or what=='h'or what=='H':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        hello()
    elif what=='5'or what=='exit'or what=='Exit'or what=='EXIT'or what=='e'or what=='E':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        thankyou()
    else:
        playsound('error-2.mp3',block=False)
        print("..\nINVALID INPUT\nPlease choose correct options....\n..")
        time.sleep(1.8)
        add_diff()

def money_add():
    global mo
    print("..\n...")
    time.sleep(1)
    print("Getting Your Account Ready....\n...")
    time.sleep(1.5)
    print(f"Your Current Account Balance is ₹{mo}\n ")
    mo2 = float(input("Enter the Amount you want to ADD (in ₹) : "))
    new_mo = mo+mo2
    array2=[]
    with open(acc_no+'.csv','r') as a:
        reader2 = csv.reader(a)
        for row1 in reader2:
            array2.append(row1)
            array2.remove(row1)
            array2.append(str(new_mo))
    with open(acc_no+'.csv','w') as writefile:
        writer = csv.writer(writefile)
        writer.writerow(array2)
    with open(acc_no+'.csv','r') as a:
        reader1 = csv.reader(a)
        for row1 in reader1:
            for i in row1:
                mo=float(i[0:16])
    time.sleep(2.5)
    playsound('confirmation.wav',block=False)
    print(f" \nYour New Current Account Balance is ₹{mo}")
    time.sleep(3)
    playsound('pop-alert.mp3',block=False)
    add_diff()

def money_diff():
    global mo
    print("..\n...")
    time.sleep(1)
    print("Getting Your Account Ready....\n...")
    time.sleep(1.5)
    print(f"Your Current Account Balance is ₹{mo}\n ")
    mo2 = float(input("Enter the Amount you want to WITHDRAW (in ₹) : "))
    new_mo = mo-mo2
    array2=[]
    with open(acc_no+'.csv','r') as a:
        reader2 = csv.reader(a)
        for row1 in reader2:
            array2.append(row1)
            array2.remove(row1)
            array2.append(str(new_mo))
    with open(acc_no+'.csv','w') as writefile:
        writer = csv.writer(writefile)
        writer.writerow(array2)
    with open(acc_no+'.csv','r') as a:
        reader1 = csv.reader(a)
        for row1 in reader1:
            for i in row1:
                mo=float(i[0:16])
    time.sleep(1.5)
    playsound('confirmation.wav',block=False)
    print(f" \nYour New Current Account Balance is ₹{mo}")
    time.sleep(3)
    playsound('pop-alert.mp3',block=False)
    add_diff()

def loan():
    global mo
    print(f"..\n...\nGetting Your Account Ready....\n...\nYour Current Account Balance is ₹{mo}")
    print(" \nThe Loan rate in our bank (PCB) is 9% per annum.") 
    loa=float(input(" \nEnter the Loan amount you want to take (in ₹) : "))
    t_mo=mo+loa
    tim=int(input("Enter time (in months) : "))
    interest=(loa*9*tim)/1200
    loan=loa+interest
    ran_num=str(random.randint(1111,10000))
    ran_str=random.choice(['JfyYiD','KdiFHc','SRkhsD','OUesxO','qGfrsP','Mbcnxv','AhauPV','reHFka','lfgdZY','adsUTy','ZxpoyH','hkHdLa','YRfgxy'])
    cache=ran_str+ran_num
    n_bot=input(" \n       LAST VERIFICATION CHECK\n       Type this -> "+cache+'\n       Your answer : ')
    if n_bot==cache:
        playsound('confirmation.wav',block=False)
        print(f" \n       VERIFICATION SUCCESSFUL\n \nYour Interest amount is ₹{interest}\nYou have to return ₹{loan} after {tim} months.")
        time.sleep(2.5)
        array2=[]
        with open(acc_no+'.csv','r') as a:
            reader2 = csv.reader(a)
            for row1 in reader2:
                array2.append(row1)
                array2.remove(row1)
                array2.append(str(t_mo))
        with open(acc_no+'.csv','w') as writefile:
            writer = csv.writer(writefile)
            writer.writerow(array2)
        with open(acc_no+'.csv','r') as a:
            reader1 = csv.reader(a)
            for row1 in reader1:
                for i in row1:
                    mo=float(i[0:16])
        playsound('confirmation.wav',block=False)
        print(f" \nYour New Current Account Balance is ₹{mo}\n..")
        time.sleep(3)
        playsound('pop-alert.mp3',block=False)
        add_diff()
    else:
        playsound('error-1.mp3',block=False)
        print(" \n       VERIFICATION FAILED....\n       Try again..\n...")
        time.sleep(1)
        add_diff()

def login_system_no():
    print("..\n...")
    time.sleep(1)
    playsound('pop-alert.mp3',block=False)
    print("Then what are you here for?\nDon't waste your and my time.\nGo and study.\nIDIOT!!\n...")

def acc_no():
    global yes2
    print("..\n...")
    time.sleep(1.5)
    yes2 = input("Do you want to Register sir? (yes/no/back/home/exit) : ")
    if yes2 == 'yes' or yes2 == 'Yes' or yes2 == 'YES' or yes2 == 'y' or yes2 == 'Y':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        register_system_yes()
    elif yes2 == 'no' or yes2 == 'No' or yes2 == 'NO' or yes2 == 'n' or yes2 == 'N':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        register_system_no()
    elif yes2 == 'back' or yes2 == 'Back' or yes2 == 'BACK' or yes2 == 'b' or yes2 == 'B':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        old_new_user()
    elif yes2 == 'home' or yes2 == 'Home' or yes2 == 'HOME' or yes2 == 'h' or yes2 == 'H':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        hello()
    elif yes2 == 'exit' or yes2 == 'Exit' or yes2 == 'EXIT' or yes2 == 'e' or yes2 == 'E':
        time.sleep(1)
        playsound('pop-alert.mp3',block=False)
        exit()
    else:
        playsound('error-2.mp3',block=False)
        print("..\nINVALID INPUT\nPlease choose correct options....\n..")
        time.sleep(1.8)
        acc_no()

def register_system_yes():
    print("..\n...")
    time.sleep(1)
    print("Fetching the Customer Registration System for you......")
    time.sleep(1)
    print("Please Wait......")
    time.sleep(2)
    playsound('pop-alert.mp3',block=False)
    register()
    time.sleep(2)
    playsound('pop-alert.mp3',block=False)
    login_want()

def register():
    global username
    global password
    global address
    print("..\n...")
    time.sleep(1.5)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    playsound('pop-alert.mp3',block=False)
    print(" \n                       REGISTER HERE\n ")
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
                    playsound('pop-alert.mp3',block=False)
                    login()
                elif inp == '2' or inp == 'new' or inp == 'New' or inp == 'NEW':
                    playsound('pop-alert.mp3',block=False)
                    register()
                elif inp == '3' or inp == 'b' or inp == 'B' or inp == 'back' or inp == 'Back' or inp == 'BACK':
                    playsound('pop-alert.mp3',block=False)
                    user_employee()
                elif inp == '4' or inp == 'e' or inp == 'E' or inp == 'exit' or inp == 'Exit' or inp == 'EXIT':
                    playsound('pop-alert.mp3',block=False)
                    exit()
                else:
                    playsound('error-2.mp3',block=False)
                    print("..\nINVALID INPUT\nPlease choose correct options....\n..")
                    time.sleep(1.8)
                    acc_exist()
            else:
                if password == passwordc:
                    address = input("Enter Your Adderess : ")
                    random_num()
                    writer.writerow([username,password])
                    playsound('confirmation.wav',block=False)
                    time.sleep(2)
                    print(" \n                    REGISTRATION SUCCESSFUL!!\n ")
                    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                    time.sleep(3)
                else:
                    playsound('error-1.mp3',block=False)
                    print("Passwords don't match\nTRY AGAIN !!\n..")
                    time.sleep(1)
                    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                    register()

def random_num():
    global r1
    r1 = str(random.randint(12345678,87654321))
    acc_num()

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
    with open("['"+r1+"'].csv",'w') as l:
        writer5 = csv.writer(l)
        first_money = input("How much money do you want to add for the first time? (in ₹) : ")
        writer5.writerow([first_money])

def acc_exist():
    global inp
    print("..\n...")
    time.sleep(2)
    playsound('wrong-answer.mp3',block=False)
    print("Account Already Exists!\n....")
    time.sleep(1.5)
    inp=input("Do you wanna login? Or wanna create a new Account? Or wanna go back?\n1. login\n2. new\n3. back\n4. exit\nChoose : ")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

def login_want():
    global olog
    print("..\n...")
    time.sleep(1.5)
    olog = input("Do You Want To Login Now? (yes/no/home/exit) : ")
    if olog == 'yes' or olog == 'Yes' or olog == 'YES' or olog == 'Y' or olog == 'y':
        playsound('pop-alert.mp3',block=False)
        login_want_yes()
    elif olog == 'no' or olog == 'No' or olog == 'NO' or olog == 'N' or olog == 'n':
        playsound('pop-alert.mp3',block=False)
        login_want_no()
    elif olog == 'home' or olog == 'Home' or olog == 'HOME' or olog == 'H' or olog == 'h':
        playsound('pop-alert.mp3',block=False)
        hello()
    elif olog == 'exit' or olog == 'Exit' or olog == 'EXIT' or olog == 'E' or olog == 'e':
        playsound('pop-alert.mp3',block=False)
        exit()
    else:
        playsound('error-2.mp3',block=False)
        print("..\nINVALID INPUT\nPlease choose correct options....\n..")
        time.sleep(1.8)
        login_want()

def login_want_yes():
    print("..\n...")
    time.sleep(1)
    print("Fetching the Login System for you......")
    time.sleep(1)
    print("Please Wait......")
    time.sleep(1)
    playsound('pop-alert.mp3',block=False)
    login()

def login_want_no():
    print("..\n...")
    time.sleep(1)
    print("Thanks for registering in 'PAISA CHORE BANK' '(PCB)'")
    time.sleep(1)
    playsound('pop-alert.mp3',block=False)
    exit()

def register_system_no():
    print("..\n...")
    time.sleep(1.5)
    playsound('pop-alert.mp3',block=False)
    print("If You are not a customer and don't want to register then don't come.\nIDIOT!!\nEveryone now-a-days are useless people.\nHmph!\n..\n...")
    time.sleep(1)

def employee_login():
    global emp_name
    global emp_password
    print("..\n...")
    time.sleep(2)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    a=0
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
            playsound('confirmation.wav',block=False)
            print("Welcome Mr./Mrs. ",emp_name,"\nYour Attendece has been recorded.\n...")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            time.sleep(1)
            emp_work()
        else:
            playsound('wrong-answer.mp3',block=False)
            print(f"Name --> {emp_name} with Password --> {emp_password} doesn't exist.")
            time.sleep(1)
            a=a+1
            if a==1:
                time.sleep(2)
                print("Try Once more....\nRemember that this is your last chance, So enter carefully...\n...")
                time.sleep(1)
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
                        playsound('confirmation.wav',block=False)
                        print("Welcome Mr./Mrs. ",emp_name,"\nYour Attendece has been recorded.\n...")
                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        time.sleep(1.5)
                        emp_work()
                    else:
                        playsound('wrong-answer.mp3',block=False)
                        print(f"Name --> {emp_name} with Password --> {emp_password} doesn't exist.")
                        time.sleep(1)
                        print("You are not an Employee of PCB !!\nTurn Off your computer before I call the Police!!\n..\n...")
                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        time.sleep(1)

def emp_work():
    global emp_ask
    print("..\n...")
    time.sleep(1.5)
    print(f"Mr./Mrs. {emp_name}, Choose your work :\n1. All Accounts \n2. Account Info \n3. back")
    emp_ask = input("Choose : ")
    if emp_ask=='1'or emp_ask=='all accounts'or emp_ask=='All Accounts'or emp_ask=='ALL ACCOUNTS'or emp_ask=='All accounts':
        playsound('pop-alert.mp3',block=False)
        emp_ask_1()
    elif emp_ask =='2'or emp_ask=='account info'or emp_ask=='Account Info'or emp_ask=='ACCOUNT INFO'or emp_ask=='Account info':
        playsound('pop-alert.mp3',block=False)
        emp_ask_2()
    elif emp_ask == 'b' or emp_ask == 'B' or emp_ask == 'back' or emp_ask == 'Back' or emp_ask == 'BACK':
        playsound('pop-alert.mp3',block=False)
        user_employee()
    elif emp_ask == 'e' or emp_ask == 'E' or emp_ask == 'exit' or emp_ask == 'Exit' or emp_ask == 'EXIT':
        playsound('pop-alert.mp3',block=False)
        exit()
    else:
        playsound('error-2.mp3',block=False)
        print("..\nINVALID INPUT\nPlease choose correct options....\n..")
        time.sleep(1.8)
        emp_work()

def emp_ask_1():
    print("..\n...")
    time.sleep(1.5)
    print("*******************************************************************************")
    with open('acc_num.csv','r') as f:
        cust_acc = csv.reader(f,delimiter='-')
        print("These are all Registered Accounts : ")
        for row in cust_acc:
            print(row)
        time.sleep(4)
        ask = input("Do you want to proceed to 'Account Info'? (yes/no/back/home/exit) : ")
        print("*******************************************************************************")
        if ask=='y'or ask=='Y' or ask=='yes'or ask=='Yes'or ask=='YES':
            emp_ask_2()
        elif ask=='n'or ask=='N' or ask=='no'or ask=='No'or ask=='NO':
            print("Your work details has been Recorded and will be sent to Boss, Mr. SAURAV KUMAR")
            playsound('pop-alert.mp3',block=False)
            emp_work()
        elif ask=='b'or ask=='B' or ask=='back'or ask=='Back'or ask=='BACK':
            playsound('pop-alert.mp3',block=False)
            emp_work()
        elif ask=='b'or ask=='B' or ask=='back'or ask=='Back'or ask=='BACK':
            playsound('pop-alert.mp3',block=False)
            hello()
        elif ask=='e'or ask=='E' or ask=='exit'or ask=='Exit'or ask=='EXIT':
            playsound('pop-alert.mp3',block=False)
            exit()
        else:
            playsound('error-2.mp3',block=False)
            print("..\nINVALID INPUT\nTry again....\n..")
            time.sleep(1.8)
            emp_ask_1()

def emp_ask_2():
    print("..\n...")
    time.sleep(1.5)
    print("-------------------------------------------------------------------------------")
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
            time.sleep(2.5)
            with open("['"+ask_acc_num+"'].csv",'r') as g:
                reader7 = csv.reader(g)
                for row2 in reader7:
                    for i in row2:
                        mon=float(i[0:16])
            print(f"current Balance : ₹{mon}")
            print("-------------------------------------------------------------------------------")
            time.sleep(4)
            playsound('pop-alert.mp3',block=False)
            emp_work()
        else:
            playsound('error-1.mp3',block=False)
            print("---->>>>  ERROR!!!  <<<<----")
            time.sleep(1.5)
            print(f"Usename -- {ask_username} and Account number -- {ask_acc_num} Doesn't Exists!\n....")
            print("-------------------------------------------------------------------------------")
            a=0
            while True:
                ent = input("1. Try again\n2. Back\nYour Choise? : ")
                if ent == '2' or ent == 'b' or ent == 'B' or ent == 'back' or ent == 'Back' or ent == 'BACK':
                    playsound('pop-alert.mp3',block=False)
                    emp_work()
                elif ent == '1' or ent == 't' or ent == 'T' or ent == 'try again' or ent == 'Try again' or ent == 'Try Again' or ent == 'TRY AGAIN':
                    playsound('pop-alert.mp3',block=False)
                    emp_ask_2()
                else:
                    playsound('error-2.mp3',block=False)
                    print("..\nINVALID INPUT\nPlease choose correct options....\n..")
                    time.sleep(1.8)
                    a=a+1
                    if a==2:
                        print("No!! No more chances!")
                        break

def thankyou():
    time.sleep(1.2)
    print("..\n...\n....")
    time.sleep(1.5)
    playsound('keyboard.mp3',block=False)
    print("THANK YOU for visiting 'PAISA CHORE BANK' 'PCB'")
    time.sleep(0.8)
    print("We will bw seeing you soon (Since your money is stored here 😏)")
    time.sleep(1)
    print("..\n...")

def exit():
    time.sleep(1.2)
    print(".\n..\n...")
    time.sleep(1.5)
    playsound('keyboard.mp3',block=False)
    print("THANKS FOR VISITING 'PAISA CHOR BANK' 'PCB'.")
    time.sleep(0.8)
    print("We hope to see you soon.")
    time.sleep(0.8)
    print("SYLPHI says Bye-Bye!")
    time.sleep(1)
    print("..\n...")

# OUTPUT CODE --->
hello()
