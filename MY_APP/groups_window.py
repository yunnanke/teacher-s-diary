import customtkinter as ctk
import psycopg2
import tkinter.ttk as ttk
from tkinter import messagebox

def back():
    from main_app import menu
    groups_win.destroy()
    menu()

def groups():
    global groups_win, style, label
    groups_win = ctk.CTk()
    groups_win.geometry("1000x800+300+50")
    groups_win.title("Группы")
    groups_win.config(bg="#F2E1D0")
    groups_win.iconbitmap("icon.ico")
    groups_win.resizable(False, False)
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

    def add_student():
        global next_id, tree, roo
        roo = ctk.CTk()
        roo.iconbitmap("icon.ico")
        roo.title("Заметка")
        roo.geometry("400x360+700+250")
        roo.config(bg="#F2E1D0")

        def update_note(student_id, new_note):
            try:
                conn = connect_db()
                cur = conn.cursor()
                cur.execute("INSERT INTO schema_324.group_notes (Номер_группы, id, Студент, Заметка) VALUES (%s, %s, %s, %s);""",
                            ("", student_id,new_note, ""))
                cur.execute(
                    "INSERT INTO schema_324.attendance (Номер_группы, Предмет, Студент) VALUES (%s, %s, %s);""",
                    ("", "", new_note))
                cur.execute(
                    "INSERT INTO schema_324.marcks (Номер_группы, Предмет, Студент) VALUES (%s, %s, %s);""",
                    ("", "", new_note))
                cur.execute(
                    "INSERT INTO schema_324.marcks_stat (Номер_группы, Предмет, Студент) VALUES (%s, %s, %s);""",
                    ("", "", new_note))
                cur.execute(
                    "INSERT INTO schema_324.attendance_stat (Номер_группы, Предмет, Студент) VALUES (%s, %s, %s);""",
                    ("", "", new_note))
                conn.commit()
                cur.close()
                conn.close()

                delete()

            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось обновить заметку: {e}")

        def get_row():
            global roo
            new_stud = entry_.get()
            roo.destroy()
            new_row = ["", str(next_id + 1), f"{new_stud}", ""]
            tree.insert("", ctk.END, values=new_row)
            update_note(next_id, new_stud)
            # next_id += 1

        lable = ctk.CTkLabel(roo, width=350, height=60, corner_radius=20, bg_color="#F2E1D0",
                             fg_color="#D4C7B4", text="Введите студента:", font=("Bahnschrift Light", 20),
                             text_color="#854627")
        lable.pack(pady=10)
        entry_ = ctk.CTkEntry(roo, width=350, height=60, corner_radius=20, bg_color="#F2E1D0",
                              fg_color="#D4C7B4", placeholder_text="Студент", placeholder_text_color="#c97349",
                              font=("Bahnschrift Light", 20), text_color="#854627", border_width=0)
        entry_.pack(pady=20)
        save_butt = ctk.CTkButton(roo, text="Сохранить", corner_radius=20, bg_color="#F2E1D0",
                                  fg_color="#D4C7B4", font=("Bahnschrift Light", 20), hover_color="#B28753",
                                  text_color="#854627", command=get_row)
        save_butt.pack(pady=10)
        roo.mainloop()

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
        global tree, next_id

        def on_treeview_click(event):
            selected_item = tree.selection()

            if not selected_item:
                return

            values = tree.item(selected_item[0], 'values')

            show_details(values)

        def show_details(row_data):
            global label
            label.configure(text="")
            for i, value in enumerate(row_data):
                if i >= 2:
                    display_text = "\n".join(str(value) for i, value in enumerate(row_data) if i >= 2)
                    label.configure(text=display_text)

        conn = connect_db()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM schema_324.group_notes ORDER BY id;")
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()

            tree = ttk.Treeview(notes_frame, style="Custom.Treeview",  columns=columns, show='headings', height=27, cursor="hand2")
            tree.pack(expand=True, padx=10, pady=10)
            tree.bind("<Double-Button-1>", on_treeview_click)

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=150, anchor=ctk.CENTER)
            next_id = 0
            for row in rows:
                tree.insert('', ctk.END, values=row)
                next_id += 1

    def load_attendance():
        global tree
        tree.destroy()
        conn = connect_db()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM schema_324.attendance;")
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

    def load_marcks():
        global tree
        tree.destroy()
        conn = connect_db()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM schema_324.marcks;")
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

    def on_update():
        global tree
        root = ctk.CTk()
        root.iconbitmap("icon.ico")
        root.title("Заметка")
        root.geometry("400x360+700+250")
        root.config(bg="#F2E1D0")

        def update_note(student_id, new_note):
            try:
                conn = connect_db()
                cur = conn.cursor()
                cur.execute("UPDATE schema_324.group_notes SET Заметка = %s WHERE id = %s;", (new_note, student_id))
                conn.commit()
                cur.close()
                conn.close()

                delete()

            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось обновить заметку: {e}")

        def save_note():
            global note, st_num
            st_num = entry_st_num.get()
            note = entry_.get()
            update_note(st_num, note)
            root.destroy()



        lable = ctk.CTkLabel(root, width=350, height=60, corner_radius=20, bg_color="#F2E1D0",
                               fg_color="#D4C7B4", text="Введите заметку:", font=("Bahnschrift Light", 20),
                               text_color="#854627")
        lable.pack(pady=10)
        entry_st_num = ctk.CTkEntry(root, width=350, height=60, corner_radius=20, bg_color="#F2E1D0",
                               fg_color="#D4C7B4", placeholder_text="Номер студента", placeholder_text_color="#c97349",
                               font=("Bahnschrift Light", 20), text_color="#854627",border_width=0)
        entry_st_num.pack(pady=10)
        entry_ = ctk.CTkEntry(root, width=350, height=60, corner_radius=20, bg_color="#F2E1D0",
                               fg_color="#D4C7B4", placeholder_text="Заметка", placeholder_text_color="#c97349",
                               font=("Bahnschrift Light", 20), text_color="#854627",border_width=0)
        entry_.pack(pady=20)
        save_butt = ctk.CTkButton(root,text="Сохранить", command=save_note, corner_radius=20, bg_color="#F2E1D0",
                               fg_color="#D4C7B4", font=("Bahnschrift Light", 20), hover_color="#B28753", text_color="#854627")
        save_butt.pack(pady=10)


        root.mainloop()

    buttons_frame = ctk.CTkFrame(groups_win, width=200, height=400, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#F2E1D0")
    buttons_frame.pack(side=ctk.LEFT, padx=30, pady=50,  anchor="n")

    notes_frame = ctk.CTkFrame(groups_win, width=650, height=700, corner_radius=20, bg_color="#F2E1D0", fg_color="#7B7458")
    notes_frame.pack(side=ctk.TOP, padx=30, pady=50)
    button_info = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Группы",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=delete)
    button_info.pack(pady=10)
    button_info = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Редактировать",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=add_student)
    button_info.pack(pady=10)
    button_info = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Заметка",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=on_update)
    button_info.pack(pady=10)
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Отметки",
                                 text_color="#854627", font=("Bahnschrift Light", 20), command=load_marcks)
    button_table.pack(pady=10)
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Посещаемость",
                                 text_color="#854627", font=("Bahnschrift Light", 20), command=load_attendance)
    button_table.pack(pady=10)
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Лабораторные",
                                 text_color="#854627", font=("Bahnschrift Light", 20))
    button_table.pack(pady=10)
    button_table = ctk.CTkButton(groups_win, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Назад",
                                 text_color="#854627", font=("Bahnschrift Light", 20), command=back)
    button_table.place(x=30, y=692)
    label = ctk.CTkLabel(groups_win, text=f"", text_color="#854627", font=("Bahnschrift Light", 20),
                         bg_color="#F2E1D0",
                         fg_color="#F2E1D0"
                         )
    label.pack(pady=5)
    load_groups()

    groups_win.mainloop()


if __name__ == "__main__":
    groups()