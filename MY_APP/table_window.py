import customtkinter as ctk
import tkinter.ttk as ttk
import psycopg2
from tkinter import messagebox


def back():
    from main_menu import menu
    table_win.destroy()
    menu()

def table_wind():
    global table_win
    table_win = ctk.CTk()
    table_win.geometry("1000x800+300+50")
    table_win.title("Расписание")
    table_win.config(bg="#F2E1D0")
    table_win.iconbitmap("icon.ico")
    table_win.resizable(False, False)

    def connect_db():
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="postgres",
                user="postgres",
                password="1234",
                port="5432"
            )
            return conn
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось подключиться к БД:\n{e}")
            return None

    def delete():
        global tree
        tree.destroy()
        load_data()

    def load_data():
        global tree
        conn = connect_db()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM schema_324.week_table;")
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()

            tree = ttk.Treeview(notes_frame,  columns=columns, show='headings', height=10)
            tree.pack(expand=True, padx=10, pady=10)

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=80, anchor=ctk.CENTER)

            for row in rows:
                tree.insert('', ctk.END, values=row)

    def data_labs():
        global tree
        tree.destroy()
        conn = connect_db()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM schema_324.week_labs;")
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()
            tree = ttk.Treeview(notes_frame, columns=columns, show='headings', height=10)
            tree.pack(expand=True, padx=10, pady=10)

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=80, anchor=ctk.CENTER)

            for row in rows:
                tree.insert('', ctk.END, values=row)

    def load_para():
        global tree
        tree.destroy()
        conn = connect_db()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM schema_324.week_para;")
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()
            tree = ttk.Treeview(notes_frame, columns=columns, show='headings', height=10)
            tree.pack(expand=True, padx=10, pady=10)

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=80, anchor=ctk.CENTER)

            for row in rows:
                tree.insert('', ctk.END, values=row)



    buttons_frame = ctk.CTkFrame(table_win, width=200, height=400, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#F2E1D0")
    buttons_frame.pack(side=ctk.LEFT, padx=30, pady=50,  anchor="n")

    notes_frame = ctk.CTkFrame(table_win, width=650, height=700, corner_radius=20, bg_color="#F2E1D0", fg_color="#D4C7B4")
    notes_frame.pack(side=ctk.RIGHT, padx=30)

    button_info = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="На неделю",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=delete)
    button_info.pack(pady=10)
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Замены",
                                 text_color="#854627", font=("Bahnschrift Light", 20))
    button_table.pack(pady=10)
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Пары",
                                 text_color="#854627", font=("Bahnschrift Light", 20), command=load_para)
    button_table.pack(pady=10)
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Лабораторные",
                                 text_color="#854627", font=("Bahnschrift Light", 20), command=data_labs)
    button_table.pack(pady=10)
    button_table = ctk.CTkButton(table_win, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Назад",
                                 text_color="#854627", font=("Bahnschrift Light", 20), command=back)
    button_table.place(x=30, y=692)
    load_data()

    table_win.mainloop()


"""if "__name__" == "__main__":
    table_wind()"""
table_wind()

