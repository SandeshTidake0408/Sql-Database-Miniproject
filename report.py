import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class ReportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("EduTracer - Student Grade Tracer")
        self.root.geometry("1400x750+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="View Student Results", font=('Mukta', 20, 'bold'),
                      bg="#FFBE79", fg="#374151").place(x=10, y=15, width=1380, height=45)

        self.var_search = StringVar()

        lbl_search = Label(self.root, text="Search by Roll Number", font=(
            "Mukta", 17, "bold"), bg="lightyellow", fg="#374151").place(x=320, y=100)
        txt_search = Entry(self.root, textvariable=self.var_search , font=(
            "Mukta", 17), bg="lightyellow").place(x=520, y=100, width=150)
        # btn_search=Button(self.root,text="Search", font=("Mukta",15,'bold'),bg='#03a9f4',fg="white",cursor='hand2').place(x=800,y=100,width=100,height=28)
        btn_search = Button(self.root, text="Search", font=("Mukta", 15, "bold"), bg="blue", fg="black", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2").place(x=800,y=100,width=100,height=28)
        # btn_search=Button()   5:40
        # one more btn

        lbl_roll = Label(self.root, text="Roll No", font=("Mukta", 17, "bold"), bg="white",fg="#374151", bd=2, relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name = Label(self.root, text="Name", font=("Mukta", 17, "bold"), bg="white",fg="#374151", bd=2, relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_course = Label(self.root, text="Course", font=("Mukta", 17, "bold"), bg="white",fg="#374151", bd=2, relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marks = Label(self.root, text="Marks Obtained", font=("Mukta", 17, "bold"), bg="white",fg="#374151", bd=2, relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_full = Label(self.root, text="Total Marks", font=("Mukta", 17, "bold"), bg="white",fg="#374151", bd=2, relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_per = Label(self.root, text="Percentage", font=("Mukta", 17, "bold"), bg="white",fg="#374151", bd=2, relief=GROOVE).place(x=900,y=230,width=150,height=50)

        # lbl_roll = Label(self.root, text="Roll No", font=("goudy old style", 15, "bold"),bg="white", bd=2, relief=GROOVE).place(x=150,y=230,width=150,height=50)
        # lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"),bg="white", bd=2, relief=GROOVE).place(x=300,y=230,width=150,height=50)
        # lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"),bg="white", bd=2, relief=GROOVE).place(x=450,y=230,width=150,height=50)
        # lbl_marks = Label(self.root, text="Marks Obtained", font=("goudy old style", 15, "bold"),bg="white", bd=2, relief=GROOVE).place(x=600,y=230,width=150,height=50)
        # lbl_full = Label(self.root, text="Total Marks", font=("goudy old style", 15, "bold"),bg="white", bd=2, relief=GROOVE).place(x=750,y=230,width=150,height=50)
        # lbl_per = Label(self.root, text="Percentage", font=("goudy old style", 15, "bold"),bg="white", bd=2, relief=GROOVE).place(x=900,y=230,width=150,height=50)
if __name__ == "__main__":
    root = Tk()
    obj = ReportClass(root)
    root.mainloop()
