import os
import tempfile
from tkinter import *

import time
import datetime as dt
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import datetime


windows=Tk()
windows.geometry('1920x1200')

windows.title('resizable') #window resizable

windows.config(bg='cyan')
windows.title('STUDENT MANAGEMENT SYSTEM')

def time_update():
    currenttime= time.strftime("%H:%M:%S")
    crnt_time.config(text=currenttime) #display the given time format
    crnt_time.after(1000, time_update) #update the time after every 1000 secs

date=dt.datetime.now()

currentDateTime = datetime.datetime.now()

def upload():
    global filename

    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File',
                                        filetypes=(("JPG file", ".jpg"), ("PNG file", ".png"),
                                                   ("All files", ".txt"))) #parameter for files format
    img=(Image.open(filename)) #to open the selected file
    image_resize=img.resize((220, 220)) #return a resized copy of the image
    selected_Image=ImageTk.PhotoImage(image_resize) #is to make the image compartible with tkinter
    lbl.config(image=selected_Image) #to configure the selected image
    lbl.image=selected_Image #to attach the selected image on the created label frame
    img.save("C:\\Users\\Igbon Ifijeh\\Desktop\\School_Management_Project/"+ str(selected_Image) + ".jpg")

def register():
    global img, connect

    #validations: if statement to condition the fields
    if id_entryname.get() == '' or firstnameEntry.get() == '' or lastnameEntry.get() == '' or dobEntry.get() == ''\
        or religionEntry.get() == '' or class_1Entry.get() == ''or fatherNameEntry.get() == ''\
        or motherNameEntry.get() == '' or homeaddressEntry.get() == '' or gender.get() == '' or variable1.get() == ''\
        or phone_noEntry.get() == '' or nokEntry.get() == '' or phone_noEntry.get() == '':
        messagebox.showerror("!", "Please ensure data have been entered on all fields")
        return

    else:
        studentDetailsText.insert(END, '\t\tStudent\'s Information' + '\n')
        studentDetailsText.insert(END, "Student Registration No: \t\t\t\t" + id_entryname.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "First Name: \t\t\t\t" + firstnameEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Last Name: \t\t\t\t" + lastnameEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Date of Birth: \t\t\t\t" + dobEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Religion: \t\t\t\t" + religionEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Class: \t\t\t\t" + class_1Entry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Father\'s Name: \t\t\t\t" + firstnameEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Mother\'s Name: \t\t\t\t" + motherNameEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Home Address: \t\t\t\t" + homeaddressEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Gender: \t\t\t\t" + gender.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Country: \t\t\t\t" + variable1.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Phone Number: \t\t\t\t" + phone_noEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Name of Next of Kin: \t\t\t\t" + nokEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Phone Number of Next of Kin: \t\t\t\t" + phone_nokEntry.get() + "\n")
        studentDetailsText.insert(END, "*************END*************"+ "\n")

    #database connection
    connect=sqlite3.connect("Student_Management_Project.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cursor = connect.cursor()

    connect.execute("CREATE TABLE IF NOT EXISTS Student_Management_Project_Table(Student_Id TEXT NOT NULL, "
                    "First_Name TEXT NOT NULL, Last_Name TEXT NOT NULL, Date_Of_Birth TEXT NOT NULL, "
                    "Religion TEXT NOT NULL, Class TEXT NOT NULL, Father_Name TEXT NOT NULL, "
                    "Mother_Name TEXT NOT NULL, Home_Address TEXT NOT NULL, Gender TEXT NOT NULL, "
                    "Country TEXT NOT NULL, Phone_Number TEXT NOT NULL, Name_Of_Next_Of_Kin TEXT NOT NULL, "
                    "Phone_Number_of_Next_Of_Kin TEXT NOT NULL, Time_Stamp TIMESTAMP)")
    cursor.execute("SELECT * FROM Student_Management_Project_Table")
    # print("Table created succesfully")
    # messagebox.showinfo("!","Database created")
    # connect.commit() #changes should be made to the connection
    # connect.close()

    selection = ("SELECT * FROM Student_Management_Project_Table WHERE Student_Id = ?")
    cursor.execute(selection, [(id_entryname.get())])
    if cursor.fetchone():
        id_entryname.delete(0, END)
        firstnameEntry .delete(0, END)
        lastnameEntry .delete(0, END)
        dobEntry .delete(0, END)
        religionEntry .delete(0, END)
        class_1Entry .delete(0, END)
        fatherNameEntry .delete(0, END)
        motherNameEntry.delete(0, END)
        homeaddressEntry.delete(0, END)
        gender.set(0)
        variable1.set("Select Country")
        phone_noEntry.delete(0, END)
        nokEntry.delete(0, END)
        phone_nokEntry.delete(0, END)
        studentDetailsText.delete("1.0", END)
        registerbtn.config(state="normal")
        Image1=PhotoImage(file="admin image.png")
        lbl.config(image=Image1)
        lbl.image=Image1
        img = ""
        messagebox.showerror("!", "ID already exist")
        return
    else:
        insert = str("INSERT INTO Student_Management_Project_Table(Student_Id,First_Name,Last_Name,"
                     "Date_Of_Birth,Religion, Class, Father_Name, Mother_Name, Home_Address, Gender, Country,"
                     "Phone_Number, Name_Of_Next_Of_Kin, Phone_Number_of_Next_Of_Kin, Time_Stamp) "
                     "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
        cursor.execute(insert, (id_entryname.get(), firstnameEntry.get(), lastnameEntry.get(), dobEntry.get(),
                                religionEntry.get(), class_1Entry.get(), fatherNameEntry.get(), motherNameEntry.get(),
                                homeaddressEntry.get(), gender.get(), variable1.get(), phone_noEntry.get(),
                                nokEntry.get(), phone_nokEntry.get(), currentDateTime))
        messagebox.showinfo("Success", "Successful storage")
        connect.commit()
        connect.close()

def reset():
    id_entryname.delete(0, END)
    firstnameEntry.delete(0, END)
    lastnameEntry.delete(0, END)
    dobEntry.delete(0, END)
    religionEntry.delete(0, END)
    class_1Entry.delete(0, END)
    fatherNameEntry.delete(0, END)
    motherNameEntry.delete(0, END)
    homeaddressEntry.delete(0, END)
    gender.set(0)
    variable1.set("Select Country")
    phone_noEntry.delete(0, END)
    nokEntry.delete(0, END)
    phone_nokEntry.delete(0, END)
    studentDetailsText.delete("1.0", END)
    registerbtn.config(state="normal")
    Image1 = PhotoImage(file="admin image.png")
    lbl.config(image=Image1)
    lbl.image = Image1
    img = ""

def exit():
    exit=messagebox.askyesno('!', "Do you want to exit?")
    if exit:
        windows.destroy()


def print(txt):
    printquestion=messagebox.askyesno("?", "Do you want to print the details?")
    if printquestion:
        temp_file = tempfile.mktemp(".txt")
        open(temp_file, 'w').write(txt)
        os.startfile(temp_file, 'print')


#variable for data collection
id_entryname=IntVar()
firstnameEntry=StringVar()
lastnameEntry=StringVar()
dobEntry=StringVar()
religionEntry=StringVar()
class_1Entry=StringVar()
fatherNameEntry=StringVar()
motherNameEntry=StringVar()
homeaddressEntry=StringVar()
gender=StringVar()
variable1=StringVar()
phone_noEntry=StringVar()
nokEntry=StringVar()
phone_nokEntry=StringVar()


#Label for profile name
prflname=Label(windows, text="STUDENT'S MANAGEMENT SYSTEM", font=('tahoma', 18, 'bold'), bg='cyan')
prflname.place(x=502, y=0)



#Student frames

data_frame1= LabelFrame(windows, bd=7, text='Student Details', bg='cadet blue', font=('ariel', 10, 'bold'), width=450,
                        height=820, relief=GROOVE)
data_frame1.place(x=10, y=20)

nok_frame1=LabelFrame(data_frame1, bd=7, text='Guardian Details', font=('ariel', 10, 'bold'),
                     bg='cadet blue', width=430, height=170)
nok_frame1.place(x=2, y=490)

# departments
nok_frame2=LabelFrame(data_frame1, bd=7, font=('ariel', 10, 'bold'),
                     bg='cadet blue', width=430, height=110)
nok_frame2.place(x=2, y=675)

#parents
data_frame2= LabelFrame(windows, bd=7, text='Parents Details', bg='cadet blue', font=('ariel', 10, 'bold'), width=450,
                        height=545, relief=GROOVE)
data_frame2.place(x=500, y=40)

#addresses
nok_frame3=LabelFrame(data_frame2, bd=7, text='Address Details', font=('ariel', 10, 'bold'),
                     bg='cadet blue', width=430, height=150)
nok_frame3.place(x=2, y=360)




studentDetails_frame=LabelFrame(windows, bd=7, bg='cadet blue',text='Student details', font=('Harrington', 13, 'bold'),
                                width=450, height=680, relief=GROOVE)
studentDetails_frame.place(x=980, y=20)

studentDetailsText=Text(studentDetails_frame, height=28, width=63, bd=5, bg='white', font=('arield', 11, 'bold'))
studentDetailsText.grid(row=0, column=0)



#button frame
button_frame= LabelFrame(windows,bd=7, bg='cadet blue',width=530, height=120)
button_frame.place(x=980, y=570)

#image frame
#image_frame=Frame(windows, bd=3, bg='black', width=230, height=230, relief=GROOVE)
#image_frame.place(x=480, y=100)





gender=StringVar()
variable1=StringVar()


#Labels and Entry fields

student_Id = Label(data_frame1, text='REG_NO:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black')
student_Id.place(x=2, y=10)

id_entryname=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
id_entryname.place(x=200, y=11)

firstname=Label(data_frame1,text='First Name:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
firstname.place(x=2, y=60)

firstnameEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
firstnameEntry.place(x=200, y=61)

lastname=Label(data_frame1,text='Last Name:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
lastname.place(x=2, y=110)

lastnameEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
lastnameEntry.place(x=200, y=111)

dob=Label(data_frame1,text='Gender:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
dob.place(x=2, y=160)

dobEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
dobEntry.place(x=200, y=161)

religion=Label(data_frame1,text='DOB:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
religion.place(x=2, y=210)

religionEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
religionEntry.place(x=200, y=211)

class_1=Label(data_frame1,text='Country:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
class_1.place(x=2, y=260)

class_1Entry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
class_1Entry.place(x=200, y=261)

fatherName=Label(data_frame1,text='Phn_no', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
fatherName.place(x=2, y=310)

fatherNameEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
fatherNameEntry.place(x=200, y=311)

motherName=Label(data_frame1,text='Email_1', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
motherName.place(x=2, y=360)

motherNameEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
motherNameEntry.place(x=200, y=361)

homeaddress=Label(data_frame1,text='Email_2', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
homeaddress.place(x=2, y=410)

homeaddressEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
homeaddressEntry.place(x=200, y=411)

#religion new
homeaddress=Label(data_frame1,text='Religion', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
homeaddress.place(x=2, y=450)

homeaddressEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
homeaddressEntry.place(x=200, y=450)





#Next of kin
nok=Label(nok_frame1,text='First name:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
nok.place(x=2, y=2)

nokEntry=Entry(nok_frame1, width=30, borderwidth=3, font=('tahoma',10))
nokEntry.place(x=195, y=2)

nok=Label(nok_frame1,text='Last name:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
nok.place(x=2, y=35)

nokEntry=Entry(nok_frame1, width=30, borderwidth=3, font=('tahoma',10))
nokEntry.place(x=195, y=35)



phone_nok=Label(nok_frame1,text='Phone No:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
phone_nok.place(x=2, y=70)

phone_nokEntry=Entry(nok_frame1, width=30, borderwidth=3, font=('tahoma',10))
phone_nokEntry.place(x=195, y=70)

phone_nok=Label(nok_frame1,text='Email:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
phone_nok.place(x=2, y=110)

phone_nokEntry=Entry(nok_frame1, width=30, borderwidth=3, font=('tahoma',10))
phone_nokEntry.place(x=195, y=110)

#department

nok=Label(nok_frame2,text='Department:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
nok.place(x=2, y=2)

nokEntry=Entry(nok_frame2, width=30, borderwidth=3, font=('tahoma',10))
nokEntry.place(x=195, y=2)

#sections 
nok=Label(nok_frame2,text='Section:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
nok.place(x=2, y=35)

nokEntry=Entry(nok_frame2, width=30, borderwidth=3, font=('tahoma',10))
nokEntry.place(x=195, y=35)

#classrooms
nok=Label(nok_frame2,text='Classroom:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
nok.place(x=2, y=65)

nokEntry=Entry(nok_frame2, width=30, borderwidth=3, font=('tahoma',10))
nokEntry.place(x=195, y=65)

#parents

firstname=Label(data_frame2,text='Father First Name:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
firstname.place(x=2, y=2)

firstnameEntry=Entry(data_frame2, width=30, borderwidth=3, font=('tahoma',10))
firstnameEntry.place(x=200, y=2)

lastname=Label(data_frame2,text='Last Name:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
lastname.place(x=2, y=40)

lastnameEntry=Entry(data_frame2, width=30, borderwidth=3, font=('tahoma',10))
lastnameEntry.place(x=200, y=40)

firstname=Label(data_frame2,text='Phn_no:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
firstname.place(x=2, y=80)

firstnameEntry=Entry(data_frame2, width=30, borderwidth=3, font=('tahoma',10))
firstnameEntry.place(x=200, y=80)

lastname=Label(data_frame2,text='Email:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
lastname.place(x=2, y=120)

lastnameEntry=Entry(data_frame2, width=30, borderwidth=3, font=('tahoma',10))
lastnameEntry.place(x=200, y=120)

#m_parent

firstname=Label(data_frame2,text='Mother First Name:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
firstname.place(x=2, y=160)

firstnameEntry=Entry(data_frame2, width=30, borderwidth=3, font=('tahoma',10))
firstnameEntry.place(x=200, y=160)

lastname=Label(data_frame2,text='Last Name:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
lastname.place(x=2, y=200)

lastnameEntry=Entry(data_frame2, width=30, borderwidth=3, font=('tahoma',10))
lastnameEntry.place(x=200, y=200)

firstname=Label(data_frame2,text='Phn_no:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
firstname.place(x=2, y=240)

firstnameEntry=Entry(data_frame2, width=30, borderwidth=3, font=('tahoma',10))
firstnameEntry.place(x=200, y=240)

lastname=Label(data_frame2,text='Email:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
lastname.place(x=2, y=280)

lastnameEntry=Entry(data_frame2, width=30, borderwidth=3, font=('tahoma',10))
lastnameEntry.place(x=200, y=280)

lastname=Label(data_frame2,text='Religion:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
lastname.place(x=2, y=320)

lastnameEntry=Entry(data_frame2, width=30, borderwidth=3, font=('tahoma',10))
lastnameEntry.place(x=200, y=320)

#addresses
nok=Label(nok_frame3,text='Door No:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
nok.place(x=2, y=2)

nokEntry=Entry(nok_frame3, width=30, borderwidth=3, font=('tahoma',10))
nokEntry.place(x=190, y=2)

nok=Label(nok_frame3,text=' Area:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
nok.place(x=2, y=40)

nokEntry=Entry(nok_frame3, width=30, borderwidth=3, font=('tahoma',10))
nokEntry.place(x=190, y=40)

nok=Label(nok_frame3,text=' Zipcode:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
nok.place(x=2, y=80)

nokEntry=Entry(nok_frame3, width=30, borderwidth=3, font=('tahoma',10))
nokEntry.place(x=190, y=80)


#Buttons
registerbtn= Button(button_frame, text='Register', bg='PURPLE', fg='WHITE', font=("#57a1f8", 16, 'bold'),
                    width=10, borderwidth=3, height=1, cursor='hand2', command=register)
registerbtn.place(x=10, y=10)

resetbtn= Button(button_frame, text='Reset', bg='PURPLE', fg='WHITE', font=("#57a1f8", 16, 'bold'),
                    width=10, borderwidth=3, height=1, cursor='hand2', command=reset)
resetbtn.place(x=350, y=10)

uploadbtn= Button(button_frame, text='Upload', bg='PURPLE', fg='WHITE', font=("#57a1f8", 16, 'bold'),
                    width=10, borderwidth=3, height=1, cursor='hand2', command=upload)
uploadbtn.place(x=10, y=65)

printbtn= Button(button_frame, text='Print', bg='PURPLE', fg='WHITE', font=("#57a1f8", 16, 'bold'),
                    width=10, borderwidth=3, height=1, cursor='hand2',
                 command=lambda:print(studentDetailsText.get("1.0", END)))
printbtn.place(x=180, y=38)

exitbtn= Button(button_frame, text='Exit', bg='red', fg='white', font=("#57a1f8", 16, 'bold'),
                    width=10, borderwidth=3, height=1, cursor='hand2', command=exit)
exitbtn.place(x=350, y=61)

#time section
crnt_time= Label(windows, text="Time", width=15, bg='cyan', fg='PURPLE', font=('#57a1f8', 12, 'bold'))
crnt_time.place(x=1400, y=750)

crnt_date=Label(windows, text=f"{date:%A,%B %d, %Y}", width=20, bg='cyan', fg='PURPLE',
                font=('#57a1f8', 12, 'bold'))
crnt_date.place(x=1320, y=780)

time_update()
windows.mainloop()