import csv
import string
import random
import pyttsx3 as ps
from playsound import playsound
from datetime import date,datetime
from time import *
from customtkinter import *

# TODO:- Make 'Toplevel Message' for Money Withdraw, Deposit, and Loan.
# TODO:- Make 'Employee Window'
# TODO:- Add keyboard 'Enter' button in 'Main Window' to enter.

def change_appearance_mode_event(new_appearance_mode: str):
    set_appearance_mode(new_appearance_mode)

def t_time():
    global Ctime
    Time=localtime()
    Ctime=str(strftime("%H:%M:%S",Time))
    if '3:30:00' < Ctime < '12:00:00' :
        greet = 'Good Morning'
    elif '12:00:00' < Ctime < '16:00:00':
        greet = 'Good Afternoon'
    elif '16:00:00' < Ctime < '19:00:00':
        greet = 'Good Evening'
    else:
        greet = 'Good Night'
    return greet

# Enter Command
def enter():
    root1.iconbitmap('Files/Items/bot_happy.ico')
    command = entry1.get()
    command1 = command.lower()

    textbox2.configure(state="normal")
    textbox2.delete("0.0",END)
    textbox2.insert("0.0",command)
    textbox2.configure(state="disabled")
    textbox3.configure(state="normal")
    textbox3.delete("0.0",END)

    if command1 in ['help','/help']:
        playsound('Files/Items/pop-alert.mp3',block=False)
        textbox3.insert("0.0","/time, /date, /date time, /epoch, /your name,\n/calc <equation>, /cls, /help, /exit,\n/say <words>, /greet me, /my name is <name>")

    elif command1 == '/hi' or command1 == '/hello':
        root1.iconbitmap('Files/Items/bot_audio.ico')
        a = ['Hii!','Hello!','Hello there!','Hi. Who are you anyway?','Hii! But, do i know you?','Hii! Nice to meet you',"Hello! What's your name?"]
        gr = random.choice(a)
        textbox3.insert("0.0",gr)
        engine.say(gr)
        engine.runAndWait()

    elif command1 == f'/hey {BOT.lower()}':
        root1.iconbitmap('Files/Items/bot_audio.ico')
        textbox3.insert("0.0",f"Yes! {BOT} is here.\nWhat can i help you with?\nType in '/help' to see all the commands.")
        engine.say(f"Yes! {BOT} is here.\nWhat can i help you with?\nType in '/help' to see all the commands.")
        engine.runAndWait()

    elif command1 == '/start':
        start()

    elif command1 == '/time':
        playsound('Files/Items/pop-alert.mp3',block=False)
        Time=localtime()
        ctime=strftime("%H:%M:%S",Time)
        textbox3.insert("0.0",f"Current time is : \n{ctime}")

    elif command1 == '/date':
        playsound('Files/Items/pop-alert.mp3',block=False)
        textbox3.insert("0.0",f"Today's Date is : \n{date.today()}")

    elif command1 in ['/datetime','/date time','/date_time']:
        playsound('Files/Items/pop-alert.mp3',block=False)
        textbox3.insert("0.0",f"Current Date and Time is : \n{datetime.now()}")

    elif command1 == '/epoch':
        playsound('Files/Items/pop-alert.mp3',block=False)
        textbox3.insert("0.0",f"Current Epoch is : \n{time()}")

    elif command1 in ['/your name','/your_name']:
        root1.iconbitmap('Files/Items/bot_audio.ico')
        textbox3.insert("0.0",f"Hi!!\nMy name is {BOT} and i am a bot created by a group of Students for a school project.")
        engine.say(f"Hi!!\nMy name is {BOT} and i am a bot created by a group of Students for a school Project.")
        engine.runAndWait()

    elif '/calc ' in command1:
        playsound('Files/Items/pop-alert.mp3',block=False)
        quest = command1.replace('/calc ','')

        try:
            ans=eval(quest)
            if isinstance(ans,int) or isinstance(ans,float):
                textbox3.insert("0.0",ans)
            else:
                root1.iconbitmap('Files/Items/bot_warning.ico')
                playsound('Files/Items/error-2.mp3',block=False)
                textbox3.insert("0.0","ERROR!!")
        except:
            root1.iconbitmap('Files/Items/bot_warning.ico')
            playsound('Files/Items/error-2.mp3',block=False)
            textbox3.insert("0.0","ERROR!!")

    elif command1 == '/cls':
        playsound('Files/Items/confirmation.wav',block=False)
        textbox3.insert("0.0","<Answer>")

    elif '/say' in command1:
        root1.iconbitmap('Files/Items/bot_audio.ico')
        speak = command1.replace('/say','')
        textbox3.insert("0.0",speak)
        engine.say(". . . . "+speak)
        engine.runAndWait()

    elif '/my name is' in command1:
        global NAME
        root1.iconbitmap('Files/Items/bot_audio.ico')
        NAME0 = command1.replace('/my name is','')
        NAME = NAME0.upper()
        textbox3.insert("0.0",f"Hello {NAME}! My Name is {BOT}.\nNice to meet you.")
        engine.say(f". . Hello  {NAME}! My Name is {BOT}.\nNice to meet you.")
        engine.runAndWait()

    elif command1 == '/greet me':
        root1.iconbitmap('Files/Items/bot_audio.ico')
        textbox3.insert("0.0",f"{t_time()} {NAME}.")
        engine.say(f"{t_time()} {NAME}.")
        engine.runAndWait()

    elif command1 == '/exit':
        root1.destroy()

    else:
        root1.iconbitmap('Files/Items/bot_warning.ico')
        playsound('Files/Items/error-2.mp3',block=False)
        textbox3.insert("0.0","COMMAND doesn't exist!\nMaybe you typed wrong command or\nforgot to put '\\' before command\nTry '/help'")

    textbox3.configure(state="disabled")

