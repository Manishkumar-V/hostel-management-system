#import tkinter as tk
import tkinter as tk
import sys
import os
import  sqlite3
#import tkMessageBox as tm
import tkinter.messagebox as tm
from tkinter import ttk
from PIL import Image,ImageTk
import random
import smtplib


V_LARGE_F = ("Verdana" ,24)
VV_LARGE_F = ("Verdana" ,33)
Large_F = ("Verdana" , 21)
Nor_F = ("Verdana" , 16)
Sm_F = ("Verdana", 12)
V_S_F = ("Verdana", 10)


conn=sqlite3.connect('hostel.db')
c=conn.cursor()
#c.execute('DROP table login')
c.execute('CREATE TABLE IF NOT EXISTS login(WardenId TEXT primary key,Password TEXT,answer varchar(10))')
conn.commit()

conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS student(s_id INTEGER primary key AUTOINCREMENT ,s_name varchar(10),mob_no char(10),g_name varchar(10),DOB date,sem INTEGER,branch varchar(4),age INTEGER,area varchar(10),city varchar(10),state varchar(20),room_no INTEGER,foreign key(room_no)REFERENCES room(room_no) )')
conn.commit()

conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS block(block_id varchar(10) primary key,warden_id varchar(10),warden_name varchar(10),no_of_rooms INTEGER,total_capacity INTEGER,room_capacity INTEGER,foreign key(warden_id) REFERENCES wardens(warden_id))')
conn.commit()

conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS guardian(g_name varchar(10), s_id varchar(10),mobileno char(10),g_mail_id varchar(50),foreign key(s_id) REFERENCES student(s_id)ON DELETE CASCADE)')
conn.commit()


conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS room(room_no integer primary key,block_id INTEGER, room_capacity INTEGER ,Occupied INTEGER)')
conn.commit()

conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS mess_emp(emp_id varchar(10) primary key, emp_name varchar(10),mobileno INTEGER,salary FLOAT)')
conn.commit()

conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS outings(s_id varchar(10), o_date DATE,in_time TIME,out_time TIME,foreign key (s_id) REFERENCES student(s_id) ON DELETE CASCADE)')
conn.commit()

conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS fees(s_id varchar(10),room_no INTEGER,block_id INTEGER,rent FLOAT,mess_expense FLOAT,due_date DATE,paid_date DATE,status varhar(10),foreign key (s_id) REFERENCES student(s_id) ON DELETE CASCADE,foreign key(room_no)REFERENCES room(room_no) ON DELETE CASCADE,foreign key(block_id)REFERENCES block(block_id) ON DELETE CASCADE)')
conn.commit()


conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS wardens(warden_id varchar(10) primary key, warden_name varchar(10),mobileno INTEGER,salary FLOAT)')
conn.commit()



conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS mess(emp_id varchar(10) primary key, emp_name varchar(10),timing INTEGER)')
conn.commit()

conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS visitors(s_id varchar(10), v_name varchar(10),relationship varchar(10),foreign key (s_id) REFERENCES student(s_id) ON DELETE CASCADE  )")
conn.commit()

'''conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute("INSERT INTO login VALUES('warden_1','xyz123','1998-8-2')")
c.execute("INSERT INTO login VALUES('warden_2','abc123','1997-11-1')")
c.execute("INSERT INTO login VALUES('warden_3','jkl123','1997-11-10')")
conn.commit()

conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute("INSERT INTO wardens VALUES('warden_1','geeta',9874521997,19000)")
c.execute("INSERT INTO wardens VALUES('warden_2','asha',8775455987,19000)")
c.execute("INSERT INTO wardens VALUES('warden_3','sandhya',7664339876,19000)")
conn.commit()

conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute("INSERT INTO mess_emp VALUES('emp_1','shobha',7885644322,'10000')")
c.execute("INSERT INTO mess_emp VALUES('emp_2','rekha',8775632111,'6000')")
c.execute("INSERT INTO mess_emp VALUES('emp_3','padma',6777321980,'7000')")
conn.commit()

conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute("INSERT INTO wardens VALUES('warden_1','geeta',9874521997,19000)")
c.execute("INSERT INTO wardens VALUES('warden_2','asha',8775455987,19000)")
c.execute("INSERT INTO wardens VALUES('warden_3','sandhya',7664339876,19000)")
conn.commit()


c.execute("INSERT INTO room VALUES(201,1,2,0)")
c.execute("INSERT INTO room VALUES(202,1,2,0)")
c.execute("INSERT INTO room VALUES(203,1,2,0)")
c.execute("INSERT INTO room VALUES(204,1,2,0)")
c.execute("INSERT INTO room VALUES(205,1,2,0)")
c.execute("INSERT INTO room VALUES(206,1,2,0)")
c.execute("INSERT INTO room VALUES(207,1,2,0)")
c.execute("INSERT INTO room VALUES(208,1,2,0)")
c.execute("INSERT INTO room VALUES(209,1,2,0)")
c.execute("INSERT INTO room VALUES(210,1,2,0)")
c.execute("INSERT INTO room VALUES(211,1,2,0)")
c.execute("INSERT INTO room VALUES(212,1,2,0)")
c.execute("INSERT INTO room VALUES(213,1,2,0)")
c.execute("INSERT INTO room VALUES(214,1,2,1)")
c.execute("INSERT INTO room VALUES(215,1,2,0)")
c.execute("INSERT INTO room VALUES(216,1,2,0)")
c.execute("INSERT INTO room VALUES(217,1,2,0)")
c.execute("INSERT INTO room VALUES(218,1,2,0)")
c.execute("INSERT INTO room VALUES(219,1,2,0)")
c.execute("INSERT INTO room VALUES(220,1,2,0)")
c.execute("INSERT INTO room VALUES(301,2,3,0)")
c.execute("INSERT INTO room VALUES(302,2,3,0)")
c.execute("INSERT INTO room VALUES(303,2,3,0)")
c.execute("INSERT INTO room VALUES(304,2,3,0)")
c.execute("INSERT INTO room VALUES(305,2,3,0)")
c.execute("INSERT INTO room VALUES(306,2,3,0)")
c.execute("INSERT INTO room VALUES(307,2,3,0)")
c.execute("INSERT INTO room VALUES(308,2,3,0)")
c.execute("INSERT INTO room VALUES(309,2,3,0)")
c.execute("INSERT INTO room VALUES(310,2,3,0)")
c.execute("INSERT INTO room VALUES(311,2,3,0)")
c.execute("INSERT INTO room VALUES(312,2,3,0)")
c.execute("INSERT INTO room VALUES(313,2,3,0)")
c.execute("INSERT INTO room VALUES(314,2,3,0)")
c.execute("INSERT INTO room VALUES(315,2,3,0)")
c.execute("INSERT INTO room VALUES(316,2,3,0)")
c.execute("INSERT INTO room VALUES(317,2,3,0)")
c.execute("INSERT INTO room VALUES(318,2,3,0)")
c.execute("INSERT INTO room VALUES(319,2,3,0)")
c.execute("INSERT INTO room VALUES(320,2,3,0)")
c.execute("INSERT INTO room VALUES(401,3,4,0)")
c.execute("INSERT INTO room VALUES(402,3,4,0)")
c.execute("INSERT INTO room VALUES(403,3,4,0)")
c.execute("INSERT INTO room VALUES(404,3,4,0)")
c.execute("INSERT INTO room VALUES(405,3,4,0)")
c.execute("INSERT INTO room VALUES(406,3,4,0)")
c.execute("INSERT INTO room VALUES(407,3,4,0)")
c.execute("INSERT INTO room VALUES(408,3,4,0)")
c.execute("INSERT INTO room VALUES(409,3,4,0)")
c.execute("INSERT INTO room VALUES(410,3,4,0)")
c.execute("INSERT INTO room VALUES(411,3,4,0)")
c.execute("INSERT INTO room VALUES(412,3,4,0)")
c.execute("INSERT INTO room VALUES(413,3,4,0)")
c.execute("INSERT INTO room VALUES(414,3,4,0)")
c.execute("INSERT INTO room VALUES(415,3,4,0)")
c.execute("INSERT INTO room VALUES(416,3,4,0)")
c.execute("INSERT INTO room VALUES(417,3,4,0)")
c.execute("INSERT INTO room VALUES(418,3,4,0)")
c.execute("INSERT INTO room VALUES(419,3,4,0)")
c.execute("INSERT INTO room VALUES(420,3,4,1)")
conn=sqlite3.connect('hostel.db')
c=conn.cursor()
c.execute("INSERT INTO block VALUES(1,'warden_1','geeta',20,40,2)")
c.execute("INSERT INTO block VALUES(2,'warden_2','asha',20,60,3)")
c.execute("INSERT INTO block VALUES(3,'warden_3','sandhya',20,80,4)")
conn.commit()'''


