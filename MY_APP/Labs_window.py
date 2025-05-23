import customtkinter as ctk
import psycopg2
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
from psycopg2 import Binary
import magic
import os

file_types = {
        'application/zip': '.zip',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document': '.docx',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': '.xlsx',
        'image/png': '.png',
        'image/jpeg': '.jpg'
    }

def back():
    from main_menu import menu
    lab_win.destroy()
    menu()

def labs_win():
    global lab_win
    lab_win = ctk.CTk()
    lab_win.geometry("900x700+400+90")
    lab_win.title("Группы")
    lab_win.config(bg="#F2E1D0")
    lab_win.iconbitmap("icon.ico")
    lab_win.resizable(False, False)

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


    def delete():
        global tree
        tree.destroy()
        load_labs()

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

    def on_treeview_click(event):
        selected_item = tree.selection()

        if not selected_item:
            return

        values = tree.item(selected_item[0], 'values')

        show_details(values)

    def show_details(row_data):
        global display_text
        for i, value in enumerate(row_data):
            if i == 3:
                display_text = value
                conn = connect_db()
                cursor = conn.cursor()

                cursor.execute("SELECT Файл FROM schema_table.para_plan WHERE Тема = %s", ("7",))
                result = cursor.fetchone()
                if result:
                    display_text = Binary(result)
                    check_file(display_text)
                    break
                else:
                    print("Файл не найден в базе данных")


    def check_file(binary_data):
        try:
            mime = magic.from_buffer(binary_data, mime=True)
            extension = file_types.get(mime, '.bin')

            filename = filedialog.asksaveasfilename(
                defaultextension=extension,
                filetypes=[
                    ("Document", ".docx"),
                    ("Spreadsheet", ".xlsx"),
                    ("Image", ".png .jpg"),
                ]
            )

            if not filename:
                return

            with open(filename, "wb") as f:
                f.write(binary_data)


            open_file(filename)

        except Exception as e:
            print("Ошибка при обработке файла:", e)


    def open_file(filepath):
        if os.name == 'nt':
            os.startfile(filepath)
        else:
            print("Не удалось открыть файл: неподдерживаемая ОС")


    def choose_file():
        global selected_file_path
        selected_file_path = ""

        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Image files", "*.png"),
                ("Excel files", "*.xlsx"),
                ("Word files", "*.docx")
            ])

        if file_path:
            selected_file_path = file_path

            if file_path.lower().endswith(".png"):
                try:
                    image = Image.open(file_path)
                    image.thumbnail((400, 600))
                    photo = ImageTk.PhotoImage(image)

                except Exception as e:
                    messagebox.showerror("Ошибка", f"Ошибка при открытии изображения: {e}")

    def create_file():
        choose_file()
        with open(selected_file_path, "rb") as file:
            binary_data = file.read()

        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute(
                """INSERT INTO schema_table.para_plan (Номер_группы, Предмет, Тема, Файл)
                 VALUES (%s, %s, %s,%s);""",
                ("", "", "7", Binary(binary_data),))
            conn.commit()
            cur.close()
            conn.close()
            delete()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось подключиться к БД:\n{e}")
            return None


    def load_labs():
        global tree
        conn = connect_db()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM schema_table.para_plan;")
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()

            tree = ttk.Treeview(notes_frame, columns=columns, style="Custom.Treeview", show='headings', height=20, cursor="hand2")
            tree.pack(expand=True, padx=10, pady=10)
            tree.bind("<Double-Button-1>", on_treeview_click)

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=150, anchor=ctk.CENTER)

            for row in rows:
                tree.insert('', ctk.END, values=row)

    up_buttons_frame = ctk.CTkFrame(lab_win, width=200, height=200, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#F2E1D0")
    up_buttons_frame.pack(side="top", padx=30, pady=50,  anchor="w")
    buttons_frame = ctk.CTkFrame(lab_win, width=200, height=200, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#F2E1D0")
    buttons_frame.pack(side="top", padx=30, pady=80, anchor="w")

    notes_frame = ctk.CTkFrame(lab_win, width=650, height=700, corner_radius=20, bg_color="#F2E1D0", fg_color="#7B7458")
    notes_frame.place(x=350, y=50)
    button_info = ctk.CTkButton(up_buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Предмет",
                                text_color="#854627", font=("Bahnschrift Light", 20))
    button_info.pack(pady=10)
    button_info = ctk.CTkButton(up_buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Группа",
                                text_color="#854627", font=("Bahnschrift Light", 20))
    button_info.pack(pady=10)
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Создать",
                                 text_color="#854627", font=("Bahnschrift Light", 20), command=create_file)
    button_table.pack(pady=10)
    button_table = ctk.CTkButton(lab_win, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Назад",
                                 text_color="#854627", font=("Bahnschrift Light", 20), command=back)
    button_table.place(x=30, y=592)
    load_labs()

    lab_win.mainloop()


"""if "__name__" == "__main__":
    groups()"""
labs_win()