def start():
    second_window()

def main():
    main_window()

def okay():
    try:
        toplevel1.destroy()
    except:
        pass
    try:
        toplevel2.destroy()
    except:
        pass
    try:
        toplevel3.destroy()
    except:
        pass
    toplevel_messages.destroy()

def try_again():
    toplevel_messages.destroy()

def rcache():
    global cache1
    global cache
    cache0 = ''.join(random.choices(string.digits+string.ascii_letters,k=8))
    cache1 = cache0

    for i in range(6):
        r1 = random.choice(range(8))
        r2 = random.choice(['-','*','^','+','?'])
        cache0 = cache0[:r1] + r2 + cache0[r1:]
        r1 += 1
    cache = cache0

def email_check(event):
    check = entry_rgmail.get()
    if '@gmail.com'in check or'@mail.com'in check or'@outlook.com'in check or'@yahoo.com'in check or'@icloud.com'in check or'@fastmail.com'in check:
        entry_rgmail.configure(border_color='#3f60fc')
        label_error.configure(text='Valid Gmail',text_color='#26c115')
    else:
        entry_rgmail.configure(border_color='#f8182f')
        label_error.configure(text='Invalid Gmail',text_color='#f8182f')

def empty_entry(event):
    if entry_rusername.get().strip()!="" and entry_rpassword1.get().strip()!="" and entry_rgmail.get().strip()!="":
        button_register.configure(state='normal')
    else:
        button_register.configure(state='disabled')

def cache_start():
    rcache()
    toplevel_register_money()

def rcache_check():
    check_cache = entry_clear_cache.get()
    if check_cache == cache1:
        with open('Files/#users.csv','a',newline='') as f:
            writer_a = csv.writer(f,delimiter=',')
            writer_a.writerow([rusername,rpassword])
        with open('Files/#usernames.csv','a',newline='') as g:
            writer_b = csv.writer(g)
            writer_b.writerow([rusername])
        with open('Files/#users@.csv','a',newline='') as g:
            writer1 = csv.writer(g,delimiter=',')
            writer1.writerow([rusername,rpassword,rgmail])
        acc_num()
        playsound('Files/Items/confirmation.wav',block=False)
        toplevel2.destroy()
        toplevel_message(register_success,off,ok,"bot_smile")
        try:
            toplevel4.destroy()
        except:
            pass
    else:
        cache_start()

def toplevel_message(message,b_state,main_button,icon):
    global toplevel_messages

    toplevel_messages = CTkToplevel()
    toplevel_messages.title('Message')
    toplevel_messages.iconbitmap('Files/Items/'+icon+'.ico')
    toplevel_messages.geometry(f"{350}x{180}")
    toplevel_messages.minsize(350,180)
    toplevel_messages.maxsize(350,180)

    label_message = CTkLabel(master=toplevel_messages,text=message,font=('Roboto',18,))
    label_message.grid(row=0,column=0,columnspan=2,padx=20,pady=(20,5),sticky='s')

    button_ok = CTkButton(master=toplevel_messages,text=main_button,border_width=3,corner_radius=15,
        border_color='#3f60fc',command=okay)
    button_ok.grid(row=1,column=0,padx=(20,10),pady=10)

    button_tryagain = CTkButton(master=toplevel_messages,text='Try Again',state=b_state,border_width=3,corner_radius=15,
        border_color='#3f60fc',command=try_again)
    button_tryagain.grid(row=1,column=1,padx=(10,20),pady=10)

def pass_switch(to_switch):
    on_off = to_switch.get()
    if to_switch == switch_lpassword:
        if on_off == 1:
            entry_lpassword.configure(show='')
        elif on_off == 0:
            entry_lpassword.configure(show='*')
    elif to_switch == switch_rpassword1:
        if on_off == 1:
            entry_rpassword1.configure(show='')
        elif on_off == 0:
            entry_rpassword1.configure(show='*')
    elif to_switch == switch_rpassword2:
        if on_off == 1:
            entry_rpassword2.configure(show='')
        elif on_off == 0:
            entry_rpassword2.configure(show='*')
    elif to_switch == switch_epassword:
        if on_off == 1:
            entry_epassword.configure(show='')
        elif on_off == 0:
            entry_epassword.configure(show='*')

def register_system():
    global rusername
    global rpassword
    global rgmail
    with open('Files/#users.csv','a',newline='') as f:
        writer_a = csv.writer(f,delimiter=',')
        rusername = entry_rusername.get()
        rpassword = entry_rpassword1.get()
        rpasswordc = entry_rpassword2.get()
        rgmail = entry_rgmail.get()
        username_exist = f"'{rusername}'\nThis username is already taken.\nUse another username."
        with open('Files/#usernames.csv','a',newline='') as g:
            writer_b = csv.writer(g)
            with open('Files/#users.csv','r') as f:
                reader = csv.reader(f,delimiter=',')
                rownum = 0
                for row in reader:
                    if row == [rusername, rpassword]:
                        rownum = rownum+1
                    else:
                        continue
                if rownum == 1:
                    toplevel_message(acc_exist,on,back,"bot_warning")
                else:
                    with open('Files/#usernames.csv','r') as g:
                        reader2 = csv.reader(g,delimiter=',')
                        rownum2 = 0
                        for row2 in reader2:
                            if row2 == [rusername]:
                                rownum2 = rownum2+1
                            else:
                                continue
                        if rownum2 == 1:
                            toplevel_message(username_exist,on,back,"bot_warning")
                        else:                    
                            if rpassword == rpasswordc:
                                check = entry_rgmail.get()
                                if '@gmail.com'in check or'@mail.com'in check or'@outlook.com'in check or'@yahoo.com'in check or'@icloud.com'in check or'@fastmail.com'in check:
                                    cache_start()
                                else:
                                    toplevel_message(invalid_email,on,back,"bot_error")
                            else:
                                toplevel_message(wrong_password,on,back,"bot_error")

