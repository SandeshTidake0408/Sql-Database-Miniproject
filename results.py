import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("EduTracer - Student Grade Tracer")
        self.root.geometry("1300x750+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="Add Student Results", font=('Mukta', 20, 'bold'),
                      bg="#FFBE79", fg="#374151").place(x=10, y=15, width=1380, height=45)

        # label-----------------
        lbl_select = Label(self.root, text="Select Student", font=(
            "Mukta", 17), fg="#374151", bg="white").place(x=50, y=100)
        lbl_name = Label(self.root, text="Name", font=(
            "Mukta", 17), fg="#374151", bg="white").place(x=50, y=160)
        lbl_course = Label(self.root, text="Course", font=(
            "Mukta", 17), fg="#374151", bg="white").place(x=50, y=220)
        lbl_marks_ob = Label(self.root, text="Marks Obtained", font=(
            "Mukta", 17), fg="#374151", bg="white").place(x=50, y=280)
        lbl_full_marks = Label(self.root, text="Full Marks", font=(
            "Mukta", 17), fg="#374151", bg="white").place(x=50, y=340)

        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_fullmarks = StringVar()

        # Entry Field------------------------
        self.roll_list = ["Select"]
        self.fetch_roll()

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list, font=(
            "Mukta", 15), state='readonly', justify=CENTER)
        self.txt_student.place(x=270, y=105, width=140)
        self.txt_student.current(0)
        self.btn_select = Button(self.root, text="Select", font=(
            "Mukta", 15, "bold"), bg="#374151", fg="white", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2", command=self.search).place(x=420, y=105, width=100, height=30)

        txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "Mukta", 15),  bg="lightyellow", fg="black").place(x=270, y=165, width=250)

        txt_course = Entry(self.root, textvariable=self.var_course, font=(
            "Mukta", 15),  bg="lightyellow", fg="black").place(x=270, y=228, width=250)

        txt_marks = Entry(self.root, textvariable=self.var_marks, font=(
            "Mukta", 15),  bg="lightyellow", fg="black").place(x=270, y=290, width=250)
        txt_fullmarks = Entry(self.root, textvariable=self.var_fullmarks, font=(
            "Mukta", 15),  bg="lightyellow", fg="black").place(x=270, y=345, width=250)

        # button=============
        btn_add = Button(self.root, text="Submit", font=("Mukta", 15), bg="lightgreen",
                         activebackground="lightgreen", cursor="hand2", borderwidth=0, relief="flat", highlightthickness=0, command=self.add).place(x=270, y=420, width=120, height=35)
        btn_clear = Button(self.root, text="Clear", font=("Mukta", 15), bg="lightgray",
                           activebackground="lightgray", cursor="hand2", borderwidth=0, relief="flat", highlightthickness=0, command=self.clear).place(x=400, y=420, width=120, height=35)
        # image============
        self.bg_img = Image.open("images/result.jpg")
        self.bg_img = self.bg_img.resize(
            (400, 400), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.bg_label = Label(self.root, image=self.bg_img, ).place(
            x=630, y=100)

  # functions started================

    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cursor = con.cursor()
        try:
            cursor.execute("select roll from student")
            rows = cursor.fetchall()
            if (len(rows) > 0):
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", "Error due to {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cursor = con.cursor()
        try:
            cursor.execute("select name ,course from student where roll=?",
                           (self.var_roll.get(),))
            row = cursor.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror(
                    "Error", "No Record Found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", "Error due to {str(ex)}")

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cursor = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror(
                    "Eror", "Please First Select Record", parent=self.root)
            else:
                cursor.execute("select *from result where roll=? and course=?",
                               (self.var_roll.get(), self.var_course.get()))
                row = cursor.fetchone()

                if row != None:
                    messagebox.showerror(
                        "Error", "Result already present", parent=self.root)
                else:
                    marks = int(self.var_marks.get())
                    total_marks = int(self.var_fullmarks.get())
                    percentage = (marks*100)/total_marks
                    x = round(percentage, 2)

                    insert_query = "INSERT INTO result (roll, name, course, marks_ob, full_marks, per) VALUES (?, ?, ?, ?, ?, ?)"
                    data = (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_fullmarks.get(),
                        str(x))
                    print(x)
                    cursor.execute(insert_query, data)

                    con.commit()
                    messagebox.showinfo(
                        "Success", "Result Added Successfully", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_roll.set('Select')
        self.var_name.set('')
        self.var_course.set('')
        self.var_marks.set('')
        self.var_fullmarks.set('')


if __name__ == "__main__":
    root = Tk()
    obj = ResultClass(root)
    root.mainloop()
