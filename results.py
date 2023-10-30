import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("EduTracer - Student Grade Tracer")
        self.root.geometry("1400x750+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="Add Student Results", font=('Mukta', 20, 'bold'),
                      bg="#FFBE79", fg="#374151").place(x=10, y=15, width=1380, height=45)

        # label-----------------
        lbl_select = Label(self.root, text="Select Student", font=(
            "Mukta", 17, "bold"), bg="white").place(x=50, y=100)
        lbl_name = Label(self.root, text="Name", font=(
            "Mukta", 17, "bold"), bg="white").place(x=50, y=160)
        lbl_course = Label(self.root, text="Course", font=(
            "Mukta", 17, "bold"), bg="white").place(x=50, y=220)
        lbl_marks_ob = Label(self.root, text="Marks Obtained", font=(
            "Mukta", 17, "bold"), bg="white").place(x=50, y=280)
        lbl_full_marks = Label(self.root, text="Full Marks", font=(
            "Mukta", 17, "bold"), bg="white").place(x=50, y=340)

        self.var_student = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        # Entry Field------------------------
        self.txt_course_name = Entry(self.root, textvariable=self.var_student, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black")
        self.txt_course_name.place(x=250, y=165, width=200)

        txt_course_duration = Entry(self.root, textvariable=self.var_name, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black").place(x=250, y=228, width=200)

        txt_course_charges = Entry(self.root, textvariable=self.var_course, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black").place(x=250, y=290, width=200)


if __name__ == "__main__":
    root = Tk()
    obj = ResultClass(root)
    root.mainloop()