def acc_num():
    deposit = entry_add_money.get()
    r1 = str(random.randint(12345678,87654321))
    with open('Files/#acc_num.csv','a',newline='') as k:
        writer2 = csv.writer(k,delimiter='-')
        with open('Files/#acc_num.csv','r') as f:
            reader2 = csv.reader(f,delimiter='-')
            rownum2 = 0
            for row2 in reader2:        
                if row2 == [r1]:
                    rownum2 = rownum2+1
                else:
                    continue
            if rownum2 == 1:
                acc_num()
            else:
                writer2.writerow([rusername,r1])
                with open('Files/'+r1+'.csv','a',newline='') as l:
                    writer_c = csv.writer(l,delimiter=',')
                    writer_c.writerow([deposit])
                with open("Files/"+rusername+'_customer.csv','a',newline='') as m:
                    writer3 = csv.writer(m,delimiter=',')
                    writer3.writerow([r1])
                    writer3.writerow([rusername])
                    writer3.writerow([rpassword])
                    writer3.writerow([rgmail])
                with open("Files/"+rusername+'_employee.csv','a',newline='') as n:
                    writer4 = csv.writer(n,delimiter=',')
                    writer4.writerow([r1])
                    writer4.writerow([rusername])
                    writer4.writerow([rgmail])

def login_system():
    global usernamelog
    
    usernamelog = entry_lusername.get()
    passwordlog = entry_lpassword.get()
    with open('Files/#users.csv','r') as f:
        reader = csv.reader(f,delimiter=',')
        rownum = 0
        for row in reader:        
            if row == [usernamelog.strip(), passwordlog.strip()]:
                rownum = rownum+1
            else:
                continue
        if rownum == 1:
            playsound('Files/Items/confirmation.wav',block=False)
            profile_after_login_system()
            # toplevel_message(login_success,off,ok,"bot_smile")
        else:
            toplevel_message(acc_not_exist,on,back,"bot_warning")

def profile_after_login_system():
    global user_info
    global user_money
    global acc_no_open

    with open('Files/'+usernamelog.strip()+'_employee.csv','r') as a:
        reader = csv.reader(a,delimiter=',')
        customer_info=[]
        for row in reader:
            cu = customer_info.append(row)
        item_no=0
        item_row=''
        for item in customer_info:
            if item_no<3:
                cu0 = str(customer_info[item_no])
                cu1 = cu0.replace("['",'')
                cu2 = cu1.replace("']",'')
                item_row += cu2+'\n\n'
                item_no += 1
        user_info = item_row.strip()
        acc_no_0=str(customer_info[0])
        acc_no_1 = acc_no_0.replace("['",'')
        acc_no_open = acc_no_1.replace("']",'')
        with open('Files/'+acc_no_open+'.csv','r') as a:
            reader1 = csv.reader(a)
            for row1 in reader1:
                for i in row1:
                    user_money=float(i[0:16])
    after_login_window()

def profile_after_login_system_2():
    global user_info_2
    global user_money_old
    global acc_no_open_2

    with open('Files/'+usernamelog.strip()+'_employee.csv','r') as a:
        reader = csv.reader(a,delimiter=',')
        customer_info=[]
        for row in reader:
            cu = customer_info.append(row)
        item_no=0
        item_row=''
        for item in customer_info:
            if item_no<3:
                cu0 = str(customer_info[item_no])
                cu1 = cu0.replace("['",'')
                cu2 = cu1.replace("']",'')
                item_row += cu2+'\n\n'
                item_no += 1
        user_info_2 = item_row.strip()
        acc_no_0=str(customer_info[0])
        acc_no_1 = acc_no_0.replace("['",'')
        acc_no_open_2 = acc_no_1.replace("']",'')
        with open('Files/'+acc_no_open_2+'.csv','r') as a:
            reader1 = csv.reader(a)
            for row1 in reader1:
                for i in row1:
                    user_money_old=float(i[0:16])

def withdraw_money_system():
    profile_after_login_system_2()
    money_add = tabview2_entry1.get()
    tabview2_entry1.delete(0,END)
    new_money = user_money_old - float(money_add)
    file_money = []
    with open('Files/'+acc_no_open_2+'.csv','r') as a:
        reader1 = csv.reader(a)
        for row1 in reader1:
            file_money.append(row1)
            file_money.remove(row1)
            file_money.append(str(new_money))
    with open('Files/'+acc_no_open_2+'.csv','w') as b:
        writer1 = csv.writer(b)
        writer1.writerow(file_money)
    label_money_info.configure(text=f'₹ {new_money}')

def add_money_system():
    profile_after_login_system_2()
    money_add = tabview2_entry2.get()
    tabview2_entry2.delete(0,END)
    new_money = user_money_old + float(money_add)
    file_money = []
    with open('Files/'+acc_no_open_2+'.csv','r') as a:
        reader1 = csv.reader(a)
        for row1 in reader1:
            file_money.append(row1)
            file_money.remove(row1)
            file_money.append(str(new_money))
    with open('Files/'+acc_no_open_2+'.csv','w') as b:
        writer1 = csv.writer(b)
        writer1.writerow(file_money)
    label_money_info.configure(text=f'₹ {new_money}')

def loan_money_system():
    profile_after_login_system_2()
    money_add = tabview2_entry3.get()
    tabview2_entry3.delete(0,END)
    new_money = user_money_old + float(money_add)
    file_money = []
    with open('Files/'+acc_no_open_2+'.csv','r') as a:
        reader1 = csv.reader(a)
        for row1 in reader1:
            file_money.append(row1)
            file_money.remove(row1)
            file_money.append(str(new_money))
    with open('Files/'+acc_no_open_2+'.csv','w') as b:
        writer1 = csv.writer(b)
        writer1.writerow(file_money)
    label_money_info.configure(text=f'₹ {new_money}')

