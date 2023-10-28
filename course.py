from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


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
            "Mukta", 15, "bold"), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2")
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_add = Button(self.root, text="Update", font=(
            "Mukta", 15, "bold"), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2")
        self.btn_add.place(x=270, y=400, width=110, height=40)
        self.btn_add = Button(self.root, text="Delete", font=(
            "Mukta", 15, "bold"), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2")
        self.btn_add.place(x=390, y=400, width=110, height=40)
        self.btn_add = Button(self.root, text="Clear", font=(
            "Mukta", 15, "bold"), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2")
        self.btn_add.place(x=510, y=400, width=110, height=40)

        # search pannel -------
        self.var_search = StringVar()
        search_course_name = Label(self.root, text="Search By | Course Name :", font=(
            "Mukta", 15), bg="white", fg="black").place(x=720, y=70)
        self.search_course_name = Entry(self.root, textvariable=self.var_course, font=(
            "Mukta", 12),  bg="#FFFACA", fg="black").place(x=980, y=75, width=180)
        self.btn_serach = Button(self.root, text="Search", font=(
            "Mukta", 15, "bold"), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0,  cursor="hand2").place(x=1170, y=70, width=100, height=30)

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


if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
