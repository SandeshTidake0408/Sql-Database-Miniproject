from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import mysql.connector
from tkinter import messagebox


class cust_win:
    def _init_(self, root):
        self.root = root
        self.root.title("Airport Management System")
        self.root.geometry("1295x550+230+220")

        self.var_ref = StringVar()
        X = random.randint(1000, 9999)
        self.var_ref.set(str(X))

        self.var_cust_name = StringVar()
        self.var_cust_gender = StringVar()
        self.var_cust_email = StringVar()
        self.var_cust_nationality = StringVar()

        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        img2 = Image.open(r"C:\Users\laxmi\Desktop\dbms mini\images\logo.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=100, height=40)

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer details",
                                    font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=22, font=(
            "times new roman", 13, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)

        cname = Label(labelframeleft, text="Customer Name",
                      font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtmname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name,
                             width=22, font=("times new roman", 13, "bold"))
        txtmname.grid(row=1, column=1)

        label_gender = Label(labelframeleft, text="Gender",
                             font=("arial", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=2, column=0, sticky=W)

        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_cust_gender, font=(
            "times new roman", 13, "bold"), width=22, state="readonly")
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=2, column=1)

        label_email = Label(labelframeleft, text="Email",
                            font=("arial", 12, "bold"), padx=2, pady=6)
        label_email.grid(row=3, column=0, sticky=W)

        entry_email = ttk.Entry(labelframeleft, textvariable=self.var_cust_email, width=22, font=(
            "times new roman", 13, "bold"))
        entry_email.grid(row=3, column=1)

        label_nationality = Label(labelframeleft, text="Nationality", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        label_nationality.grid(row=4, column=0, sticky=W)

        entry_nationality = ttk.Entry(
            labelframeleft, textvariable=self.var_cust_nationality, width=22, font=("times new roman", 13, "bold"))
        entry_nationality.grid(row=4, column=1)

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnADD = Button(btn_frame, text="Add", command=self.add_data, font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10, padx=1)
        btnADD.grid(row=0, column=0)

        btnUPDATE = Button(btn_frame, text="Update", command=self.update_data, font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10, padx=1)
        btnUPDATE.grid(row=0, column=1)

        btnDELETE = Button(btn_frame, text="Delete", command=self.delete_data, font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10, padx=1)
        btnDELETE.grid(row=0, column=2)

        btnRESET = Button(btn_frame, text="Reset", command=self.reset, font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10, padx=1)
        btnRESET.grid(row=0, column=3)

        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details and search System",
                                 font=("times new roman", 12, "bold"), padx=2)
        table_frame.place(x=435, y=50, width=860, height=490)

        lblSearchby = Label(table_frame, text="Search By", font=(
            "arial", 12, "bold"), bg="red", fg="white")
        lblSearchby.grid(row=0, column=0, sticky=W, padx=2)

        self.search_by = StringVar()

        combo_Search = ttk.Combobox(table_frame, textvariable=self.search_by, font=(
            "times new roman", 13, "bold"), width=24, state="readonly")
        combo_Search["values"] = ("name", "email")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()

        txtSearch = ttk.Entry(table_frame, textvariable=self.txt_search, font=(
            "arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(table_frame, text="Search", command=self.search_data, font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10, padx=1)
        btnSearch.grid(row=0, column=3)

        btnShowall = Button(table_frame, text="Show all", command=self.fetch_data, font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", width=10, padx=1)
        btnShowall.grid(row=0, column=4)

        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column=("ref", "name", "gender", "email", "nationality"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill='x')
        scroll_y.pack(side=RIGHT, fill='y')

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Refer NO")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_cust_name.get() == "" or self.var_cust_email.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="laxmi", database="management")
                my_cursor = conn.cursor()
                X = random.randint(1000, 9999)
                self.var_ref.set(str(X))
                my_cursor.execute("INSERT INTO customer VALUES (%s, %s, %s, %s, %s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_cust_gender.get(),
                    self.var_cust_email.get(),
                    self.var_cust_nationality.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Customer details added successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error: {
                                     str(e)}", parent=self.root)

    def update_data(self):
        if self.var_cust_name.get() == "" or self.var_cust_email.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="laxmi", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE customer SET name=%s, gender=%s, email=%s, nationality=%s WHERE ref=%s", (
                    self.var_cust_name.get(),
                    self.var_cust_gender.get(),
                    self.var_cust_email.get(),
                    self.var_cust_nationality.get(),
                    self.var_ref.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Customer details updated successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error: {
                                     str(e)}", parent=self.root)

    def delete_data(self):
        if self.var_ref.get() == "":
            messagebox.showerror(
                "Error", "Customer Ref is required to delete", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="laxmi", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "DELETE FROM customer WHERE ref=%s", (self.var_ref.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Customer details deleted successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error: {
                                     str(e)}", parent=self.root)

    def reset(self):
        self.var_ref.set("")  # Clear the reference number
        self.var_cust_name.set("")
        self.var_cust_gender.set("Male")
        self.var_cust_email.set("")
        self.var_cust_nationality.set("")

        # Generate a new random reference number
        X = random.randint(1000, 9999)
        self.var_ref.set(str(X))

    def search_data(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="laxmi", database="management")
        my_cursor = conn.cursor()

        my_cursor.execute(f"SELECT * FROM customer WHERE {str(
            self.search_by.get())} LIKE '%{str(self.txt_search.get())}%'")

        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="laxmi", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from customer")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.Cust_Details_Table.delete(
                    *self.Cust_Details_Table.get_children())
                for row in rows:
                    self.Cust_Details_Table.insert("", "end", values=row)
                conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_cust_gender.set(row[2])
        self.var_cust_email.set(row[3])
        self.var_cust_nationality.set(row[4])


if _name_ == "_main_":
    root = Tk()
    obj = cust_win(root)
    root.mainloop()
