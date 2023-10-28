from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk  # Import the ttk module for style


class RMS:
    def __init__(self, root):
        self.root = root
        root.title("EduTracer - Student Grade Tracer")
        root.geometry("1400x760+0+0")
        root.config(bg="white")

        # Create a style object for a more modern look
        self.style = ttk.Style()
        self.style.configure('TButton', padding=6, relief="flat",
                             background="#FFBE79", font=('Mukta', 15))
        self.style.map('TButton', foreground=[('active', '#374151')])

        self.logo = ImageTk.PhotoImage(file="images/logo.png")
        title = Label(root, text="EduTracer", compound="none", image=self.logo, font=(
            'Mukta', 17, 'bold'), bg="#FFBE79", fg="#374151")
        title.place(x=0, y=0, relwidth=1, height=50)

        m_frame = LabelFrame(root, text="Menu", font=(
            "Mukta", 15), bg="white", padx=5)
        m_frame.place(x=10, y=70, width=1400, relwidth=1, height=80)

        btn_course = ttk.Button(m_frame, text="Course",
                                command=self.on_course, style="TButton")
        btn_student = ttk.Button(
            m_frame, text="Student", command=self.on_student, style="TButton")
        btn_result = ttk.Button(m_frame, text="Result",
                                command=self.on_result, style="TButton")
        btn_view = ttk.Button(m_frame, text="View Results",
                              command=self.on_view_results, style="TButton")
        btn_logout = ttk.Button(m_frame, text="Logout",
                                command=self.on_logout, style="TButton")
        btn_exit = ttk.Button(m_frame, text="Exit",
                              command=root.quit, style="TButton")

        btn_course.place(x=20, y=5, width=200, height=40)
        btn_student.place(x=240, y=5, width=200, height=40)
        btn_result.place(x=460, y=5, width=200, height=40)
        btn_view.place(x=680, y=5, width=200, height=40)
        btn_logout.place(x=900, y=5, width=200, height=40)
        btn_exit.place(x=1120, y=5, width=200, height=40)

        self.bg_img = Image.open("images/bg.jpg")
        self.bg_img = self.bg_img.resize((820, 500), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.bg_label = Label(root, image=self.bg_img)
        self.bg_label.place(x=600, y=155, width=820, height=500)

        self.course_lbl = Label(
            root, text="Total Course\n[ 0 ]", font=("Mukta", 15))
        self.course_lbl.place(x=600, y=670, width=200, height=70)
        self.student_lbl = Label(
            root, text="Total Student\n[ 0 ]", font=("Mukta", 15))
        self.student_lbl.place(x=880, y=670, width=200, height=70)
        self.result_lbl = Label(
            root, text="Total Results\n[ 0 ]", font=("Mukta", 15))
        self.result_lbl.place(x=1120, y=670, width=200, height=70)

        footer = Label(root, text="EduTracer Student Grade Tracer      Contact Us: Email:sandeshtidake37@gmail.com",
                       font=('Mukta', 8), bg="#374151", fg="white")
        footer.pack(side="bottom", fill=X)

    def on_course(self):
        # Implement the action for the "Course" button
        pass

    def on_student(self):
        # Implement the action for the "Student" button
        pass

    def on_result(self):
        # Implement the action for the "Result" button
        pass

    def on_view_results(self):
        # Implement the action for the "View Results" button
        pass

    def on_logout(self):
        # Implement the action for the "Logout" button
        pass


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