def emp_login_system():
    emp_name = entry_eusername.get()
    emp_password = entry_epassword.get()
    emp_login_success = f"Login Successfully!\nWelcome {emp_name}.\nYour attendence has been recorded."
    emp_login_fail = f"Employee named '{emp_name}' not found!\nnote :- Either Your Username or\nPassword Is Wrong."
    with open('Files/!employee_list.csv','r') as f:
        reader = csv.reader(f,delimiter=',')
        rownum = 0
        for row in reader:        
            if row == [emp_name, emp_password]:
                rownum = rownum+1
            else:
                continue
        if rownum == 1:
            playsound('Files/Items/confirmation.wav',block=False)
            toplevel_message(emp_login_success,off,ok)
        else:
            toplevel_message(emp_login_fail,on,back)        


def main_window():
    global root1
    global frame1
    global entry1
    global textbox1
    global textbox2
    global textbox3

    try:
        root2.destroy()
    except:
        pass
    try:
        root3.destroy()
    except:
        pass
 
    set_appearance_mode('dark')
    set_default_color_theme('blue')

    # root1 : Creating a master
    root1 = CTk()
    root1.title('Banking System')
    root1.iconbitmap('Files/Items/bot_happy.ico')
    root1.geometry(f"{880}x{615}")
    root1.minsize(880,615)
    root1.maxsize(880,615)
    
    
    # label1 : HEADING
    label1 = CTkLabel(master=root1,text='Main Window',font=('Roboto',24,'bold'))
    label1.grid(row=0,column=3,pady=10,padx=60,ipadx=20,sticky='w')


    # radio buttons : For decoration
    radio1 = CTkRadioButton(master=root1,text="--------------------------------------",fg_color='#f30701')
    radio1.grid(row=1,column=0)
    
    radio2 = CTkRadioButton(master=root1,text="--------------------------------------",fg_color='#2424ff')
    radio2.grid(row=2,column=0)
    
    radio3 = CTkRadioButton(master=root1,text="--------------------------------------",fg_color='#ede807')
    radio3.grid(row=3,column=0)
    
    radio4 = CTkRadioButton(master=root1,text="--------------------------------------",fg_color='#26c115')
    radio4.grid(row=4,column=0)


    # frame1 : Creating a Frame
    frame1 = CTkFrame(master=root1,border_width=3,corner_radius=10,border_color='#3f60fc')
    frame1.grid(row=1,column=2,pady=10,padx=0,rowspan=4,columnspan=3)


    # textbox : Creating textboxes
    textbox1 = CTkTextbox(master=frame1,height=150,width=370,
        border_color='#ffa346',border_width=3,corner_radius=18,font=('Roboto',15,))
    textbox1.grid(row=0,column=0,padx=10,pady=10,columnspan=2)
    textbox1.insert("0.0",f'''HELLO!!\nMy name is {BOT} ^_^\nI am a banking bot of 'PAISA CHOR BANK' '(PCB)'
And I will be helping you with your work.\nClick 'Start' to start Or Enter a 'Command' ''')
    textbox1.configure(state="disabled")

    textbox2 = CTkTextbox(master=frame1,height=90,width=250,
        border_color='#4aff4a',border_width=3,corner_radius=18,font=('Roboto',15,))
    textbox2.grid(row=1,column=2,padx=10,)
    textbox2.insert("0.0","/<command>")
    textbox2.configure(state="disabled")

    textbox3 = CTkTextbox(master=frame1,height=130,width=370,
        border_color='#ffa346',border_width=3,corner_radius=18,font=('Roboto',16,))
    textbox3.grid(row=2,column=0,padx=10,pady=10,columnspan=2)
    textbox3.insert("0.0","<Answer>")
    textbox3.configure(state="disabled")


    # entry1 : Creating a Entry for user to enter input
    entry1 = CTkEntry(master=root1,placeholder_text="                   Enter Command",
        border_width=3,corner_radius=10,border_color='#3f60fc',font=('Roboto',15,))
    entry1.grid(row=5,column=3,pady=12,padx=10,ipadx=80,ipady=10)


    # Appearance Theme
    label_appearance = CTkLabel(master=root1,text='Theme :',font=('Roboto',18,))
    label_appearance.grid(row=5,column=0,padx=10,sticky='ws')
    
    appearance_mode_optionemenu =CTkOptionMenu(master=root1, values=["Dark","Light", "System"],fg_color='#0379fc',
        button_color='#0756cb',command=change_appearance_mode_event)
    appearance_mode_optionemenu.grid(row=6, column=0, padx=(0,15),ipadx=8,ipady=3)


    # button : Creating Buttons
    button3 = CTkButton(master=root1,text='Exit',border_width=3,corner_radius=10,hover_color='#f8182f',
        border_color='#3f60fc',command=root1.destroy)
    button3.grid(row=6,column=2,ipadx=20,ipady=10)

    button1 = CTkButton(master=root1,text='Enter',border_width=3,corner_radius=15,border_color='#3f60fc',
        command=enter)
    button1.grid(row=6,column=3,ipadx=20,ipady=10)

    button2 = CTkButton(master=root1,text='Start',border_width=3,corner_radius=10,hover_color='#35dd17',
        border_color='#3f60fc',command=start)
    button2.grid(row=6,column=4,ipadx=20,ipady=10)

    root1.mainloop()


