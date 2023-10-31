import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class StudentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("EduTracer - Student Grade Tracer")
        self.root.geometry("1400x750+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="Student Details", font=('Mukta', 20, 'bold'),
                      bg="#FFBE79", fg="#374151").place(x=10, y=15, width=1380, height=45)
        # variable---------
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # widgets-----------
        # ====column1
        lbl_roll = Label(self.root, text="Roll No", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=10, y=70)
        lbl_name = Label(self.root, text="Name", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=10, y=110)
        lbl_email = Label(self.root, text="Email", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=10, y=150)
        lbl_gender = Label(self.root, text="Gender", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=10, y=190)
        lbl_state = Label(self.root, text="State", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=10, y=230)
        lbl_city = Label(self.root, text="City", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=250, y=230)

        lbl_address = Label(self.root, text="Address", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=10, y=270)

        # entry Fields--------------------
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black")
        self.txt_roll.place(x=110, y=70, width=200)
        txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black").place(x=110, y=110, width=200)
        txt_eamil = Entry(self.root, textvariable=self.var_email, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black").place(x=110, y=150, width=200)

        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=(
            "Select", "Male", "Female", "Other"), font=("Mukta", 12), state='readonly', justify=CENTER)
        self.txt_gender.place(x=110, y=195, width=200)
        self.txt_gender.current(0)

        self.txt_state = Entry(self.root, textvariable=self.var_state, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black").place(x=110, y=235, width=120)
        self.city = Entry(self.root, textvariable=self.var_city, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black").place(x=300, y=235, width=120)

        # ====column2
        lbl_dob = Label(self.root, text="DOB", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=340, y=70)
        lbl_contact = Label(self.root, text="Contact", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=340, y=110)
        lbl_admission = Label(self.root, text="Admission", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=340, y=150)
        lbl_course = Label(self.root, text="Course", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=340, y=190)
        lbl_pin = Label(self.root, text="Pin Code", font=(
            "Mukta", 15, "bold"), bg="white", fg="#374151").place(x=440, y=230)

        # entry field------------------
        self.course_list = ["Select"]
        self.fetch_course()

        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black")
        self.txt_dob.place(x=460, y=70, width=200)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black").place(x=460, y=110, width=200)
        txt_admission = Entry(self.root, textvariable=self.var_a_date, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black").place(x=460, y=150, width=200)

        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list, font=(
            "Mukta", 12), state='readonly', justify=CENTER)
        self.txt_course.place(x=460, y=195, width=200)
        self.txt_course.current(0)
        self.txt_pin = Entry(self.root, textvariable=self.var_pin, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black").place(x=540, y=235, width=120)

        # ---------address fields========
        self.txt_address = Text(self.root, font=(
            "Mukta", 12), bg="#FFFACA", fg="black")
        self.txt_address.place(x=110, y=280, width=540, height=120)

        # button--------------------

        self.btn_add = Button(self.root, text="Save", font=(
            "Mukta", 15, "bold"), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2", command=self.add)
        self.btn_add.place(x=120, y=420, width=110, height=40)
        self.btn_add = Button(self.root, text="Update", font=(
            "Mukta", 15, "bold"), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2", command=self.update)
        self.btn_add.place(x=270, y=420, width=110, height=40)
        self.btn_add = Button(self.root, text="Delete", font=(
            "Mukta", 15, "bold"), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2", command=self.delete)
        self.btn_add.place(x=410, y=420, width=110, height=40)
        self.btn_add = Button(self.root, text="Clear", font=(
            "Mukta", 15, "bold"), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2", command=self.clear)
        self.btn_add.place(x=550, y=420, width=110, height=40)

        # search pannel -------
        self.var_search = StringVar()
        search_course_roll = Label(self.root, text="Search By | Roll No :", font=(
            "Mukta", 15), bg="white", fg="black").place(x=720, y=70)
        self.search_roll = Entry(self.root, textvariable=self.var_search, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black").place(x=980, y=75, width=180)
        self.btn_serach = Button(self.root, text="Search", font=(
            "Mukta", 15, "bold"), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2", command=self.search).place(x=1170, y=70, width=100, height=30)

        # content ---------------in table tree
        self.c_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.c_frame.place(x=720, y=110, width=550, height=340)

        scrolly = Scrollbar(self.c_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.c_frame, orient=HORIZONTAL)

        self.course_table = ttk.Treeview(self.c_frame, columns=(
            "roll", "name", "email", "gender", "dob", "contact", "admission", "course", "state", "city", "pincode", "address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.course_table.xview)
        scrolly.config(command=self.course_table.yview)

        self.course_table.heading("roll", text="Roll No")
        self.course_table.heading("name", text="Name")
        self.course_table.heading("email", text="Email")
        self.course_table.heading("gender", text="Gender")
        self.course_table.heading("dob", text="DOB")
        self.course_table.heading("contact", text="Contact")
        self.course_table.heading("admission", text="Admissiom")
        self.course_table.heading("course", text="Course")
        self.course_table.heading("state", text="State")
        self.course_table.heading("city", text="City")
        self.course_table.heading("pincode", text="Pincode")
        self.course_table.heading("address", text="Address")

        self.course_table.pack(fill=BOTH, expand=1)
        self.course_table["show"] = "headings"

        self.course_table.column("roll", width=70)
        self.course_table.column("name", width=100)
        self.course_table.column("email", width=100)
        self.course_table.column("gender", width=100)
        self.course_table.column("dob", width=100)
        self.course_table.column("contact", width=100)
        self.course_table.column("admission", width=100)
        self.course_table.column("course", width=100)
        self.course_table.column("state", width=100)
        self.course_table.column("city", width=100)
        self.course_table.column("pincode", width=100)
        self.course_table.column("address", width=200)
        self.course_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()  # for display existing entries

# ==============db function==============

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cursor = con.cursor()
        try:
            cursor.execute("select *from student where roll=?",
                           (self.var_search.get(),))
            row = cursor.fetchone()
            if row != None:
                self.course_table.delete(*self.course_table.get_children())
                self.course_table.insert('', END, values=row)
            else:
                messagebox.showerror(
                    "Error", "No Record Found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", "Error due to {str(ex)}")

    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set(""),
        self.var_pin.set("")
        self.txt_address.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cursor = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Eror", "Roll No Should be Required", parent=self.root)
            else:
                cursor.execute("select *from student where roll=?",
                               (self.var_roll.get(),))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Please Select Student From list", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to delete ?", parent=self.root)
                    if op == True:
                        cursor.execute(
                            "delete from student where roll=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Student Deleted Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", "Error due to {str(ex)}")

    def get_data(self, ev):
        self.txt_roll.config(state="readonly")
        r = self.course_table.focus()
        content = self.course_table.item(r)
        row = content["values"]
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9]),
        self.var_pin.set(row[10])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[11])

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cursor = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Eror", "Roll No Should be Required", parent=self.root)
            else:
                cursor.execute("select *from student where roll=?",
                               (self.var_roll.get(),))
                row = cursor.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", f"Roll No already present", parent=self.root)
                else:
                    cursor.execute("insert into student(roll, name, email, gender, dob, contact, admission, course, state, city, pincode, address) values(?,?,?,?,?,?,?,?,?,?,?,?)", (self.var_roll.get(),
                                                                                                                                                                                      self.var_name.get(),
                                                                                                                                                                                      self.var_email.get(),
                                                                                                                                                                                      self.var_gender.get(),
                                                                                                                                                                                      self.var_dob.get(),
                                                                                                                                                                                      self.var_contact.get(),
                                                                                                                                                                                      self.var_a_date.get(),
                                                                                                                                                                                      self.var_course.get(),
                                                                                                                                                                                      self.var_state.get(),
                                                                                                                                                                                      self.var_city.get(),
                                                                                                                                                                                      self.var_pin.get(),
                                                                                                                                                                                      self.txt_address.get("1.0", END)))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Student Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", "Error due to {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cursor = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Eror", "Roll No Should be Required", parent=self.root)
            else:
                cursor.execute("select *from student where roll=?",
                               (self.var_roll.get(),))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Select Student from List", parent=self.root)
                else:
                    cursor.execute("update student set name=?, email=?, gender=?, dob=?, contact=?, admission=?, course=?, state=?, city=?, pincode=?, address=? where roll=?", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", END),
                        self.var_roll.get(),))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Student Details Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", "Error due to {str(ex)}")

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cursor = con.cursor()
        try:
            cursor.execute("select *from student")
            rows = cursor.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", "Error due to {str(ex)}")

    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        cursor = con.cursor()
        try:
            cursor.execute("select name from course")
            rows = cursor.fetchall()
            if (len(rows) > 0):
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", "Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()
