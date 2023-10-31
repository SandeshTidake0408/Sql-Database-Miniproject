from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from student import StudentClass
from results import ResultClass


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("EduTracer - Student Grade Tracer")
        self.root.geometry("1400x750+0+0")
        self.root.config(bg="white")
        self.logo = ImageTk.PhotoImage(file="images/logo.png")
        title = Label(self.root, text="EduTracer", compound="none", image=self.logo, font=('Mukta', 17,
                      'bold'), bg="#FFBE79", fg="#374151").place(x=0, y=0, relwidth=1, height=50)
        # menu
        m_frame = LabelFrame(self.root, text="Menu", font=(
            "Mukta", 15),fg='black' ,bg="white", padx=5)
        m_frame.place(x=10, y=70, width=1400, relwidth=1, height=80)

        btn_course = Button(m_frame, text="Course", font=(
            "Mukta", 15), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0, cursor="hand2", command=self.add_course).place(x=20, y=5, width=200, height=40)
        btn_student = Button(m_frame, text="Student", font=(
            "Mukta", 15), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0, cursor="hand2", command=self.add_student).place(x=240, y=5, width=200, height=40)
        btn_result = Button(m_frame, text="Result", font=(
            "Mukta", 15), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0, cursor="hand2", command=self.add_result).place(x=460, y=5, width=200, height=40)
        btn_view = Button(m_frame, text="View Results", font=(
            "Mukta", 15), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0, cursor="hand2").place(x=680, y=5, width=200, height=40)
        btn_logout = Button(m_frame, text="Logout", font=(
            "Mukta", 15), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0, cursor="hand2").place(x=900, y=5, width=200, height=40)
        btn_exit = Button(m_frame, text="Exit", font=(
            "Mukta", 15), bg="#FFBE79", fg="#374151", borderwidth=0, relief="flat", highlightthickness=0, cursor="hand2").place(x=1120, y=5, width=200, height=40)

        # main screen BG
        self.bg_img = Image.open("images/bg.jpg")
        self.bg_img = self.bg_img.resize(
            (820, 500), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.bg_label = Label(self.root, image=self.bg_img, ).place(
            x=600, y=155, width=820, height=500)

        # details
        self.course_lbl = Label(self.root, text="Total Course\n[ 0 ]", font=(
            "Mukta", 15)).place(x=600, y=670, width=200, height=70)
        self.student_lbl = Label(self.root, text="Total Student\n[ 0 ]", font=(
            "Mukta", 15),).place(x=880, y=670, width=200, height=70)
        self.result_lbl = Label(self.root, text="Total Results\n[ 0 ]", font=(
            "Mukta", 15)).place(x=1120, y=670, width=200, height=70)

        # footer
        footer = Label(self.root, text="EduTracer Stuent Grade Tracer      Contact Us: Email:sandeshtidake37@gmail.com",
                       font=('Mukta', 8), bg="#374151", fg="white").pack(side="bottom", fill=X)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