def second_window():
    global root2

    try:
        root1.destroy()
    except:
        pass
    try:
        root3.destroy()
    except:
        pass

    set_appearance_mode('dark')
    set_default_color_theme('blue')

    # root2 : Creating second master
    root2 = CTk()
    root2.title('Banking System')
    root2.iconbitmap('Files/Items/bot_happy.ico')
    root2.geometry(f"{650}x{530}")
    root2.minsize(650,530)
    root2.maxsize(650,530)

    # Creating a frame    
    frame2 = CTkFrame(master=root2,border_width=2)
    frame2.grid(row=1,column=0,pady=0,padx=0,rowspan=4)
    
    frame2_button1 = CTkButton(master=frame2,text='Main',width=169,height=80,border_color='#3f60fc',
        hover_color='#35dd17',border_width=3,command=main)
    frame2_button1.grid(row=0,column=0,pady=(10,5),padx=(5,5))
    frame2_button2 = CTkButton(master=frame2,text='Exit',width=169,height=80,border_color='#3f60fc',
        hover_color='#f8182f',border_width=3,command=root2.destroy)
    frame2_button2.grid(row=1,column=0,pady=(0,10),padx=(5,5))

    frame2_label1 = CTkLabel(master=frame2,text=" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
    frame2_label1.grid(row=2,column=0)

    # Appearance Theme
    label_appearance = CTkLabel(master=frame2,text='Theme :',font=('Roboto',18,))
    label_appearance.grid(row=4,column=0,padx=10,pady=(20,0),sticky='ws')
    
    appearance_mode_optionemenu =CTkOptionMenu(master=frame2, values=["Dark","Light", "System"],fg_color='#0379fc',
        button_color='#0756cb',command=change_appearance_mode_event)
    appearance_mode_optionemenu.grid(row=5, column=0, padx=20,pady=(0,20))

    # radio buttons : For decoration
    radio1 = CTkRadioButton(master=root2,text="-------------------",fg_color='#f30701')
    radio1.grid(row=1,column=1)
    
    radio2 = CTkRadioButton(master=root2,text="-------------------",fg_color='#2424ff')
    radio2.grid(row=2,column=1)
    
    radio3 = CTkRadioButton(master=root2,text="-------------------",fg_color='#ede807')
    radio3.grid(row=3,column=1)
    
    radio4 = CTkRadioButton(master=root2,text="-------------------",fg_color='#26c115')
    radio4.grid(row=4,column=1)

    # Creating a Tabview
    tabview1 = CTkTabview(master=root2,width=250,height=200,border_width=4,border_color='#3f60fc')
    tabview1.grid(row=1,column=2,pady=(10,10),ipadx=40,rowspan=4,sticky="nsew")
    tabview1.add("Customer")
    tabview1.add("Employee")
    tabview1.set("Customer")

    tabview1_label1 = CTkLabel(master=tabview1.tab("Customer"),text="➡  Already have account?",
        font=('Roboto',18,))
    tabview1_label1.grid(row=0,column=0,padx=20,pady=(20,10),sticky='s')
    tabview1_button1 = CTkButton(master=tabview1.tab("Customer"),text="Login Here",width=110,height=50,
        border_color='#3f60fc',border_width=3,command=toplevel_login)
    tabview1_button1.grid(row=1,column=0)

    tabview1_label2 = CTkLabel(master=tabview1.tab("Customer"),text="➡  Don't have an account?",
        font=('Roboto',18,))
    tabview1_label2.grid(row=3,column=0,padx=20,pady=(20,10),sticky='s')
    tabview1_button2 = CTkButton(master=tabview1.tab("Customer"),text="Register Here",width=110,height=50,
        border_color='#3f60fc',border_width=3,command=toplevel_register)
    tabview1_button2.grid(row=4,column=0)

    tabview1_label1 = CTkLabel(master=tabview1.tab("Employee"),text="➡  Employee Login               ",
        font=('Roboto',18,))
    tabview1_label1.grid(row=0,column=0,padx=20,pady=(20,10),sticky='s')
    tabview1_button1 = CTkButton(master=tabview1.tab("Employee"),text="Login Here",width=110,height=50,
        border_color='#3f60fc',border_width=3,command=toplevel_emp_login)
    tabview1_button1.grid(row=1,column=0)

    root2.mainloop()


def after_login_window():
    global root3
    global tabview2_entry1
    global tabview2_entry2
    global tabview2_entry3
    global label_money_info

    try:
        root2.destroy()
    except:
        pass
    
    set_appearance_mode('dark')
    set_default_color_theme('blue')

    # root3 : Creating 'After Login Window' master
    root3 = CTk()
    root3.title('User Profile')
    root3.iconbitmap('Files/Items/bot_happy.ico')
    root3.geometry(f"{850}x{530}")
    root3.minsize(850,530)
    root3.maxsize(850,530)

    # label_1 : HEADING
    label_1 = CTkLabel(master=root3,text='Your Profile',font=('Roboto',25,'underline'))
    label_1.grid(row=1,column=1,pady=10,padx=60,ipadx=20,columnspan=2,)

    # Creating 1st frame
    frame3 = CTkFrame(master=root3,border_width=2)
    frame3.grid(row=1,column=0,pady=0,padx=0,rowspan=4)
    
    frame3_button1 = CTkButton(master=frame3,text='Main',width=169,height=80,border_color='#3f60fc',
        hover_color='#35dd17',border_width=3,font=('Roboto',15,),command=main)
    frame3_button1.grid(row=0,column=0,pady=(10,5),padx=(5,5))
    frame3_button2 = CTkButton(master=frame3,text='Back',width=169,height=80,border_color='#3f60fc',
        hover_color='#f4680b',border_width=3,font=('Roboto',15,),command=second_window)
    frame3_button2.grid(row=1,column=0,pady=(0,5),padx=(5,5))
    frame3_button3 = CTkButton(master=frame3,text='Exit',width=169,height=80,border_color='#3f60fc',
        hover_color='#f8182f',border_width=3,font=('Roboto',15,),command=root3.destroy)
    frame3_button3.grid(row=2,column=0,pady=(0,5),padx=(5,5))

    frame3_label1 = CTkLabel(master=frame3,text=" \n \n \n \n \n \n \n \n \n \n ")
    frame3_label1.grid(row=3,column=0)

    # Appearance Theme
    label_appearance = CTkLabel(master=frame3,text='Theme :',font=('Roboto',18,))
    label_appearance.grid(row=4,column=0,padx=10,pady=(20,0),sticky='ws')
    
    appearance_mode_optionemenu =CTkOptionMenu(master=frame3, values=["Dark","Light", "System"],fg_color='#0379fc',
        button_color='#0756cb',command=change_appearance_mode_event)
    appearance_mode_optionemenu.grid(row=5, column=0, padx=20,pady=(0,30))

    # label_2 : Output Row's names
    label_2 = CTkLabel(master=root3,text='Account no. : \n\nUsername    : \n\nE-mail      : ',font=('Courier New',22,))
    label_2.grid(row=2,column=1,pady=(10,0),padx=(20,0),sticky='en')
    label_3 = CTkLabel(master=root3,text='Balance     : ',font=('Courier New',22,))
    label_3.grid(row=3,column=1,pady=(0,10),padx=(20,0),sticky='en')

    label_user_info = CTkLabel(master=root3,text=user_info,font=('Courier New',22,))
    label_user_info.grid(row=2,column=2,pady=(0,10),padx=(20,0),sticky='w')
    label_money_info = CTkLabel(master=root3,text=f'₹ {user_money}',font=('Courier New',22,))
    label_money_info.grid(row=3,column=2,pady=(0,10),padx=(20,0),sticky='wn')

    # Creating a Tabview
    tabview_2 = CTkTabview(master=root3,width=250,height=200,border_width=2,)
    tabview_2.grid(row=4,column=1,pady=(10,0),ipadx=80,columnspan=2,sticky="nsew")
    tabview_2.add("Withdraw")
    tabview_2.add("Deposit")
    tabview_2.add("Loan")
    tabview_2.set("Withdraw")

    tabview2_label1 = CTkLabel(master=tabview_2.tab("Withdraw"),
        text="➡        Enter the Amount to Withdraw :                                        ",font=('Roboto',18,))
    tabview2_label1.grid(row=0,column=0,padx=20,pady=(20,10),columnspan=2,sticky='s')
    tabview2_entry1 = CTkEntry(master=tabview_2.tab("Withdraw"),placeholder_text="  ₹",
        border_width=3,corner_radius=10,border_color='#3f60fc',font=('Roboto',15,))
    tabview2_entry1.grid(row=1,column=0,pady=12,padx=10,ipadx=80,ipady=10)
    tabview2_button1 = CTkButton(master=tabview_2.tab("Withdraw"),text="Proceed",width=80,height=50,
        border_color='#3f60fc',border_width=3,command=withdraw_money_system)
    tabview2_button1.grid(row=1,column=1,sticky='w')

    tabview2_label2 = CTkLabel(master=tabview_2.tab("Deposit"),
        text="➡        Enter the Amount to Deposit :                                            ",font=('Roboto',18,))
    tabview2_label2.grid(row=0,column=0,padx=20,pady=(20,10),columnspan=2,sticky='s')
    tabview2_entry2 = CTkEntry(master=tabview_2.tab("Deposit"),placeholder_text="  ₹",
        border_width=3,corner_radius=10,border_color='#3f60fc',font=('Roboto',15,))
    tabview2_entry2.grid(row=1,column=0,pady=12,padx=10,ipadx=80,ipady=10)
    tabview2_button2 = CTkButton(master=tabview_2.tab("Deposit"),text="Proceed",width=80,height=50,
        border_color='#3f60fc',border_width=3,command=add_money_system)
    tabview2_button2.grid(row=1,column=1,sticky='w')

    tabview2_label3_1 = CTkLabel(master=tabview_2.tab("Loan"),font=('Roboto',18,),
        text='''Our Bank provides Loan at 9% per Annum\n    ➡         Enter the Amount you want to Borrow :                         ''',)
    tabview2_label3_1.grid(row=0,column=0,padx=(20,0),pady=(20,10),columnspan=2,sticky='s')
    tabview2_entry3 = CTkEntry(master=tabview_2.tab("Loan"),placeholder_text="  ₹",
        border_width=3,corner_radius=10,border_color='#3f60fc',font=('Roboto',15,))
    tabview2_entry3.grid(row=2,column=0,pady=12,padx=10,ipadx=80,ipady=10)
    tabview2_button3 = CTkButton(master=tabview_2.tab("Loan"),text="Proceed",width=80,height=50,
        border_color='#3f60fc',border_width=3,command=loan_money_system)
    tabview2_button3.grid(row=2,column=1,sticky='w')

    root3.mainloop()


def toplevel_login():
    global toplevel1
    global entry_lusername
    global entry_lpassword
    global switch_lpassword

    try:
        toplevel1.destroy()
    except:
        pass
    try:
        toplevel2.destroy()
    except:
        pass
    try:
        toplevel3.destroy()
    except:
        pass

    toplevel1 = CTkToplevel()
    toplevel1.title('Login')
    toplevel1.geometry(f"{300}x{470}")
    toplevel1.minsize(300,470)
    toplevel1.maxsize(300,470)

    label_login = CTkLabel(master=toplevel1,text='Login',font=('Roboto',22,))
    label_login.grid(row=0,column=1,padx=10,pady=(10,10),sticky='s')

    # Login Frame
    frame_login = CTkFrame(master=toplevel1,border_width=4,border_color='#3f60fc')
    frame_login.grid(row=1,column=1,pady=(0,20),padx=20)

    label_username = CTkLabel(master=frame_login,text='Enter Username',font=('Roboto',18))
    label_username.grid(row=1,column=0,pady=(10,0),padx=60,sticky='sw')

    entry_lusername = CTkEntry(master=frame_login,placeholder_text="           Username",
        border_width=3,corner_radius=10,border_color='#3f60fc',font=('Roboto',15,))
    entry_lusername.grid(row=2,column=0,pady=5,padx=10,ipadx=50,ipady=5)

    label_password = CTkLabel(master=frame_login,text='Enter Password',font=('Roboto',18))
    label_password.grid(row=3,column=0,pady=(10,0),padx=60,sticky='sw')

    entry_lpassword = CTkEntry(master=frame_login,placeholder_text="           Password",show='*',
        border_width=3,corner_radius=10,border_color='#3f60fc',font=('Roboto',15,))
    entry_lpassword.grid(row=4,column=0,pady=5,padx=10,ipadx=50,ipady=5)

    switch_lpassword = CTkSwitch(master=frame_login,text='Show',font=('Roboto',12),switch_height=15,switch_width=30,
        command=lambda:pass_switch(switch_lpassword))
    switch_lpassword.grid(row=5,column=0,sticky='n')

    label_enter = CTkLabel(master=frame_login,text=' \n \n \n \n \n \n \n ')
    label_enter.grid(row=6,column=0,pady=5,)

    button1 = CTkButton(master=frame_login,text='Login',border_width=3,corner_radius=15,border_color='#3f60fc',
        command=login_system)
    button1.grid(row=7,column=0,pady=20)


def toplevel_register():
    global toplevel2
    global entry_rusername
    global entry_rpassword1
    global entry_rpassword2
    global entry_rgmail
    global label_error
    global button_register
    global switch_rpassword1
    global switch_rpassword2

    try:
        toplevel1.destroy()
    except:
        pass
    try:
        toplevel2.destroy()
    except:
        pass
    try:
        toplevel3.destroy()
    except:
        pass

    toplevel2 = CTkToplevel()
    toplevel2.title('Register')
    toplevel2.geometry(f"{300}x{540}")
    toplevel2.minsize(300,540)
    toplevel2.maxsize(300,540)

    label_register = CTkLabel(master=toplevel2,text='Register',font=('Roboto',22,))
    label_register.grid(row=0,column=1,padx=10,pady=(10,10),sticky='s')

    # Login Frame
    frame_register = CTkFrame(master=toplevel2,border_width=4,border_color='#3f60fc')
    frame_register.grid(row=1,column=1,pady=(0,20),padx=20)

    label_username = CTkLabel(master=frame_register,text='Create Username',font=('Roboto',18))
    label_username.grid(row=1,column=0,pady=(10,0),padx=60,sticky='sw')

    entry_rusername = CTkEntry(master=frame_register,placeholder_text="    Create Username",
        border_width=3,corner_radius=10,border_color='#3f60fc',font=('Roboto',15,))
    entry_rusername.bind('<KeyRelease>',empty_entry)
    entry_rusername.grid(row=2,column=0,pady=5,padx=10,ipadx=50,ipady=5)

    label_password1 = CTkLabel(master=frame_register,text='Create Password',font=('Roboto',18))
    label_password1.grid(row=3,column=0,pady=(15,0),padx=60,sticky='sw')

    entry_rpassword1 = CTkEntry(master=frame_register,placeholder_text="    Create Password",show='*',
        border_width=3,corner_radius=10,border_color='#3f60fc',font=('Roboto',15,))
    entry_rpassword1.bind('<KeyRelease>',empty_entry)
    entry_rpassword1.grid(row=4,column=0,pady=5,padx=10,ipadx=50,ipady=5)

    switch_rpassword1 = CTkSwitch(master=frame_register,text='Show',font=('Roboto',12,),switch_height=15,switch_width=30,
        command=lambda:pass_switch(switch_rpassword1))
    switch_rpassword1.grid(row=5,column=0,sticky='n')

    label_password2 = CTkLabel(master=frame_register,text='Confirm Password',font=('Roboto',18))
    label_password2.grid(row=6,column=0,pady=(15,0),padx=60,sticky='sw')

    entry_rpassword2 = CTkEntry(master=frame_register,placeholder_text="   Confirm Password",show='*',
        border_width=3,corner_radius=10,border_color='#3f60fc',font=('Roboto',15,))
    entry_rpassword2.grid(row=7,column=0,pady=5,padx=10,ipadx=50,ipady=5)

    switch_rpassword2 = CTkSwitch(master=frame_register,text='Show',font=('Roboto',12,),switch_height=15,switch_width=30,
        command=lambda:pass_switch(switch_rpassword2))
    switch_rpassword2.grid(row=8,column=0,sticky='n')

    label_gmail = CTkLabel(master=frame_register,text='Enter Email',font=('Roboto',18))
    label_gmail.grid(row=9,column=0,pady=(15,0),padx=60,sticky='sw')

    entry_rgmail = CTkEntry(master=frame_register,placeholder_text="    Someone123@gmail.com",
        border_width=3,corner_radius=10,border_color='#3f60fc',font=('Roboto',15,),)
    entry_rgmail.bind('<KeyRelease>',empty_entry)
    entry_rgmail.bind('<KeyRelease>',email_check)
    entry_rgmail.grid(row=10,column=0,pady=(5,0),padx=10,ipadx=50,ipady=5)
    
    label_error = CTkLabel(master=frame_register,text='',font=('Roboto',13))
    label_error.grid(row=11,column=0,sticky='n')

    button_register = CTkButton(master=frame_register,text='Register',border_width=3,corner_radius=15,
        border_color='#3f60fc',command=register_system,state='disabled')
    button_register.grid(row=12,column=0,pady=(0,10))


def toplevel_register_money():
    global toplevel4
    global entry_add_money
    global entry_clear_cache

    try:
        toplevel4.destroy()
    except:
        pass

    toplevel4 = CTkToplevel()
    toplevel4.title('Register')
    toplevel4.geometry(f"{500}x{350}")
    toplevel4.minsize(500,350)
    toplevel4.maxsize(500,350)

    label_register = CTkLabel(master=toplevel4,text='Deposit Money',font=('Roboto',22,))
    label_register.grid(row=0,column=1,padx=10,pady=(10,10),sticky='s')

    # Add Money Frame
    frame_add_money = CTkFrame(master=toplevel4,border_width=4,border_color='#3f60fc')
    frame_add_money.grid(row=1,column=1,pady=(0,10),padx=20)

    label_add_money = CTkLabel(master=frame_add_money,text='Deposit An Initial Amount',font=('Roboto',18))
    label_add_money.grid(row=1,column=0,pady=(10,10),padx=60,sticky='sw')

    entry_add_money = CTkEntry(master=frame_add_money,placeholder_text="    ₹",
        border_width=3,corner_radius=10,border_color='#3f60fc',font=('Roboto',15,))
    entry_add_money.grid(row=2,column=0,pady=10,padx=10,ipadx=50,ipady=5)

    # Cache Frame
    frame_cache = CTkFrame(master=toplevel4,border_width=4,border_color='#3f60fc')
    frame_cache.grid(row=2,column=1,pady=(0,10),padx=20)

    label_clear_cache = CTkLabel(master=frame_cache,text='Clear Cache (Enter without any symbol)\n \n'+cache,font=('Roboto',18))
    label_clear_cache.grid(row=1,column=0,pady=(10,10),padx=60,sticky='sw')

    entry_clear_cache = CTkEntry(master=frame_cache,placeholder_text="  Without any Symbol",
        border_width=3,corner_radius=10,border_color='#3f60fc',font=('Roboto',15,))
    entry_clear_cache.grid(row=2,column=0,pady=10,padx=10,ipadx=50,ipady=5)

    button1 = CTkButton(master=toplevel4,text='Register',border_width=3,corner_radius=15,border_color='#3f60fc',
        command=rcache_check)
    button1.grid(row=3,column=1,pady=(0,10))


def toplevel_emp_login():
    global toplevel3
    global entry_eusername
    global entry_epassword
    global switch_epassword

    try:
        toplevel1.destroy()
    except:
        pass
    try:
        toplevel2.destroy()
    except:
        pass
    try:
        toplevel3.destroy()
    except:
        pass

    toplevel3 = CTkToplevel()
    toplevel3.title('Employee Login')
    toplevel3.geometry(f"{300}x{470}")
    toplevel3.minsize(300,470)
    toplevel3.maxsize(300,470)

    label_login = CTkLabel(master=toplevel3,text='Employee Login',font=('Roboto',22,))
    label_login.grid(row=0,column=1,padx=10,pady=(10,10),sticky='s')

    # Login Frame
    frame_login = CTkFrame(master=toplevel3,border_width=4,border_color='#3f60fc')
    frame_login.grid(row=1,column=1,pady=(0,20),padx=20)

    label_username = CTkLabel(master=frame_login,text='Enter Username',font=('Roboto',18))
    label_username.grid(row=1,column=0,pady=(10,0),padx=60,sticky='sw')

    entry_eusername = CTkEntry(master=frame_login,placeholder_text="           Username",
        border_width=3,corner_radius=10,border_color='#3f60fc',font=('Roboto',15,))
    entry_eusername.grid(row=2,column=0,pady=5,padx=10,ipadx=50,ipady=5)

    label_password = CTkLabel(master=frame_login,text='Enter Password',font=('Roboto',18))
    label_password.grid(row=3,column=0,pady=(10,0),padx=60,sticky='sw')

    entry_epassword = CTkEntry(master=frame_login,placeholder_text="           Password",show='*',
        border_width=3,corner_radius=10,border_color='#3f60fc',font=('Roboto',15,))
    entry_epassword.grid(row=4,column=0,pady=5,padx=10,ipadx=50,ipady=5)

    switch_epassword = CTkSwitch(master=frame_login,text='Show',font=('Roboto',12),switch_height=15,switch_width=30,
        command=lambda:pass_switch(switch_epassword))
    switch_epassword.grid(row=5,column=0,sticky='n')

    label_enter = CTkLabel(master=frame_login,text=' \n \n \n \n \n \n ')
    label_enter.grid(row=6,column=0,pady=5,)

    button1 = CTkButton(master=frame_login,text='Login',border_width=3,corner_radius=15,border_color='#3f60fc',
        command=emp_login_system)
    button1.grid(row=7,column=0,pady=20)

# Some Important veriables
NAME = ''
BOT = 'SYLPHI'

engine = ps.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[3].id)
engine.setProperty('rate',180)

switch_lpassword = None
switch_rpassword1 = None
switch_rpassword2 = None
switch_epassword = None

# Text Store :-
on = 'normal'              # For 'Try Again' Button in Toplevels
off = 'disabled'           # For 'Try Again' Button in Toplevels
ok = 'Okay'
back = 'Go Back'
register_success = 'Registration Successfull!'
acc_exist = 'This User already exists!\nTry Logging in or\nCreate a new account.'
wrong_password = "Passwords don't match!\nEnter same passwords."
invalid_email = "Invalid Email Address!\nPlease Type Valid Email Address."
login_success = 'Login Successfully!'
acc_not_exist = "This account doesn't exist!\nCheck your login info or\nTry making a new account."



main_window()
# second_window()
