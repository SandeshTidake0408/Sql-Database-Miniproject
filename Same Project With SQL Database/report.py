import mysql.connector as c
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
        self.var_id = ""
        lbl_search = Label(self.root, text="Search by | Roll Number", font=(
            "Mukta", 15, ), bg="white", fg="#374151").place(x=150, y=95)
        txt_search = Entry(self.root, textvariable=self.var_search, font=(
            "Mukta", 15), fg="black", bg="white").place(x=380, y=100, width=150)

        btn_search = Button(self.root, text="Search", font=("Mukta", 15), bg="lightgreen", fg="white", borderwidth=0,
                            relief="flat", highlightthickness=0,  cursor="hand2", command=self.search).place(x=550, y=95, width=120, height=32)

        btn_clear = Button(self.root, text="Clear", font=("Mukta", 15), bg="#374151", fg="white", borderwidth=0,
                           relief="flat", highlightthickness=0,  cursor="hand2", command=self.clear).place(x=700, y=95, width=120, height=32)

        lbl_roll = Label(self.root, text="Roll No", font=("Mukta", 17, "bold"), bg="white",
                         fg="#374151", bd=2, relief=GROOVE).place(x=150, y=230, width=150, height=50)
        lbl_name = Label(self.root, text="Name", font=("Mukta", 17, "bold"), bg="white",
                         fg="#374151", bd=2, relief=GROOVE).place(x=300, y=230, width=150, height=50)
        lbl_course = Label(self.root, text="Course", font=("Mukta", 17, "bold"), bg="white",
                           fg="#374151", bd=2, relief=GROOVE).place(x=450, y=230, width=150, height=50)
        lbl_marks = Label(self.root, text="Marks Obtained", font=("Mukta", 17, "bold"), bg="white",
                          fg="#374151", bd=2, relief=GROOVE).place(x=600, y=230, width=200, height=50)
        lbl_full = Label(self.root, text="Total Marks", font=("Mukta", 17, "bold"), bg="white",
                         fg="#374151", bd=2, relief=GROOVE).place(x=800, y=230, width=150, height=50)
        lbl_per = Label(self.root, text="Percentage", font=("Mukta", 17, "bold"), bg="white",
                        fg="#374151", bd=2, relief=GROOVE).place(x=950, y=230, width=150, height=50)

        self.roll = Label(self.root, font=("Mukta", 17, "bold"),
                          bg="white", fg="black", bd=2, relief=GROOVE)
        self.roll.place(x=150, y=280, width=150, height=50)
        self.name = Label(self.root, font=("Mukta", 17, "bold"),
                          bg="white", fg="#374151", bd=2, relief=GROOVE)
        self.name.place(x=300, y=280, width=150, height=50)
        self.course = Label(self.root, font=(
            "Mukta", 17, "bold"), bg="white", fg="#374151", bd=2, relief=GROOVE)
        self.course.place(x=450, y=280, width=150, height=50)
        self.marks = Label(self.root, font=("Mukta", 17, "bold"),
                           bg="white", fg="#374151", bd=2, relief=GROOVE)
        self.marks.place(x=600, y=280, width=200, height=50)
        self.full = Label(self.root, font=("Mukta", 17, "bold"),
                          bg="white", fg="#374151", bd=2, relief=GROOVE)
        self.full.place(x=800, y=280, width=150, height=50)
        self.per = Label(self.root, font=("Mukta", 17, "bold"),
                         bg="white", fg="#374151", bd=2, relief=GROOVE)
        self.per.place(x=950, y=280, width=150, height=50)

        btn_delete = Button(self.root, text="Delete", font=("Mukta", 15, "bold"), bg="#FF8066", fg="white", borderwidth=0,
                            relief="flat", highlightthickness=0,  cursor="hand2", command=self.delete).place(x=150, y=350, width=150, height=35)

    # function-=================

    def search(self):
        con = c.connect(host="localhost", user="root",
                        passwd="SDT123@#", database="edutracer")
        cursor = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror(
                    "Error", "Roll No. should be required", parent=self.root)
            else:
                cursor.execute(
                    "SELECT * FROM result WHERE roll = %s", (self.var_search.get(),))

                row = cursor.fetchone()
                if row != None:
                    self.var_id = row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror(
                        "Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_id = ""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    def delete(self):
        con = c.connect(host="localhost", user="root",
                        passwd="SDT123@#", database="edutracer")
        cursor = con.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror(
                    "Eror", "Search Student result first", parent=self.root)
            else:
                cursor.execute(
                    "SELECT * FROM result WHERE rid = %s", (self.var_id,))

                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Student Result", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to delete ?", parent=self.root)
                    if op == True:
                        cursor.execute(
                            "DELETE FROM result WHERE rid = %s", (self.var_id,))

                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Result Deleted Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", "Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = ReportClass(root)
    root.mainloop()
