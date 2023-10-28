from tkinter import *
from PIL import Image, ImageTk


class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("EduTracer - Student Grade Tracer")
        self.root.geometry("1400x750+80+170")
        self.root.config(bg="white")
        self.root.focus_force()






if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
