import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("EduTracer - Student Grade Tracer")
        self.root.geometry("1400x750+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="Course Details", font=('Mukta', 20, 'bold'),
                      bg="#FFBE79", fg="#374151").place(x=10, y=15, width=1380, height=45)
        # variable---------
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        # widgets-----------
        course_name = Label(self.root, text="Course Name", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=10, y=70)
        course_duration = Label(self.root, text="Duration", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=10, y=110)
        course_charges = Label(self.root, text="Charges", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=10, y=150)
        course_description = Label(self.root, text="Description", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=10, y=190)

        # entry Fields--------------------
        self.txt_course_name = Entry(self.root, textvariable=self.var_course, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black")
        self.txt_course_name.place(x=150, y=70, width=200)
        txt_course_duration = Entry(self.root, textvariable=self.var_duration, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black").place(x=150, y=110, width=200)
        txt_course_charges = Entry(self.root, textvariable=self.var_charges, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black").place(x=150, y=150, width=200)
        self.txt_course_description = Text(self.root, font=(
            "Mukta", 12), bg="#FFFACA", fg="black")
        self.txt_course_description.place(x=150, y=190, width=500, height=140)

        # button--------------------
        self.btn_add = Button(self.root, text="Save", font=(
            "Mukta", 15, "bold"), bg="lightgreen", fg="white", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_add = Button(self.root, text="Update", font=(
            "Mukta", 15, "bold"), bg="#845EC2", fg="white", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2", command=self.update)
        self.btn_add.place(x=270, y=400, width=110, height=40)
        self.btn_add = Button(self.root, text="Delete", font=(
            "Mukta", 15, "bold"), bg="#FF8066", fg="white", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2", command=self.delete)
        self.btn_add.place(x=390, y=400, width=110, height=40)
        self.btn_add = Button(self.root, text="Clear", font=(
            "Mukta", 15, "bold"), bg="#374151", fg="white", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2", command=self.clear)
        self.btn_add.place(x=510, y=400, width=110, height=40)

        # search pannel -------
        self.var_search = StringVar()
        search_course_name = Label(self.root, text="Search By | Course Name :", font=(
            "Mukta", 15), bg="white", fg="black").place(x=720, y=70)
        self.search_course_name = Entry(self.root, textvariable=self.var_course, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black").place(x=980, y=75, width=180)
        self.btn_serach = Button(self.root, text="Search", font=(
            "Mukta", 15, "bold"), bg="#374151", fg="white", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2", command=self.search).place(x=1170, y=70, width=100, height=30)

        # content ---------------in table tree
        self.c_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.c_frame.place(x=720, y=110, width=550, height=340)

        scrolly = Scrollbar(self.c_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.c_frame, orient=HORIZONTAL)

        self.course_table = ttk.Treeview(self.c_frame, columns=(
            "cid", "name", "duration", "charges", "description"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.course_table.xview)
        scrolly.config(command=self.course_table.yview)

        self.course_table.heading("cid", text="Course ID")
        self.course_table.heading("name", text="Course Name")
        self.course_table.heading("duration", text="Course Duration")
        self.course_table.heading("charges", text="Course Charges")
        self.course_table.heading("description", text="Course Description")
        self.course_table.pack(fill=BOTH, expand=1)
        self.course_table["show"] = "headings"

        self.course_table.column("cid", width=80)
        self.course_table.column("name", width=100)
        self.course_table.column("duration", width=100)
        self.course_table.column("charges", width=100)
        self.course_table.column("description", width=150)
        self.course_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()  # for display existing entries
# ==============db function==============

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cursor = con.cursor()
        try:
            cursor.execute(
                f"select *from course where name LIKE '%{self.var_course.get()}%'")
            rows = cursor.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", "Error due to {str(ex)}")

    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_course_description.delete('1.0', END)
        self.txt_course_name.config(state=NORMAL)

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cursor = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Eror", "Course Name Should be Required", parent=self.root)
            else:
                cursor.execute("select *from course where name=?",
                               (self.var_course.get(),))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Please Select Course From list", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to delete ?", parent=self.root)
                    if op == True:
                        cursor.execute(
                            "delete from course where name=?", (self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Course Deleted Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", "Error due to {str(ex)}")

    def get_data(self, ev):
        self.txt_course_name.config(state="readonly")
        r = self.course_table.focus()
        content = self.course_table.item(r)
        row = content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_course_description.delete('1.0', END)
        self.txt_course_description.insert(END, row[4])

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cursor = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Eror", "Course Name Should be Required", parent=self.root)
            else:
                cursor.execute("select *from course where name=?",
                               (self.var_course.get(),))
                row = cursor.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", f"Course Name already present", parent=self.root)
                else:
                    cursor.execute("insert into course(name, duration, charges, description) values(?,?,?,?)", (self.var_course.get(
                    ), self.var_duration.get(), self.var_charges.get(), self.txt_course_description.get("1.0", END)))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Course Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", "Error due to {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cursor = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Eror", "Course Name Should be Required", parent=self.root)
            else:
                cursor.execute("select *from course where name=?",
                               (self.var_course.get(),))

                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Select Course from List", parent=self.root)
                else:
                    cursor.execute("update course set duration=?,charges=?,description=? where name=?", (self.var_duration.get(
                    ), self.var_charges.get(), self.txt_course_description.get("1.0", END), self.var_course.get()))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Course Update Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", "Error due to {str(ex)}")

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cursor = con.cursor()
        try:
            cursor.execute("select *from course")
            rows = cursor.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", "Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