class hostelapp(tk.Tk):         
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self,default="images_0UU_icon.ico")
        tk.Tk.wm_title(self,"Girls Hostel")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        b1=tk.Button(self,text="Quit",fg="black",bg="white",relief="raised",width=5,font=Sm_F,command=lambda:self.destroy())
        b1.place(x=1260,y=10)
        self.frames = {}
        
        for F in (LoginPage,FirstPage): 
            frame = F(container,self)
            self.frames[F]= frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(LoginPage)     

   
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

    def get_page(self,page_class):
        return self.frames[page_class]

     
class LoginPage(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)
        load = Image.open("VJEC-St-Alphonsa-Hostel-3.jpg")
        render = ImageTk.PhotoImage(load)   
        img = tk.Label(image=render)        
        img.image = render
        c1 = tk.Canvas(self)       
        c1.pack(fill="both", expand=True)
        c1.create_image(0,0,image = img.image,anchor = "nw")
        c1.create_text(660,410, text="Login",font = Large_F) 
        c1.create_text(540,470, text="WardenId",font = Sm_F)
        c1.create_text(540,530, text="Password",font = Sm_F)
        E1 = tk.Entry(self, state="normal", font=Sm_F,width=20, bd=3) 
        E2 = tk.Entry(self, state="normal",font=Sm_F, width=20, bd=3, show="*")
        E1.focus_set() 
        E1.place(x=660, y=460)  
        E2.place(x=660, y=520)
        B2 =tk.Button(self, text="Forgot Password?",bg="white",justify="left",font=V_S_F,fg="red",relief="flat",command=lambda:forgot_info(E1.get()))
        B2.place(x=480, y=570)
        B1 =tk.Button(self, text="Login",font=Sm_F,fg="black",bg="gray78",relief="raised",width=10,command=lambda:user_info(E1,E2))
        B1.place(x=680, y=570)
    
        
        def user_info(E1,E2):
                conn=sqlite3.connect('hostel.db')
                c=conn.cursor()
                find_5=("select date('now')")
                c.execute(find_5)
                res_1=c.fetchone()
                find_4=("select s_id from fees where due_date<?")
                c.execute(find_4,[(res_1[0])])
                result_1=c.fetchall()
                n_list=[int(i[0]) for i in result_1]
                w='unpaid'
                for i in range(len(n_list)):
                    c.execute("UPDATE fees set status=? where s_id=?",(w,n_list[i]))
                    conn.commit()
                f=E1.get()
                g=E2.get()
                find=("select * from login WHERE WardenId=? AND Password=?")
                c.execute(find,[(f),(g)])
                result=c.fetchall()
                if result:
                    controller.show_frame(FirstPage)

                else:
                    tm.showerror('login','username or password is incorrect')
                c.close()
                conn.close()
                E1.delete(0,'end')
                E2.delete(0,'end')

        def forgot_info(f):
                t13=tk.Toplevel()
                t13.title("Forgot password")
                t13.geometry("600x400")
                t13.configure(bg="white")
                E1.delete(0,'end')
                E2.delete(0,'end')
                sq=tk.Label(t13,text="Warden Id",font=Sm_F,fg="black",bg="white",anchor='w')
                sq.place(x=80,y=70)
                Eq=tk.Entry(t13,font=V_S_F,bd=3,fg="black",bg="white",width=20)
                Eq.focus_set()
                Eq.place(x=300,y=70)
                s1=tk.Label(t13,text="Security Question",font=Sm_F,fg="black",bg="white",anchor='w')
                s1.place(x=80,y=120)
                s2=tk.Label(t13,text="Answer",font=Sm_F,fg="black",bg="white",anchor='w')
                s2.place(x=80,y=170)
                s2=tk.Label(t13,text="What is your date of birth?",font=Sm_F,fg="black",bg="white",anchor='w')
                l2=tk.Label(t13,text="(yyyy-mm-dd)",font=Sm_F,fg="gray41",bg="white",anchor='w')
                l2.place(x=470,y=170)
                s2.place(x=300,y=120)
                Es=tk.Entry(t13,font=V_S_F,bd=3,fg="black",bg="white",width=20)
                Es.focus_set()
                Es.place(x=300,y=170)
                


                def fetch():
                    p=Es.get()
                    q=Eq.get()
                    
                    conn=sqlite3.connect('hostel.db')
                    c=conn.cursor()
                    c.execute("select WardenId from login where WardenId=?", (q,))
                    resw=c.fetchall()
                    if resw:
                        c.execute("SELECT Password from login WHERE answer=? AND WardenId=?",(p,q))
                        result1=c.fetchone()
                        if result1:
                            E1.insert(0,q)
                            E2.insert(0,result1[0])
                            t13.destroy()
                        else:
                            tm.showerror('login','Wrong Answer',parent=t13)
                    else:
                        tm.showerror('login','Warden Id not found',parent=t13)
                        
                
                B1=tk.Button(t13,text="Submit",font=Sm_F,fg="black",width=10,bg="gray88",relief="raised",command=lambda:fetch())
                B1.place(x=200,y=250)
                
class FirstPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        load = Image.open("newlogo.png")
        render = ImageTk.PhotoImage(load)   
        img = tk.Label(image=render)        
        img.image = render
        c1 = tk.Canvas(self)       
        c1.pack(fill="both", expand=True)
        c1.configure(bg="gray72")
        c1.create_image(35,15,image = img.image,anchor ="nw")
        c1.create_text(750,80,text="Classic Hostel",font=VV_LARGE_F)
        c1.create_line(0,180,1800,180,fill="black")
        but1=tk.Button(self,text="New Student",width=25,height=2,font=Sm_F,fg="black",bg="gray72",relief="raised",command=lambda:new_stud())
        but1.place(x=14,y=187)
        but2=tk.Button(self,text="Existing Student",width=25,height=2,font=Sm_F,fg="black",bg="gray72",relief="raised",command=lambda:exist_stud()) 
        but3=tk.Button(self,text="Visitors",width=25,height=2,font=Sm_F,fg="black",bg="gray72",relief="raised",command=lambda:visitors())
        but4=tk.Button(self,text="Outings",width=25,height=2,font=Sm_F,fg="black",bg="gray72",relief="raised",command=lambda:outings())
        but5=tk.Button(self,text="Fees Renewal",width=25,height=2,font=Sm_F,fg="black",bg="gray72",relief="raised",command=lambda:Fees())
        but6=tk.Button(self,text="Mess Employee",width=25,height=2,font=Sm_F,fg="black",bg="gray72",relief="raised",command=lambda:mess_employee())
        but7=tk.Button(self,text="Warden",width=25,height=2,font=Sm_F,fg="black",bg="gray72",relief="raised",command=lambda:warden_employee())
        but8=tk.Button(self,text="Logout",width=25,height=2,font=Sm_F,fg="black",bg="gray72",relief="raised",command=lambda:controller.show_frame(LoginPage))
        c1.create_line(290,181,290,700,fill="black")
        but2.place(x=14,y=252)
        but3.place(x=14,y=317)
        but4.place(x=14,y=381)
        but5.place(x=14,y=442)
        but6.place(x=14,y=506)
        but7.place(x=14,y=570)
        but8.place(x=14,y=634)
        load = Image.open("NIE-ADMN_BLOCK(4).jpg")
        render = ImageTk.PhotoImage(load)   
        img = tk.Label(image=render)        
        img.image = render
        c1.create_image(302,183,image = img.image,anchor ="nw")
                   
        def new_stud():
            top1=tk.Toplevel()
            top1.title("New Student")
            top1.geometry("1920x1080")
            can1=tk.Canvas(top1)
            can1.pack(fill="both",expand=True)
            load = Image.open("greylight.jpg")
            render = ImageTk.PhotoImage(load)   
            img = tk.Label(image=render)        
            img.image = render
            can1.create_image(0,0,image = img.image,anchor = "nw")
        
            
            
            def comm():
                conn=sqlite3.connect('hostel.db')
                c=conn.cursor()
                c.execute("PRAGMA foreign_keys = ON")
                q1=p1.get()
                q2=p2.get()
                q3=p3.get()
                q4=p4.get()
                q5=p5.get()
                q6=p6.get()
                q7=p7.get()
                q8=p8.get()
                q9=p9.get()
                q10=p10.get()
                c.execute("INSERT INTO student(s_name,g_name,mob_no,DOB,age,area,city,state,sem,branch) values(?,?,?,?,?,?,?,?,?,?)",(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10))
                ss=c.lastrowid
                conn.commit()
                c.close()
                conn.close()
                guardian(ss)
            
            def guardian(ss):
                    top2=tk.Toplevel()
                    top2.title("Guardian")
                    top2.geometry("1920x1080")
                    can2=tk.Canvas(top2)
                    can2.pack(fill="both",expand=True)
                    load = Image.open("greylight.jpg")
                    render = ImageTk.PhotoImage(load)   
                    img = tk.Label(image=render)        
                    img.image = render
                    can2.create_image(0,0,image = img.image,anchor = "nw")
                    conn=sqlite3.connect('hostel.db')
                    c=conn.cursor()
                    can2.create_text(670,30,text="Guardian Information",font=Large_F)
                    can2.create_text(470,100, text="Student Id",font = Sm_F,anchor='w')
                    can2.create_text(470,150, text="Guardian Name",font = Sm_F,anchor='w')
                    can2.create_text(470,200, text="Mobile Number",font = Sm_F,anchor='w')
                    can2.create_text(470,250, text="Email Id",font = Sm_F,anchor='w')
                    q= tk.Label(top2,bg="gray73",text=ss,font=Sm_F,fg="black")
                    o3=tk.Entry(top2,state="normal",font=V_S_F,width=20,bd=3)
                    o4=tk.Entry(top2,state="normal",font=V_S_F,width=20,bd=3)
                    o5=tk.Entry(top2,state="normal",font=V_S_F,width=20,bd=3)
                    q.place(x=710,y=88)
                    o3.place(x=710,y=140)
                    o4.place(x=710,y=190)
                    o5.place(x=710,y=240)
                    B10=tk.Button(top2, text="Next",font=Sm_F,fg="black",bg="white",relief="raised",width=10,command=lambda:sub())
                    B10.place(x=580, y=300)

                    conn.commit()               
                    c.close()
                    conn.close()
                    

                    def sub():
                        
                        j1=o3.get()
                        j2=o4.get()
                        j3=o5.get()
                        z=q.cget('text')
                        conn=sqlite3.connect('hostel.db')
                        c=conn.cursor()
                        c.execute("INSERT INTO guardian values(?,?,?,?)",(j1,z,j2,j3))
                        
                        conn.commit()               
                        c.close()
                        conn.close()
                        top2.destroy()
                        room(ss)
            

            def room(ss):
                top3=tk.Toplevel()
                top3.title("Room Selection")
                top3.geometry("600x400")
                top3.configure(bg="white")
                conn=sqlite3.connect('hostel.db')
                c=conn.cursor()
                c.execute("PRAGMA foreign_keys = ON")
                v2=tk.IntVar()
                v2.set(2)
                l1=tk.Label(top3,text="Make your choice",font=Nor_F,bg="white")
                l1.place(x=180,y=90)
                
               
                sharing2=tk.Radiobutton(top3,text="2 sharing",fg="black",variable=v2,value=2,font=30,bg="white")
                sharing3=tk.Radiobutton(top3,text="3 sharing",fg="black",variable=v2,value=3,font=30,bg="white")
                sharing4=tk.Radiobutton(top3,text="4 sharing",fg="black",variable=v2,value=4,font=30,bg="white")
                sharing2.place(x=200,y=150)
                sharing3.place(x=200,y=180)
                sharing4.place(x=200,y=210)
                
                def combine(B2,ss):
                    B2.destroy()
                    B9=tk.Button(top1, text="Next",font=Sm_F,bg="white",fg="black",relief="raised",width=10,command=lambda:top1.destroy())
                    B9.place(x=580,y=640)

                    X=v2.get()
                    show_room(X,ss)
                    top3.destroy()

                    
                B11=tk.Button(top3, text="Next",font=Sm_F,bg="gray84",fg="black",relief="raised",width=10,command=lambda:combine(B2,ss) )
                B11.place(x=200,y=280)

                conn.commit()
                c.close()
                conn.close()

                
           
            
            can1.create_text(670,30,text="Student Information",font=Large_F)
            can1.create_text(470,100, text="Student Name",font = Sm_F,anchor='w')
            can1.create_text(470,150, text="Father Name",font = Sm_F,anchor='w')
            can1.create_text(470,200, text="Student PhoneNumber",font = Sm_F,anchor='w')
            can1.create_text(470,250, text="Date of birth",font = Sm_F,anchor='w')
            can1.create_text(470,300, text="Age",font = Sm_F,anchor='w')
            can1.create_text(470,350, text="Area",font = Sm_F,anchor='w')
            can1.create_text(470,400, text="City",font = Sm_F,anchor='w')
            can1.create_text(470,450, text="State",font = Sm_F,anchor='w')
            can1.create_text(470,500, text="Sem",font = Sm_F,anchor='w')
            can1.create_text(470,550, text="Branch",font = Sm_F,anchor='w')
            p1=tk.Entry(top1,state="normal",font=V_S_F,width=20,bd=3)
            p2=tk.Entry(top1,state="normal",font=V_S_F,width=20,bd=3)
            p3=tk.Entry(top1,state="normal",font=V_S_F,width=20,bd=3)
            p4=tk.Entry(top1,state="normal",font=V_S_F,width=20,bd=3)
            p5=tk.Entry(top1,state="normal",font=V_S_F,width=20,bd=3)
            p6=tk.Entry(top1,state="normal",font=V_S_F,width=20,bd=3)
            p7=tk.Entry(top1,state="normal",font=V_S_F,width=20,bd=3)
            p8=tk.Entry(top1,state="normal",font=V_S_F,width=20,bd=3)
            p9=tk.Entry(top1,state="normal",font=V_S_F,width=20,bd=3)
            p10=tk.Entry(top1,state="normal",font=V_S_F,width=20,bd=3)
            p1.place(x=710,y=90)
            p2.place(x=710,y=140)
            p3.place(x=710,y=190)
            p4.place(x=710,y=240)
            p5.place(x=710,y=290)
            p6.place(x=710,y=340)
            p7.place(x=710,y=390)
            p8.place(x=710,y=440)
            p9.place(x=710,y=490)
            p10.place(x=710,y=540)
            B2=tk.Button(top1, text="Next",font=Sm_F,fg="black",bg="white",relief="raised",width=10,command=lambda:comm())
            B2.place(x=580, y=610)
            B3=tk.Button(top1, text="Back",font=Sm_F,fg="black",bg="white",relief="raised",width=5,command=lambda:top1.destroy())
            B3.place(x=1260,y=10)




            def show_room(f1,ss):
                top4=tk.Toplevel()
                top4.title("Room Selection")
                top4.geometry("1000x1200")
                top4.configure(bg="white")
                
                conn=sqlite3.connect('hostel.db')
                c1=conn.cursor()
                c1.execute("PRAGMA foreign_keys = ON")
                label=tk.Label(top4,text="Choose your room",font=Nor_F,bg="white")
                label.place(x=100,y=35)
                
                find3=("select room_no from room where room_capacity=? and Occupied<?")
                c1.execute(find3,[(f1),(f1)])
                result1=c1.fetchall()
                
                u={}
                b={}
                j=0
                u=tk.StringVar()
                for i,index in enumerate(result1):
                    
                    b[i]=tk.Radiobutton(top4,text=index[0],bg="white",font=15,variable=u,value=(i+1)).place(x=100,y=70+j)
                    j=j+25
                def comp():
                    n=u.get()
                    n=int(n)
                    n=n-1
                    
                    can1.create_text(470,600, text="Room Number",font = Sm_F,anchor='w')
                    for i,index in enumerate(result1):
                            
                            h= tk.Label(top1,font=Sm_F,text=result1[n][0],bg="gray50")
                            h.place(x=710,y=590)
                    return (n,result1[n][0])
                    
                def combinex(ss):
                    conn=sqlite3.connect('hostel.db')
                    c=conn.cursor()
                    c.execute("PRAGMA foreign_keys = ON")
                    n,w=comp()
                    c.execute("UPDATE student set room_no=? where s_id=?",(w,ss))
                    
                    c.execute("UPDATE room set Occupied=Occupied+1 WHERE room_no=?" ,(w,))
                    conn.commit()
                    c.close()
                    conn.close()   
                            
                    top4.destroy()
                    fee_payment(n,ss)
                B7=tk.Button(top4, text="Next",font=Sm_F,fg="black",bg="gray83",relief="raised",width=10,command=lambda:combinex(ss))
                B7.place(x=100, y=620)   
                conn.commit()               
                c1.close()
                conn.close()
                
                def fee_payment(n,ss):
                    top5=tk.Toplevel()
                    top5.title("Fee Payment")
                    top5.geometry("800x600")
                    top5.configure(bg="white")
                    conn=sqlite3.connect('hostel.db')
                    c=conn.cursor()
                    l1=tk.Label(top5,text="Fee Payment",font=Nor_F,bg="white")
                    l1.place(x=300,y=25)
                    l2=tk.Label(top5,text="Student id         : ",font=Sm_F,bg="white")
                    l2.place(x=220,y=90)
                    l3=tk.Label(top5,text=ss,font=Sm_F,bg="white")
                    l3.place(x=440,y=90)
                    r11=l3.cget('text')
                    for i,index in enumerate(result1):
                            l3=tk.Label(top5, text="Room Number    :",font = Sm_F,bg="white")
                            l3.place(x=220,y=120) 
                            l4= tk.Label(top5,font=Sm_F,text=result1[n][0],bg="white")
                            l4.place(x=440,y=120)
                    r2=result1[n][0]
                    l5=tk.Label(top5, text="Paid Date          : ",font = Sm_F,bg="white")
                    l5.place(x=220,y=150)
                    find5=("select date('now')")
                    c.execute(find5)
                    res=c.fetchone()
                    v1=tk.StringVar()
                    v1.set(res)
                    r_2=v1.get()
                    r7=r_2[2:-3]
                    l6=tk.Label(top5, textvariable=v1,font = Sm_F,bg="white")
                    l6.place(x=440,y=150)
                    l7=tk.Label(top5, text="Due Date          :",font = Sm_F,bg="white")
                    l7.place(x=220,y=180)
                    find6=("select date('now','+1 year')")
                    c.execute(find6)
                    resu=c.fetchone()
                    v2=tk.StringVar()
                    v2.set(resu)
                    r_1=v2.get()
                    r6=r_1[2:-3]
                    l8=tk.Label(top5, textvariable=v2,font = Sm_F,bg="white")
                    l8.place(x=440,y=180)
                    CheckVar1=tk.StringVar()
                    ch1 = tk.Checkbutton(top5, text = "Paid",bg="white",font=19, variable = CheckVar1,command=lambda:ammount(ch1,top5,r11,r2,r6,r7),onvalue = 1,  offvalue = 0 )
                    ch1.place(x=220,y=300)
                    
                def ammount(ch1,top5,r11,r2,r6,r7):
                    r8=''
                    r8=ch1.cget("text")
                    ch1.config(state="disabled")
                    val=tk.IntVar()
                    val1=tk.IntVar()
                    val_final=tk.IntVar()
                    if f1==2:
                        conn=sqlite3.connect('hostel.db')
                        c=conn.cursor()
                        amm=40000
                        amm1=8000
                        val.set(amm)
                        val1.set(amm1)
                        L1=tk.Label(top5, textvariable=val,font = Sm_F,bg="white")
                        L1.place(x=440,y=210)
                        L2=tk.Label(top5, textvariable=val1,font = Sm_F,bg="white")
                        L2.place(x=440,y=240)
                        newval=val.get()+val1.get()
                        val_final.set(newval)
                        L3=tk.Label(top5, textvariable=val_final,font = Sm_F,bg="white")
                        L3.place(x=440,y=270)
                        r3=1
                        c.execute("INSERT INTO fees(s_id,room_no,block_id,rent,mess_expense,due_date,paid_date,status) values(?,?,?,?,?,?,?,?)",(r11,r2,r3,amm,amm1,r6,r7,r8))
                        conn.commit()
                    elif f1==3:
                        conn=sqlite3.connect('hostel.db')
                        c=conn.cursor()
                        amm=20000
                        amm1=8000
                        val.set(amm)
                        val1.set(amm1)
                        L1=tk.Label(top5, textvariable=val,font = Sm_F,bg="white")
                        L1.place(x=440,y=210)
                        L2=tk.Label(top5, textvariable=val1,font = Sm_F,bg="white")
                        L2.place(x=440,y=240)
                        newval=val.get()+val1.get()
                        val_final.set(newval)
                        L3=tk.Label(top5, textvariable=val_final,font = Sm_F,bg="white")
                        L3.place(x=440,y=270)
                        r3=2
                        c.execute("INSERT INTO fees(s_id,room_no,block_id,rent,mess_expense,due_date,paid_date,status) values(?,?,?,?,?,?,?,?)",(r11,r2,r3,amm,amm1,r6,r7,r8))
                        conn.commit()
                    elif f1==4:
                        conn=sqlite3.connect('hostel.db')
                        c=conn.cursor()
                        amm=10000
                        amm1=8000
                        val.set(amm)
                        val1.set(amm1)
                        L1=tk.Label(top5, textvariable=val,font = Sm_F,bg="white")
                        L1.place(x=440,y=210)
                        L2=tk.Label(top5, textvariable=val,font = Sm_F,bg="white")
                        L2.place(x=440,y=240)
                        newval=val.get()+val1.get()
                        val_final.set(newval)
                        L3=tk.Label(top5, textvariable=val_final,font = Sm_F,bg="white")
                        L3.place(x=440,y=270)
                        r3=3
                        c.execute("INSERT INTO fees(s_id,room_no,block_id,rent,mess_expense,due_date,paid_date,status) values(?,?,?,?,?,?,?,?)",(r11,r2,r3,amm,amm1,r6,r7,r8))
                        conn.commit()    
                    l9=tk.Label(top5, text="Rent                 : ",font = Sm_F,bg="white")
                    l9.place(x=220,y=210)
                    l10=tk.Label(top5, text="Mess Expenses   : ",font = Sm_F,bg="white")
                    l10.place(x=220,y=240)
                    l11=tk.Label(top5, text="Total fees          : ",font = Sm_F,bg="white")
                    l11.place(x=220,y=270)
                    b1=tk.Button(top5, text="Finish",font=Sm_F,bg="gray92",fg="black",relief="raised",width=10,command=lambda:finalise(top5,r11))
                    b1.place(x=300, y=370)
                def finalise(top5,r11):
                    c.close
                    conn.close()
                    top5.destroy()
                    top1.destroy()
                                

  

            
        def exist_stud():
            top6=tk.Toplevel()
            top6.title("Existing Student")
            top6.geometry("1920x1080")
            can2=tk.Canvas(top6)
            can2.pack(fill="both",expand=True)
            load = Image.open("greylight.jpg")
            render = ImageTk.PhotoImage(load)   
            img = tk.Label(image=render)        
            img.image = render
            can2.create_image(0,0,image = img.image,anchor = "nw")
            can2.create_text(670,30,text="Student information",font=Large_F)
            can2.create_text(470,100, text="Student Id",font = Sm_F,anchor='w')
            can2.create_text(470,150, text="Student Name",font = Sm_F,anchor='w')
            can2.create_text(470,200, text="Mobile Number",font = Sm_F,anchor='w')
            can2.create_text(470,250, text="Father Name",font = Sm_F,anchor='w')
            can2.create_text(470,300, text="Date of birth",font = Sm_F,anchor='w')
            can2.create_text(470,350, text="Sem",font = Sm_F,anchor='w')
            can2.create_text(470,400, text="Branch",font = Sm_F,anchor='w')
            can2.create_text(470,450, text="Age",font = Sm_F,anchor='w')
            can2.create_text(470,500, text="Area",font = Sm_F,anchor='w')
            can2.create_text(470,550, text="City",font = Sm_F,anchor='w')
            can2.create_text(470,600, text="State",font = Sm_F,anchor='w')
            d1=tk.Entry(top6,state="normal",font=V_S_F,width=20,bd=3)
            d1.focus_set()
            d1.place(x=710,y=90)
            
            
            B3=tk.Button(top6, text="Back",font=Sm_F,fg="black",bg="white",relief="raised",width=5,command=lambda:top6.destroy())
            B3.place(x=1260,y=10)
            
            B2=tk.Button(top6, text="Fetch",font=Sm_F,fg="black",bg="white",relief="raised",width=10,command=lambda:fetching())
            B2.place(x=550, y=620)
            
            def fetching():
                conn=sqlite3.connect('hostel.db')
                c=conn.cursor()
                c.execute("PRAGMA foreign_keys = ON")
                a=d1.get()
                
                find2=("select * from student WHERE s_id=?")
                c.execute(find2,[(a)])
                result2=c.fetchall()
                if result2:
                    for i,index in enumerate(result2):
                        
                        n1= tk.Label(top6,font=Sm_F,text=a,bg="gray73")
                        n1.place(x=710,y=88)
                        y=n1.cget('text')
                        p2=tk.Entry(top6,state="normal",font=V_S_F,width=20,bd=3)
                        l=p2.insert(0,index[1])
                        p3=tk.Entry(top6,state="normal",font=V_S_F,width=20,bd=3)
                        m=p3.insert(0,index[2])
                        p4=tk.Entry(top6,state="normal",font=V_S_F,width=20,bd=3)
                        n=p4.insert(0,index[3])
                        p5=tk.Entry(top6,state="normal",font=V_S_F,width=20,bd=3)
                        o=p5.insert(0,index[4])
                        p6=tk.Entry(top6,state="normal",font=V_S_F,width=20,bd=3)
                        p=p6.insert(0,index[5])
                        p7=tk.Entry(top6,state="normal",font=V_S_F,width=20,bd=3)
                        q=p7.insert(0,index[6])
                        p8=tk.Entry(top6,state="normal",font=V_S_F,width=20,bd=3)
                        r=p8.insert(0,index[7])
                        p9=tk.Entry(top6,state="normal",font=V_S_F,width=20,bd=3)
                        s=p9.insert(0,index[8])
                        p10=tk.Entry(top6,state="normal",font=V_S_F,width=20,bd=3)
                        t=p10.insert(0,index[9])
                        p11=tk.Entry(top6,state="normal",font=V_S_F,width=20,bd=3)
                        u=p11.insert(0,index[10])
                        p2.place(x=710,y=140)
                        p3.place(x=710,y=190)
                        p4.place(x=710,y=240)
                        p5.place(x=710,y=290)
                        p6.place(x=710,y=340)
                        p7.place(x=710,y=390)
                        p8.place(x=710,y=440)
                        p9.place(x=710,y=490)
                        
                        p10.place(x=710,y=540)
                        p11.place(x=710,y=590)
                        B2.destroy()
                        d1.destroy()
                        B5=tk.Button(top6, text="Update",font=Sm_F,bg="white",fg="black",relief="raised",width=10,command=lambda:updating())
                        B5.place(x=520, y=630)
                        B6=tk.Button(top6, text="Vacate",font=Sm_F,bg="white",fg="black",relief="raised",width=10,command=lambda:dele())
                        B6.place(x=720, y=630)
                else:
                        tm.showerror('Existing Student','Student Id not found',parent=top6)
                conn.commit()
                c.close()
                conn.close()
                def updating():
                    conn=sqlite3.connect('hostel.db')
                    c=conn.cursor()
                    c.execute("PRAGMA foreign_keys = ON")
                    c.execute("UPDATE student SET s_name=(?),mob_no=(?),g_name=(?),DOB=(?),sem=(?),branch=(?),age=(?),area=(?),city=(?),state=(?) WHERE s_id=?",(p2.get(),p3.get(),p4.get(),p5.get(),p6.get(),p7.get(),p8.get(),p9.get(),p10.get(),p11.get(),y))
                    conn.commit()
                    c.close()
                    conn.close()
                    top6.destroy()
                def dele():
                    conn=sqlite3.connect('hostel.db')
                    c=conn.cursor()
                    c.execute("PRAGMA foreign_keys = ON")
                    
                    c.execute("UPDATE room set Occupied=Occupied-1 WHERE room_no=(select room_no from student WHERE s_id=?)",(y,))
                    c.execute("DELETE FROM student WHERE s_id=?", (y,))
                    conn.commit()
                    c.close()
                    conn.close()
                    top6.destroy()

            
                



            
        
        def warden_employee():
    
            top7=tk.Toplevel()
            top7.title("Wardens")
            top7.geometry("1920x1080")
            can3=tk.Canvas(top7)
            can3.pack(fill="both",expand=True)
            load = Image.open("greylight.jpg")
            render = ImageTk.PhotoImage(load)   
            img = tk.Label(image=render)        
            img.image = render
            can3.create_image(0,0,image = img.image,anchor = "nw")
            
            can3.create_text(670,30,text="Warden Information",font=Large_F)
            can3.create_text(470,100, text="Warden Id",font = Sm_F,anchor='w')
            x=tk.Entry(top7,state="normal",font=V_S_F,width=20,bd=3)
            x.place(x=710,y=90)
            x.focus_set()
            B20=tk.Button(top7, text="Back",font=Sm_F,bg="white",fg="black",relief="raised",width=5,command=lambda:top7.destroy())
            B20.place(x=1260,y=10)
            
            
            def com1(B6):
                conn=sqlite3.connect('hostel.db')
                c=conn.cursor()
                c.execute("PRAGMA foreign_keys = ON")
                y=x.get()
                find6=("SELECT * from wardens where warden_id=?")
                c.execute(find6,[(y)])
                result3=c.fetchall()
                if result3:
                    B6.destroy()
                    x.destroy()
                    can3.create_text(470,100, text="Warden Id",font = Sm_F,anchor='w')
                    can3.create_text(470,150, text="Warden Name",font = Sm_F,anchor='w')
                    can3.create_text(470,200, text="Warden PhoneNumber",font = Sm_F,anchor='w')
                    can3.create_text(470,250, text="Salary",font = Sm_F,anchor='w')
                    r1=tk.Label(top7,text=result3[0][0],bg="gray72",font = Sm_F)
                    r1.place(x=710,y=90)
                    r2=tk.Label(top7,text=result3[0][1],bg="gray73",font = Sm_F)
                    r2.place(x=710,y=140)
                    r3=tk.Label(top7,text=result3[0][2],bg="gray69",font = Sm_F)
                    r3.place(x=710,y=190)
                    r4=tk.Label(top7,text=result3[0][3],bg="gray69",font = Sm_F)
                    r4.place(x=710,y=240)
                    B6=tk.Button(top7, text="Next",font=Sm_F,bg="white",fg="black",relief="raised",width=10,bd=3,command=lambda:top7.destroy())
                    B6.place(x=570,y=340)
                    conn.commit()
                    c.close()
                    conn.close()
                else:
                    tm.showerror('Wardens','Warden Id not found',parent=top7)
                
            B6=tk.Button(top7, text="Fetch",bg="white",font=Sm_F,fg="black",relief="raised",width=10,bd=3,command=lambda:com1(B6))
            B6.place(x=550,y=420)
                
        
        
        
        def mess_employee():
            top8=tk.Toplevel()
            top8.title("Mess Employees")
            top8.geometry("1920x1080")
            can4=tk.Canvas(top8)
            can4.pack(fill="both",expand=True)
            load = Image.open("greylight.jpg")
            render = ImageTk.PhotoImage(load)   
            img = tk.Label(image=render)        
            img.image = render
            can4.create_image(0,0,image = img.image,anchor = "nw")
    
            can4.create_text(670,30,text="Mess Information",font=Large_F)
            can4.create_text(470,100, text="Emp Id",font = Sm_F,anchor='w')
            x=tk.Entry(top8,state="normal",font=V_S_F,width=20,bd=3)
            x.place(x=710,y=90)
            x.focus_set()
            B22=tk.Button(top8, text="Back",font=Sm_F,bg="white",fg="black",relief="raised",width=5,command=lambda:top8.destroy())
            B22.place(x=1260,y=10)
            
            
            def com2(B7):
                conn=sqlite3.connect('hostel.db')
                c=conn.cursor()
                y=x.get()
                find7=("SELECT * from mess_emp where emp_id=?")
                c.execute(find7,[(y)])
                result5=c.fetchall()
                if result5:
                    B7.destroy()
                    x.destroy()
                    can4.create_text(470,100, text="Emp Id",font = Sm_F,anchor='w')
                    can4.create_text(470,150, text="Emp Name",font = Sm_F,anchor='w')
                    can4.create_text(470,200, text="Mobile Number",font = Sm_F,anchor='w')
                    can4.create_text(470,250, text="Salary",font = Sm_F,anchor='w')
                    k1=tk.Label(top8,text=result5[0][0],bg="gray72",font = Sm_F)
                    k1.place(x=710,y=90)
                    k2=tk.Label(top8,text=result5[0][1],bg="gray73",font = Sm_F)
                    k2.place(x=710,y=140)
                    k3=tk.Label(top8,text=result5[0][2],bg="gray69",font = Sm_F)
                    k3.place(x=710,y=190)
                    k4=tk.Label(top8,text=result5[0][3],bg="gray69",font = Sm_F)
                    k4.place(x=710,y=240)
                    B7=tk.Button(top8, text="Next",font=Sm_F,bg="white",fg="black",relief="raised",width=10,bd=3,command=lambda:top8.destroy())
                    B7.place(x=570,y=340)
                    conn.commit()
                    c.close()
                    conn.close()
                else:
                    tm.showerror('Mess Employee','Employee Id not found',parent=top8)
                
            B7=tk.Button(top8, text="Fetch",font=Sm_F,bg="white",fg="black",relief="raised",width=10,bd=3,command=lambda:com2(B7))
            B7.place(x=550,y=420)  

        def visitors():
            top9=tk.Toplevel()
            top9.title("Visitors")
            top9.geometry("1920x1080")
            can5=tk.Canvas(top9)
            can5.pack(fill="both",expand=True)
            load = Image.open("greylight.jpg")
            render = ImageTk.PhotoImage(load)   
            img = tk.Label(image=render)        
            img.image = render
            can5.create_image(0,0,image = img.image,anchor = "nw")

            can5.create_text(670,30,text="Student Information",font=Large_F)
            can5.create_text(470,100,text="Student Id",font=Sm_F,anchor='w')
            can5.create_text(470,150,text="Visitors Name",font=Sm_F,anchor='w')
            can5.create_text(470,200,text="Relationship",font=Sm_F,anchor='w')
            y1=tk.Entry(top9,state="normal",font=V_S_F,width=20,bd=3)
            y2=tk.Entry(top9,state="normal",font=V_S_F,width=20,bd=3)
            y3=tk.Entry(top9,state="normal",font=V_S_F,width=20,bd=3)
            y1.focus_set()
            y1.place(x=710,y=90)
            y2.place(x=710,y=140)
            y3.place(x=710,y=190)
            def combine5():
                comm1(y1.get(),y2.get(),y3.get())
                top9.destroy()

            btn7=tk.Button(top9,text="Finish",bg="white",font=Sm_F,width=10,bd=3,command=lambda:combine5())
            btn7.place(x=570,y=310)
            B3=tk.Button(top9, text="Back",font=Sm_F,bg="white",fg="black",relief="raised",width=5,command=lambda:top9.destroy())
            B3.place(x=1260,y=10)

            def comm1(p11,p22,p33):
                conn=sqlite3.connect('hostel.db')
                c=conn.cursor()
                c.execute("PRAGMA foreign_keys = ON")
                q11=p11
                q22=p22
                q33=p33
                find7=("select s_id from student where s_id=?")
                c.execute(find7,[(q11)])
                result8=c.fetchall()
                c.close()
                conn.close()
                
                if result8:
                    conn=sqlite3.connect('hostel.db')
                    c=conn.cursor()
                    c.execute("PRAGMA foreign_keys = ON")
                    c.execute("INSERT INTO visitors(s_id,v_name,relationship) values(?,?,?)",(q11,q22,q33))
                    conn.commit()
                    c.close()
                    conn.close()
                else:
                    tm.showerror('Visitors','Student Id not found',parent=top9)


        
        def outings():
        
            top10=tk.Toplevel()
            top10.title("Outings")
            top10.geometry("1920x1080")
            can6=tk.Canvas(top10)
            can6.pack(fill="both",expand=True)
            load = Image.open("greylight.jpg")
            render = ImageTk.PhotoImage(load)   
            img = tk.Label(image=render)        
            img.image = render
            can6.create_image(0,0,image = img.image,anchor = "nw")
            can6.create_text(720,130,text="Outings",font=Large_F)
            
            b22=tk.Button(top10,text="New Entry",width=15,height=1,font=Nor_F,fg="black",bg="white",relief="raised",command=lambda:enter_out()) 
            b33=tk.Button(top10,text="Existing Entry",width=15,height=1,font=Nor_F,fg="black",bg="white",relief="raised",command=lambda:enter_in())
            b44=tk.Button(top10,text="Send Email",width=15,height=1,font=Nor_F,fg="black",bg="white",relief="raised",command=lambda:email())
            b22.place(x=50,y=200)
            b33.place(x=50,y=270)
            b44.place(x=50,y=340)
            B24=tk.Button(top10, text="Back",font=Sm_F,bg="white",fg="black",relief="raised",width=5,command=lambda:top10.destroy())
            B24.place(x=1260,y=10)

            

            def enter_out():
                
                b33.config(state="disabled")
                b44.config(state="disabled")
                lab2=tk.Label(top10,text="StudentId",font=Nor_F,fg="black",bg="gray75")
                lab2.place(x=530,y=200)
                
                lab3=tk.Label(top10,text="Out Date",font=Nor_F,bg="gray75",fg="black")
                lab3.place(x=530,y=250)
                
                lab4=tk.Label(top10,text="Out Time",font=Nor_F,bg="gray72",fg="black")
                lab4.place(x=530,y=300)
                  
                d11=tk.Entry(top10,state="normal",font=Sm_F,width=20,bd=3)
                d22=tk.Entry(top10,state="normal",font=Sm_F,width=20,bd=3)
                d33=tk.Entry(top10,state="normal",font=Sm_F,width=20,bd=3)
                d11.place(x=750,y=203)
                d22.place(x=750,y=253)
                d33.place(x=750,y=303)
                d11.focus_set()
                btn3=tk.Button(top10,text="Submit",font=Sm_F,fg="black",bg="white",width=10,command=lambda: insert_outime(d11.get(),d22.get(),d33.get()))
                btn3.place(x=660,y=400)
                
                def insert_outime(p1,p2,p3):
                    conn=sqlite3.connect('hostel.db')
                    c=conn.cursor()
                    c.execute("select s_id from student where s_id=?",(p1,))
                    res1=c.fetchall()
                    if res1:
                        c.execute("INSERT INTO outings(s_id,o_date,out_time,in_time) values(?,?,?,?)",(p1,p2,p3,0))
                        conn.commit()
                        c.close()
                        conn.close()
                        lab2.destroy()
                        lab3.destroy()
                        lab4.destroy()
                        d11.destroy()
                        d22.destroy()
                        d33.destroy()
                        btn3.destroy()
                        b33.config(state="normal")
                        b44.config(state="normal")
                    else:
                        tm.showerror('outings','student id not found',parent=top10)
                        conn.commit()
                        c.close()
                        conn.close()
                
                    
                        
                    
            def enter_in():
                b22.config(state="disabled")
                b44.config(state="disabled")
                lab2=tk.Label(top10,text="Student Id",font=Nor_F,fg="black",bg="gray75")
                lab2.place(x=530,y=200)
                lab4=tk.Label(top10,text="In Time",font=Nor_F,fg="black",bg="gray75")
                lab4.place(x=530,y=250)
                d11=tk.Entry(top10,state="normal",font=Sm_F,width=20,bd=3)
                d22=tk.Entry(top10,state="normal",font=Sm_F,width=20,bd=3)
                d11.place(x=750,y=203)
                d22.place(x=750,y=253)
                d11.focus_set() 
                btn4=tk.Button(top10,text="Submit",font=Sm_F,fg="black",width=10,bg="white",command=lambda: insert_intime(d11.get(),d22.get()))
                btn4.place(x=660,y=350)

                def insert_intime(p1,p2):
                      
                    conn=sqlite3.connect('hostel.db')
                    c=conn.cursor()
                    c.execute("select s_id from student where s_id=?",(p1,))
                    res2=c.fetchall()
                    if res2:
                        c.execute("delete from outings where s_id=? ",(p1,))
                        conn.commit()
                        c.close()
                        conn.close()
                        lab2.destroy()
                        lab4.destroy()
                        d11.destroy()
                        d22.destroy()
                        btn4.destroy()
                        b22.config(state="normal")
                        b44.config(state="normal")
                    else:
                        tm.showerror('outings','student id not found',parent=top10)
                    


            def  email():
                b22.config(state="disabled")
                b33.config(state="disabled")
                conn=sqlite3.connect('hostel.db')
                c=conn.cursor()
                label=tk.Label(top10,text="Student Ids",font=Nor_F,fg="black",bg="gray77")
                label.place(x=450,y=200)
                find3=("select s_id from outings where in_time=?")
                c.execute(find3,[(0)])                                                                             
                result1=c.fetchall()
                         
                u={}
                b={}
                j=230
                g=[]
                v=[]

                def up(g):
                    for i in g:
                        print(i.get())
                        
                        
                for i,index in enumerate(result1):
                    v=tk.IntVar()
                    g.append(v)
                        
                    b[i]=tk.Checkbutton(top10,text=index[0],state="normal",fg="black",bg="gray76",variable=v,font=25,command=lambda:up(g),onvalue=index[0],offvalue=0)
                    b[i].place(x=450,y=j+15)
                    j+=35
                    b[i].var=v
                         
                btn5=tk.Button(top10,text="Send",font=Sm_F,width=10,bg="white",fg="black",command=lambda:send_mail(g))
                btn5.place(x=600,y=600)
                conn.commit()
                c.close()
                conn.close()
                    
                def send_mail(g):
                    btn5.destroy()
                    label.destroy()
                    for i in range(len(b)):
                           b[i].destroy()
                    b22.config(state="normal")
                    b33.config(state="normal")
                    conn=sqlite3.connect('hostel.db')
                    c=conn.cursor()
                    for i in g:
                        if(i.get()!=0):
                            
                            find5=("select g_mail_id from guardian where s_id=? ")
                            c.execute(find5,([i.get()]))
                            result2=c.fetchall()
                            
                            c.execute("select O_date,out_time from Outings where s_id=?",(i.get(),))
                            resm=c.fetchall()
                            
                            resm2=resm[0]
                            od=str(resm2[0])
                            ot=str(resm2[1])
                            c.execute("select s_name from student where s_id=?",(i.get(),))
                            snm=c.fetchone()
                            snm2=str(snm[0])
                            
                            
                            for k,index in enumerate(result2):
                                
                                gmail_user = "niegirlshostel123@gmail.com"
                                gmail_pwd = "dbmsproject"
                                TO = [index[0]]
                                SUBJECT = "Student Absence Notification-NIE girls hostel"
                                TEXT="Dear parent,\n    With reference to above subject we write to state that your daughter "+snm2+" has not been returned to the hostel.\nShe left the hostel on "+od+" at "+ot+".\n\nTHANK YOU\n"
                                    
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.ehlo()
                                server.starttls()
                                server.login(gmail_user, gmail_pwd)
                                BODY = '\r\n'.join(['To: %s' % TO,
                                        'From: %s' % gmail_user,
                                            'Subject: %s' % SUBJECT,'',TEXT])

                                server.sendmail(gmail_user, [TO], BODY)
                                tm.showinfo('Email','Email sent successfully!!',parent=top10)
                                
                    conn.commit()
                    c.close()
                    conn.close()

                    
        def Fees():
            top11=tk.Toplevel()
            top11.title("Fees")
            top11.geometry("1920x1080")
            can7=tk.Canvas(top11)
            can7.pack(fill="both",expand=True)
            load = Image.open("greylight.jpg")
            render = ImageTk.PhotoImage(load)   
            img = tk.Label(image=render)        
            img.image = render
            can7.create_image(0,0,image = img.image,anchor = "nw")
    
            can7.create_text(720,130,text="Renewal",font=Large_F)
            bu1=tk.Button(top11, text="Renewal",font=Nor_F,bg="white",fg="black",relief="raised",width=10,height=1,command=lambda:renewal())
            bu1.place(x=50,y=250)
            bu2=tk.Button(top11, text="Fee status",font=Nor_F,bg="white",fg="black",relief="raised",width=10,height=1,command=lambda:status())
            bu2.place(x=50,y=350)
            bu3=tk.Button(top11, text="Back",font=Sm_F,bg="white",fg="black",relief="raised",width=5,command=lambda:top11.destroy())
            bu3.place(x=1260,y=10)
            
            def status():
                conn=sqlite3.connect('hostel.db')
                c=conn.cursor()
                bu1.config(state="disabled")
                w='unpaid'
                find_5=("select s_id from fees where status=?")
                c.execute(find_5,[(w)])                                                                             
                result_6=c.fetchall()
                label=tk.Label(can7,text="Student Ids",font=Nor_F,fg="black",bg="gray77")
                label.place(x=500,y=200)
                u={}
                b={}
                j=230
                g=[]
                v=[]


                        
                        
                for i,index in enumerate(result_6):
                        v=tk.IntVar()
                        g.append(v)
                        b[i]=tk.Checkbutton(can7,text=index[0],state="normal",fg="black",font=25,bg="gray76",variable=v,onvalue=index[0],offvalue=0)
                        b[i].place(x=450,y=j+15)
                        j+=35
                        b[i].var=v
                         
                btn22=tk.Button(can7,text="Send",font=Sm_F,bg="white",relief="raised",width=10,command=lambda:send_mail(g))
                btn22.place(x=600,y=600)

                
                def send_mail(g):
                        bu1.config(state="normal")
                        label.destroy()
                        btn22.destroy()
                        for i in range(len(b)):
                               b[i].destroy()
                        conn=sqlite3.connect('hostel.db')
                        c1=conn.cursor()
                        for i in g:
                                 if(i.get()!=0):
                                     
                                     find5=("select g_mail_id from guardian where s_id=? ")
                                     c1.execute(find5,([i.get()]))
                                     result2=c1.fetchall()
                                     c1.execute("select rent,mess_expense,due_date from fees where s_id=?",(i.get(),))
                                     resf=c1.fetchone()
                                    
                                     ren1=resf[0]
                                     expen1=resf[1]
                                     due1=resf[2]
                                     tot1=ren1+expen1
                                     
                                     
                                     ren=str(ren1)
                                     expen=str(expen1)
                                     tot=str(tot1)
                                     due=str(due1)
                                     c1.execute("select s_name from student where s_id=?",(i.get(),))
                                     sn=c1.fetchone()
                                     nam=str(sn[0])
                                     
                                     for k,index in enumerate(result2):
                                         
                                         gmail_user = "niegirlshostel123@gmail.com"
                                         gmail_pwd = "dbmsproject"
                                         TO = [index[0]]
                                         SUBJECT = "REMINDER :Fee payment - NIE Girls Hostel"
                                         TEXT="Dear parent,\n    With reference to above subject we write to state that due date for the fee payment of your daughter "+nam+" is "+due+".\nFee details are given below.Kindly pay the fees ASAP\n\nRent                    :  "+ren+"\nMess Expense  :  "+expen+"\nTotal amount    :  "+tot+"\n\nTHANK YOU\n" 
                                         server = smtplib.SMTP('smtp.gmail.com', 587)
                                         server.ehlo()
                                         server.starttls()
                                         server.login(gmail_user, gmail_pwd)
                                         BODY = '\r\n'.join(['To: %s' % TO,
                                            'From: %s' % gmail_user,
                                            'Subject: %s' % SUBJECT,'',TEXT])

                                         server.sendmail(gmail_user, [TO], BODY)
                                         tm.showinfo('Email','Email sent successfully!!',parent=top11)              


            def renewal():
                        bu2.config(state="disabled")
                        
                        
                        lab2=tk.Label(can7,text="Student Id",font=Nor_F,fg="black",bg="gray75")
                        lab2.place(x=530,y=200)
                        e1=tk.Entry(can7,state="normal",font=Sm_F,width=20,bd=3)
                        e1.place(x=750,y=203)
                        e1.focus_set()
                        bn3=tk.Button(can7, text="Check",font=Sm_F,bg="white",fg="black",relief="raised",width=10,command=lambda:che())
                        bn3.place(x=630,y=330)
                        def che():
                            info=e1.get()
                            conn=sqlite3.connect('hostel.db')
                            c=conn.cursor()
                            c.execute("select s_id from student where s_id=?",(info,))
                            fetch1=c.fetchall()
                            if fetch1:
                                
                                find1=("select status from fees where s_id=?")
                                c.execute(find1,[(info)])
                                result_1=c.fetchone()
                                print(result_1[0])
                                if result_1[0]=='Paid':
                                          tm.showinfo('Renewal','No renewal required!!',parent=top11)
                                          lab2.destroy()
                                          e1.destroy()
                                          bn3.destroy()
                                          bu2.config(state="normal")
                                elif result_1[0]=='unpaid':
                                            find2=("select room_no,due_date,rent,mess_expense from fees where s_id=?")
                                            c.execute(find2,[(info)])                                                                             
                                            result_2=c.fetchall()
                                            n_t=result_2[0]
                                            print(n_t[0])
                                            top12=tk.Toplevel()
                                            top12.title("Renewal")
                                            top12.geometry("1920x1080")
                                            can8=tk.Canvas(top12)
                                            can8.pack(fill="both",expand=True)
                                            load = Image.open("greylight.jpg")
                                            render = ImageTk.PhotoImage(load)   
                                            img = tk.Label(image=render)        
                                            img.image = render
                                            can8.create_image(0,0,image = img.image,anchor = "nw")
                                            can8.create_text(650,50,text="Fees Renewal",font=Large_F)
                                            can8.create_text(560,130,text="Student id         :",font=Nor_F)
                                            can8.create_text(760,130,text=info,font=Nor_F)
                                            can8.create_text(560,180,text="Room no            :",font=Nor_F)
                                            can8.create_text(760,180,text=n_t[0],font=Nor_F)
                                            can8.create_text(560,230,text="Due date           :",font=Nor_F)
                                            can8.create_text(760,230,text=n_t[1],font=Nor_F)
                                            can8.create_text(560,280,text="Rent                 :",font=Nor_F)
                                            can8.create_text(760,280,text=n_t[2],font=Nor_F)
                                            can8.create_text(560,330,text="Mess Expense    :",font=Nor_F)
                                            can8.create_text(760,330,text=n_t[2],font=Nor_F)
                                            CheckVar1=tk.StringVar()
                                            ch1 = tk.Checkbutton(top12, text = "Paid",bg="gray65",fg="black",font=30, variable = CheckVar1,command=lambda:up1(),onvalue = 1,  offvalue = 0 )
                                            ch1.place(x=470,y=470)
                                            def up1():
                                                r1=''
                                                r1=ch1.cget("text")
                                                ch1.config(state="disabled")
                                                find_3=("select date('now')")
                                                c.execute(find_3)
                                                result_3=c.fetchone()
                                                can8.create_text(560,380,text="Paid date           :",font=Nor_F)
                                                can8.create_text(760,380,text=result_3[0],font=Nor_F)
                                                find_4=("select date('now','+1 year')")
                                                c.execute(find_4)
                                                result_4=c.fetchone()
                                                can8.create_text(562,430,text="Next DueDate    :",font=Nor_F)
                                                can8.create_text(760,430,text=result_4[0],font=Nor_F)
                                                w='Paid'
                                                c.execute("UPDATE fees set status=(?),due_date=(?),paid_date=(?) where s_id=?",(w,result_4[0],result_3[0],info))
                                                conn.commit()
                                                bn4=tk.Button(top12, text="Finish",font=Sm_F,bg="white",fg="black",relief="raised",width=10,command=lambda:fin())
                                                bn4.place(x=560,y=550)
                                                def fin():
                                                    top12.destroy()
                                                    lab2.destroy()
                                                    e1.destroy()
                                                    bn3.destroy()
                                                    bu2.config(state="normal")
                                               
                            else:
                                tm.showerror('Fees','Student id not found',parent=top11)


  

pp = hostelapp()   
pp.geometry("1920x1080")
pp.mainloop()






