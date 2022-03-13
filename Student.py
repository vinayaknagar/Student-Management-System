from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student management System")
        self.root.geometry("1350x800+0+0")
        
        title=Label(self.root,text="Student Management System",font=("times new roman",40,"bold"),bg="Yellow",fg="red",bd=7,relief=GROOVE)
        title.pack(side=TOP,fill=X)
        
        #...................Variables...................................
        self.roll=StringVar()
        self.name=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()
        
        self.search_by=StringVar()
        self.search_txt=StringVar()


        #...........................Manage Frame........................
        
        m_f=Frame(self.root,bd=4,relief=RIDGE,bg="yellow")
        m_f.place(x=20,y=100,width=450,height=610)
        
        m_t=Label(m_f,text="Manage Student",font=("times new roman",30,"bold"),bg="yellow",fg="red")
        m_t.grid(row=0,columnspan=2,pady=20)
        
        s_roll=Label(m_f,text="Roll No : ",font=("times new roman",20,"bold"),bg="yellow",fg="red")
        s_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        
        txt_roll=Entry(m_f,textvariable=self.roll,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,fg="darkred")
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        s_name=Label(m_f,text="Name : ",font=("times new roman",20,"bold"),bg="yellow",fg="red")
        s_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        
        txt_name=Entry(m_f,textvariable=self.name,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,fg="darkred")
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        s_gender=Label(m_f,text="Gender : ",font=("times new roman",20,"bold"),bg="yellow",fg="red")
        s_gender.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        
        c_g=ttk.Combobox(m_f,textvariable=self.gender,font=("times new roman",13,"bold"),state='readonly')
        c_g['values']=("male","female","other")
        c_g.grid(row=3,column=1,padx=20,pady=10)
        
        
        s_email=Label(m_f,text="Email : ",font=("times new roman",20,"bold"),bg="yellow",fg="red")
        s_email.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        
        txt_email=Entry(m_f,textvariable=self.email,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,fg="darkred")
        txt_email.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        
        s_con=Label(m_f,text="Contact : ",font=("times new roman",20,"bold"),bg="yellow",fg="red")
        s_con.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        
        txt_con=Entry(m_f,textvariable=self.contact,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,fg="darkred")
        txt_con.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        
        s_dob=Label(m_f,text="D.O.B : ",font=("times new roman",20,"bold"),bg="yellow",fg="red")
        s_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        
        txt_dob=Entry(m_f,textvariable=self.dob,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,fg="darkred")
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        s_adress=Label(m_f,text="Address : ",font=("times new roman",20,"bold"),bg="yellow",fg="red")
        s_adress.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        
        self.txt_address=Text(m_f,width=15,height=3,font=("",20))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        
        
        #....................Button.....................................
        b_f=Frame(self.root,bd=4,relief=RIDGE,bg="yellow")
        b_f.place(x=23,y=655,width=447)
        
        add=Button(b_f,text="Add",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        update=Button(b_f,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delete=Button(b_f,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clear=Button(b_f,text="Clear",width=10,command=self.clear_data).grid(row=0,column=3,padx=10,pady=10)
       
        
        #...........................Detail Frame........................
        
        d_f=Frame(self.root,bd=4,relief=RIDGE,bg="yellow")
        d_f.place(x=500,y=100,width=800,height=610)
        
        search=Label(d_f,text="Search : ",font=("times new roman",20,"bold"),bg="yellow",fg="red")
        search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
        c_search=ttk.Combobox(d_f,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
        c_search['values']=("Roll_no","Name","contact")
        c_search.grid(row=0,column=1,padx=20,pady=10)
        
        txt_search=Entry(d_f,width=15,textvariable=self.search_txt,font=("times new roman",11,"bold"),bd=5,relief=GROOVE,fg="darkred")
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        searchbtn=Button(d_f,text="Search",command=self.search_data,width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(d_f,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)
        exit_btn=Button(d_f,text="Exit",width=10,pady=5,command=self.exit_app).grid(row=0,column=5,padx=10,pady=10)
        
        
        #.....................Table Frame......................
        t_f=Frame(d_f,bd=4,relief=RIDGE,bg="yellow")
        t_f.place(x=10,y=70,width=750,height=500)
        
        scroll_x=Scrollbar(t_f,orient=HORIZONTAL)
        scroll_y=Scrollbar(t_f,orient=VERTICAL)
        self.s_ta=ttk.Treeview(t_f,column=("Roll","Name","Gender","Email","Contact","D.O.B.","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.s_ta.xview)
        scroll_y.config(command=self.s_ta.yview)
        self.s_ta.heading("Roll", text="Roll No")
        self.s_ta.heading("Name", text="Name")
        self.s_ta.heading("Gender", text="Gender")
        self.s_ta.heading("Email", text="Email")
        self.s_ta.heading("Contact", text="Contact")
        self.s_ta.heading("D.O.B.", text="D.O.B")
        self.s_ta.heading("Address", text="Address")
        self.s_ta['show']='headings'
        self.s_ta.column("Roll",width=50)
        self.s_ta.column("Name",width=100)
        self.s_ta.column("Gender",width=100)
        self.s_ta.column("Email",width=150)
        self.s_ta.column("Contact",width=100)
        self.s_ta.column("D.O.B.",width=100)
        self.s_ta.column("Address",width=150)
        self.s_ta.bind("<ButtonRelease-1>",self.cursor)
        
        self.s_ta.pack(fill=BOTH,expand=1 )
        self.fetch_data()
    
    def add_student(self):
        
        if self.roll.get()=="" or self.name.get()=="" or self.gender.get()=="" or self.email.get()=="" or self.contact.get()=="" or self.dob.get()=="" or self.txt_address.get("1.0",END)=="":
            messagebox.showerror("Error","All Fields Are Required.")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into Student values(%s,%s,%s,%s,%s,%s,%s)",(
                self.roll.get(),
                self.name.get(),
                self.gender.get(),
                self.email.get(),
                self.contact.get(),
                self.dob.get(),
                self.txt_address.get('1.0',END)
                ))
            con.commit()
            self.fetch_data()
            self.clear_data()
            con.close()
            
            messagebox.showinfo("Success","Record Has Been Inserted")
    
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from Student")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.s_ta.delete(*self.s_ta.get_children())
            for row in rows:
                self.s_ta.insert('',END,values=row)
            con.commit()
        con.close()
    
    def clear_data(self):
        self.roll.set("")
        self.name.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.dob.set("")
        self.txt_address.delete("1.0",END)
        
    def cursor(self,ev):
        cursor_row=self.s_ta.focus()
        contant=self.s_ta.item(cursor_row)
        row=contant['values']
        self.roll.set(row[0])
        self.name.set(row[1])
        self.gender.set(row[2])
        self.email.set(row[3])
        self.contact.set(row[4])
        self.dob.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])
        
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update Student set Name=%s,Gender=%s,Email=%s,contact=%s,DOB=%s,Address=%s where Roll_no=%s",(
            self.name.get(),
            self.gender.get(),
            self.email.get(),
            self.contact.get(),
            self.dob.get(),
            self.txt_address.get('1.0',END),
            self.roll.get()
            ))
        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()
    
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from Student where Roll_no=%s",self.roll.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear_data()
    
    def search_data(self):
        
        if self.search_by.get()=="" or self.search_txt.get()=="":
            messagebox.showerror("Error","Please Select Search Details.")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("select * from Student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.s_ta.delete(*self.s_ta.get_children())
                for row in rows:
                    self.s_ta.insert('',END,values=row)
                con.commit()
                con.close()
            else:
                messagebox.showerror("Not Found","Searching Data is not Found.")
        
    
    def exit_app(self):
          op=messagebox.askyesno("Exit","Do You Want To Exit?")
          if op>0:
              self.root.destroy()
             
root=Tk()
obj=Student(root)
root.mainloop()