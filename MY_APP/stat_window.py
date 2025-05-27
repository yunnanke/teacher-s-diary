import customtkinter as ctk
import psycopg2
import tkinter.ttk as ttk

def back(log):
    from main_app import menu
    stat_win.destroy()
    menu(log)

def statistics_win(login):
    global stat_win
    stat_win = ctk.CTk()
    stat_win.geometry("900x580+300+50")
    stat_win.title("Группы")
    stat_win.config(bg="#F2E1D0")
    stat_win.iconbitmap("icon.ico")
    stat_win.resizable(False, False)

    style = ttk.Style()
    style.configure("Custom.Treeview",
                    background="#D4C7B4",
                    foreground="#854627",
                    font=("Bahnschrift Light", 12))
    style.map("Custom.Treeview",
              background=[('selected', '#D3D3D3')],
              foreground=[('selected', '#B28753')])
    style.configure("Custom.Treeview.Heading",
                    background="#7B7458",
                    foreground="#854627",
                    font=("Bahnschrift Light", 12))

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
        except ValueError:
            return None

    def delete():
        global tree
        tree.destroy()
        load_groups()

    def load_groups():
        global tree
        conn = connect_db()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM schema_324.group_notes ORDER BY id;")
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()

            tree = ttk.Treeview(notes_frame, columns=columns, show='headings', style="Custom.Treeview", height=27, cursor="hand2")
            tree.pack(expand=True, padx=10, pady=10)

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=150, anchor=ctk.CENTER)

            for row in rows:
                tree.insert('', ctk.END, values=row)

    def load_attendance_stat():
        global tree
        tree.destroy()
        conn = connect_db()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM schema_324.attendance_stat;")
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()

            tree = ttk.Treeview(notes_frame, columns=columns, style="Custom.Treeview", show='headings', height=28, cursor="hand2")
            tree.pack(expand=True, padx=10, pady=10)

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=150, anchor=ctk.CENTER)

            for row in rows:
                tree.insert('', ctk.END, values=row)

    def load_marcks_stat():
        global tree
        tree.destroy()
        conn = connect_db()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM schema_324.marcks_stat;")
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()

            tree = ttk.Treeview(notes_frame, columns=columns, style="Custom.Treeview", show='headings', height=27, cursor="hand2")
            tree.pack(expand=True, padx=10, pady=10)

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=150, anchor=ctk.CENTER)

            for row in rows:
                tree.insert('', ctk.END, values=row)

    up_buttons_frame = ctk.CTkFrame(stat_win, width=200, height=200, corner_radius=20, bg_color="#F2E1D0",
                                    fg_color="#F2E1D0")
    up_buttons_frame.pack(side="top", padx=30, pady=50, anchor="w")
    buttons_frame = ctk.CTkFrame(stat_win, width=200, height=200, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#F2E1D0")
    buttons_frame.pack(side="top", padx=30, pady=80, anchor="w")

    notes_frame = ctk.CTkFrame(stat_win, width=650, height=700, corner_radius=20, bg_color="#F2E1D0",
                               fg_color="#7B7458")
    notes_frame.place(x=350, y=50)
    button_info = ctk.CTkButton(up_buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Группы",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=delete)
    button_info.pack(pady=10)
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Успеваемость",
                                 text_color="#854627", font=("Bahnschrift Light", 20), command=load_marcks_stat)
    button_table.pack(pady=10)
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Посещаемость",
                                 text_color="#854627", font=("Bahnschrift Light", 20), command=load_attendance_stat)
    button_table.pack(pady=10)
    button_table = ctk.CTkButton(stat_win, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Назад",
                                 text_color="#854627", font=("Bahnschrift Light", 20), command=lambda:back(login))
    button_table.place(x=30, y=492)
    load_groups()

    stat_win.mainloop()


"""if __name__ == "__main__":
    statistics_win()"""