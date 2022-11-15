from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from course import courseclass
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1500x790+0+0")
        self.root.config(bg="white")
        #icons
        self.logo_dash=ImageTk.PhotoImage(file="Images/srms_dash.png")


        #title
        title=Label(self.root,text="Student Result Managment System",padx=10,compound=LEFT, image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #menu
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width="1475",height=80)
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=110,y=5,width=200,height=40)
        btn_Student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=340,y=5,width=200,height=40)
        btn_Result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=560,y=5,width=200,height=40)
        btn_viewstudentsmarks=Button(M_Frame,text="View Student Marks",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=780,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1000,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1220,y=5,width=200,height=40)                        

        #content window
        self.bg_image=Image.open("images/bg.jpg")
        self.bg_image=self.bg_image.resize((920,350),Image.ANTIALIAS)
        self.bg_image=ImageTk.PhotoImage(self.bg_image)

        self.lbl_bg=Label(self.root,image=self.bg_image).place(x=400,y=180,width=920,height=350)

        #update details
        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white").place(x=400,y=530,width=250,height=100)
        self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white").place(x=740,y=530,width=250,height=100)
        self.lbl_results=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white").place(x=1070,y=530,width=250,height=100)        
        

       #footer
        footer=Label(self.root,text="SRMS-Student Result Managment System\nContact Us foe any Technical Issue: 706xxxx18 ",padx=10,font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=courseclass(self.new_win)






if  __name__=="__main__":
        root=Tk()
        obj=RMS(root)
        root.mainloop()