from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

from PIL import Image, ImageTk  # pip install pillow


class courseclass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        #self.root.focus_forse()

        #title
        title=Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,height=35,width=1180)
        #variables
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()


        #widgets
        lbl_coursename=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_charges=Label(self.root,text="Charges",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
        
        #entry fields
        self.txt_coursename=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightpink").place(x=150,y=60,width=200)
        txt_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="lightpink").place(x=150,y=100,width=200)
        txt_charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15,"bold"),bg="lightpink").place(x=150,y=140,width=200)
        self.txt_description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightblue").place(x=150,y=180,width=500,height=150)

        #buttons
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_add=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2")
        self.btn_add.place(x=270,y=400,width=110,height=40)
        self.btn_add=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2")
        self.btn_add.place(x=390,y=400,width=110,height=40)
        self.btn_add=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2")
        self.btn_add.place(x=510,y=400,width=110,height=40)

        #searchpannel
        self.var_search=StringVar()
        lbl_search_coursename=Label(self.root,text="Search Course Name:",font=("goudy old style",15,"bold"),bg="white").place(x=680,y=60)
        txt_search_coursename=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightpink").place(x=870,y=60,width=200)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=1080,y=60,width=120,height=28)
        
        #content
        self.c_frme=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frme.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.c_frme,orient=VERTICAL)
        scrollx=Scrollbar(self.c_frme,orient=HORIZONTAL)
        self.coursetable=ttk.Treeview(self.c_frme,columns=("Cid","Name","Charges","Description","Duration"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.coursetable.xview)
        scrolly.config(command=self.coursetable.yview)
        
        self.coursetable.heading("Cid",text="Course ID")
        self.coursetable.heading("Name",text="Name")
        self.coursetable.heading("Charges",text="Charges")
        self.coursetable.heading("Duration",text="Duration")
        self.coursetable.heading("Description",text="Description")
        self.coursetable["show"]="headings"
        self.coursetable.column("Cid",width=100)
        self.coursetable.column("Name",width=100)
        self.coursetable.column("Charges",width=100)
        self.coursetable.column("Duration",width=100)
        self.coursetable.column("Description",width=150)

 
        self.coursetable.pack(fill=BOTH,expand=1)

    #=================================
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course Name already present",parent=self.root)
                else:
                    cur.execute("insert into course (name,duration,charges,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added SUCCessfully",parent=self.root)
       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


if  __name__=="__main__":
        root=Tk()
        obj=courseclass(root)
        root.mainloop()