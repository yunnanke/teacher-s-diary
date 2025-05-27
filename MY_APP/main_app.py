import customtkinter as ctk
from customtkinter import CTkImage
from tkinter import messagebox
import re
import json
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import psycopg2
from psycopg2 import Binary

def ex():
    global win
    win.destroy()

def exit():
    global menu_win
    menu_win.destroy()

def back():
    global win, root
    root.destroy()
    win.deiconify()


def registry():
    global win, root
    win.withdraw()
    root = ctk.CTk()
    root.iconbitmap("icon.ico")
    root.title("Регистрация")
    root.geometry("400x600+700+250")
    root.config(bg="#F2E1D0")


    def save_credentials():
        global mail, password, login
        login = entry_login.get()
        mail = entry_mail.get()
        password = entry_pass.get()

        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        allowed_domains = ['mail.ru', 'gmail.com', 'outlook.com', 'rambler.ru', 'yandex.ru']
        match = re.match(pattern, mail)

        if not match:
            messagebox.showerror("Error", "Incorrect email.")
            return False
        try:
            _, domain = mail.split('@')
        except ValueError:
            messagebox.showerror("Error", "Invalid email format.")
            return False
        if domain not in allowed_domains:
            messagebox.showerror("Error", "Email domain is not allowed.")
            return False

        try:
            with open("users.json", "r") as f:
                data = json.load(f)
            for user in data:
                if user["mail"] == mail:
                    messagebox.showerror("Error", "This mail is already in use!")
                    return False

            new_user = {"mail": mail, "password": password, "username": login, "name":""}
            data.append(new_user)
            with open("users.json", "w") as f:
                json.dump(data, f, indent=3, ensure_ascii=False)
                win.destroy()
                root.destroy()
                info_window(login)
            return True
        except ValueError:
            messagebox.showerror("Error", "User database not found.")
            return False

    def toggle_password():
        if entry_pass.cget("show") == "*":
            entry_pass.configure(show="")
            eye_button.configure(text="👁️")
        else:
            entry_pass.configure(show="*")
            eye_button.configure(text="🙈")


    titleReg = ctk.CTkLabel(master=root, width=80, height=80, corner_radius=20, fg_color="#D4C7B4", bg_color="#F2E1D0",
                         text="Регистрация",
                         text_color="#854627", font=("Bahnschrift Light", 50))
    titleReg.pack(padx=10, pady=45)

    entry_login = ctk.CTkEntry(master=root, width=350, height=60, corner_radius=20, bg_color="#F2E1D0",
                               fg_color="#D4C7B4", placeholder_text="Логин", placeholder_text_color="#c97349",
                               font=("Bahnschrift Light", 20), text_color="#854627",border_width=0)
    entry_login.pack(pady=10)
    entry_mail = ctk.CTkEntry(master=root, width=350, height=60, corner_radius=20, bg_color="#F2E1D0",
                               fg_color="#D4C7B4", placeholder_text="Почта", placeholder_text_color="#c97349",
                               font=("Bahnschrift Light", 20), text_color="#854627",border_width=0)
    entry_mail.pack(pady=10)
    entry_pass = ctk.CTkEntry(master=root, width=350, height=60, corner_radius=20, bg_color="#F2E1D0",
                              fg_color="#D4C7B4", placeholder_text="Пароль", placeholder_text_color="#c97349",
                              font=("Bahnschrift Light", 20), text_color="#854627",border_width=0)
    entry_pass.pack(pady=10)
    eye_button = ctk.CTkButton(master=root, text="👁️", width=0, height=0, corner_radius=20,
                               command=toggle_password, fg_color="#D4C7B4", bg_color="#D4C7B4",
                               hover_color="#D4C7B4", text_color="#c97349",
                               font=("Arial", 20))
    eye_button.place(in_=entry_pass, relx=1, x=-60, y=15)
    registration = ctk.CTkButton(root, width=150, height=40, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Зарегистрироваться",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=save_credentials)
    registration.pack(pady=30)
    back_button = ctk.CTkButton(root, width=130, height=40, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Назад",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=back)
    back_button.pack(pady=0)



    root.mainloop()


def log_in():
    global win, root
    win.withdraw()
    root = ctk.CTk()
    root.iconbitmap("icon.ico")
    root.title("Авторизация")
    root.geometry("400x500+700+250")
    root.config(bg="#F2E1D0")

    def open_credentials():
        global data, dictionary
        login = entry_login.get()
        password = entry_pass.get()
        with open("users.json", "r") as f:
            data = json.load(f)
            for dictionary in data:
                if dictionary["username"] == login:
                    for dictionary in data:
                        if dictionary["password"] == password:
                            return True

    def autorization():
        global mail, password, login
        login = entry_login.get()
        password = entry_pass.get()
        if not login or not password:
            messagebox.showerror("Error", "Please enter your login and password correctly.")
            return
        if open_credentials():
            root.destroy()
            win.destroy()
            menu(login)

        else:
            messagebox.showerror("Error", "Incorrect login or password!")

    def toggle_password():
        if entry_pass.cget("show") == "*":
            entry_pass.configure(show="")
            eye_button.configure(text="👁️")
        else:
            entry_pass.configure(show="*")
            eye_button.configure(text="🙈")


    titleReg = ctk.CTkLabel(master=root, width=80, height=80, corner_radius=20, fg_color="#D4C7B4", bg_color="#F2E1D0",
                         text="Авторизация",
                         text_color="#854627", font=("Bahnschrift Light", 50))
    titleReg.pack(padx=10, pady=45)

    entry_login = ctk.CTkEntry(master=root, width=350, height=60, corner_radius=20, bg_color="#F2E1D0",
                               fg_color="#D4C7B4", placeholder_text="Логин", placeholder_text_color="#c97349",
                               font=("Bahnschrift Light", 20), text_color="#854627",border_width=0)
    entry_login.pack(pady=10)
    login = entry_login.get()
    entry_pass = ctk.CTkEntry(master=root, width=350, height=60, corner_radius=20, bg_color="#F2E1D0",
                              fg_color="#D4C7B4", placeholder_text="Пароль", placeholder_text_color="#c97349",
                              font=("Bahnschrift Light", 20), text_color="#854627",border_width=0)
    entry_pass.pack(pady=10)
    password = entry_pass.get()
    eye_button = ctk.CTkButton(master=root, text="👁️", width=0, height=0, corner_radius=20,
                               command=toggle_password, fg_color="#D4C7B4", bg_color="#D4C7B4",
                               hover_color="#D4C7B4", text_color="#c97349",
                               font=("Arial", 20))
    eye_button.place(in_=entry_pass, relx=1, x=-60, y=15)
    registration = ctk.CTkButton(root, width=150, height=40, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Войти",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=autorization)
    registration.pack(pady=30)
    back_button = ctk.CTkButton(root, width=130, height=40, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Назад",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=back)
    back_button.pack(pady=0)


    root.mainloop()

def info_window(log):
    global info_win
    login = log

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

    def update_note():
        global photo, selected_file_path

        """with open(selected_file_path, "rb") as file:
            binary_data = file.read()"""

        name = name_ent.get()
        fam = fam_ent.get()
        ot = o_ent.get()
        post = post_ent.get()
        phone = num_ent.get()

        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute(
                """INSERT INTO schema_table.contacts (Имя, Фамилия, Отчество, Должность, Телефон, Фото)
                 VALUES (%s, %s, %s, %s, %s, %s);""",
                (name, fam, ot, post, phone, Binary(photo)))
            conn.commit()
            cur.close()
            conn.close()


        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить данные: {e}")

    def open_users():
        global data, login
        name = name_ent.get()
        try:
            with open("users.json", "r") as f:
                data = json.load(f)

                found = False
                for user in data:
                    if user["username"] == login:
                        user["name"] = name
                        found = True
                        break

                if found:
                        update_note()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при обновлении users.json:\n{e}")

    def choose_photo():
        global photo, selected_file_path
        photo = ""
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if file_path:
            selected_file_path = file_path
            image = Image.open(file_path)
            image.thumbnail((400, 600))
            photo = ImageTk.PhotoImage(image)

            image_label.image = photo
            image_label.configure(image=photo)
            image_label.configure(text="")

    def mene():
        global info_win
        if name_ent.get() == "" or fam_ent.get() == "" or o_ent.get() == "" or num_ent.get() == "" or photo == "":
            messagebox.showerror("Ошибка", f"Введите данные!")
        else:
            open_users()
            info_win.destroy()
            menu(log)



    info_win = ctk.CTk()
    info_win.geometry("800x600+400+100")
    info_win.title("Контактная информация")
    info_win.resizable(False, False)
    info_win.iconbitmap("icon.ico")
    info_win.config(bg="#F2E1D0")

    frame = ctk.CTkFrame(info_win, width=800, height=600, fg_color="#F2E1D0", bg_color="#F2E1D0")
    frame.pack(side=ctk.LEFT,padx=30, pady=10)

    name_ent = ctk.CTkEntry(frame, width=350, height=40, corner_radius=20, bg_color="#F2E1D0", fg_color="#D4C7B4",
                            placeholder_text="Имя",
                            placeholder_text_color="#c97349", font=("Bahnschrift Light", 20),border_width=0)
    name_ent.pack(pady=10)
    fam_ent = ctk.CTkEntry(frame, width=350, height=40, corner_radius=20, bg_color="#F2E1D0", fg_color="#D4C7B4",
                            placeholder_text="Фамилия",
                            placeholder_text_color="#c97349", font=("Bahnschrift Light", 20),border_width=0)
    fam_ent.pack(pady=10)
    o_ent = ctk.CTkEntry(frame, width=350, height=40, corner_radius=20, bg_color="#F2E1D0", fg_color="#D4C7B4",
                            placeholder_text="Отчество",
                            placeholder_text_color="#c97349", font=("Bahnschrift Light", 20),border_width=0)
    o_ent.pack(pady=10)
    post_ent = ctk.CTkEntry(frame, width=350, height=40, corner_radius=20, bg_color="#F2E1D0", fg_color="#D4C7B4",
                            placeholder_text="Должность",
                            placeholder_text_color="#c97349", font=("Bahnschrift Light", 20),border_width=0)
    post_ent.pack(pady=10)
    num_ent = ctk.CTkEntry(frame, width=350, height=40, corner_radius=20, bg_color="#F2E1D0", fg_color="#D4C7B4",
                            placeholder_text="Контактный телефон",
                            placeholder_text_color="#c97349", font=("Bahnschrift Light", 20),border_width=0)
    num_ent.pack(pady=10)
    table_button = ctk.CTkButton(frame, width=175, height=40, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Расписание(PDF\Exel)",
                                text_color="#854627", font=("Bahnschrift Light", 20))
    table_button.pack(pady=10, anchor="w")
    photo_button = ctk.CTkButton(frame, width=175, height=40, corner_radius=20, bg_color="#F2E1D0",
                             fg_color="#D4C7B4", hover_color="#B28753", text="Фото",
                             text_color="#854627", font=("Bahnschrift Light", 20), command=choose_photo)
    photo_button.pack(pady=10, anchor="w")
    _button = ctk.CTkButton(frame, width=175, height=40, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Продолжить",
                                 text_color="#854627", font=("Bahnschrift Light", 20), command=mene)
    _button.pack(pady=30, anchor="w")

    image_frame = ctk.CTkFrame(info_win, width=800, height=400, fg_color="#D4C7B4", bg_color="#F2E1D0")
    image_frame.pack(side=ctk.RIGHT,padx=30, pady=30,anchor="e")

    image_label = ctk.CTkLabel(image_frame, width=800, height=400, fg_color="#D4C7B4", bg_color="#F2E1D0", text="Фото",
                                text_color="#854627", font=("Bahnschrift Light", 20))
    image_label.pack()

    info_win.mainloop()


def menu(login):
    global menu_win

    def table():
        global menu_win
        menu_win.destroy()
        from table_window import table_wind
        table_wind()

    def group():
        global menu_win
        menu_win.destroy()
        from groups_window import groups
        groups()

    def stat():
        global menu_win
        menu_win.destroy()
        from stat_window import statistics_win
        statistics_win()

    def plan_():
        global menu_win
        menu_win.destroy()
        from plan_window import plan_wind
        plan_wind()

    def labs():
        global menu_win
        menu_win.destroy()
        from labs_window import labs_win
        labs_win()

    def meny():
        global menu_win
        log = None
        menu_win.destroy()
        info_window(log)

    def create_rounded_avatar():
        image = Image.open("icon.ico")
        image = image.resize((60, 60), Image.LANCZOS)
        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + image.size, fill=255)
        output_image = Image.new("RGBA", image.size)
        output_image.paste(image, (0, 0), mask)

        # Возвращаем объект CTkImage
        return CTkImage(output_image, size=image.size)

    menu_win = ctk.CTk()
    menu_win.geometry("800x600+400+100")
    menu_win.title("Меню")
    menu_win.config(bg="#F2E1D0")
    menu_win.iconbitmap("icon.ico")
    menu_win.resizable(False,False)

    buttons_frame = ctk.CTkFrame(menu_win, width=200, height=550, corner_radius=20, bg_color="#F2E1D0", fg_color="#F2E1D0")
    buttons_frame.pack(side=ctk.LEFT, padx=30)

    notes_frame = ctk.CTkFrame(menu_win, width=650, height=550, corner_radius=20, bg_color="#F2E1D0", fg_color="#D4C7B4")
    notes_frame.pack(side=ctk.RIGHT, padx=30)

    photo = create_rounded_avatar()
    photo_icon = ctk.CTkLabel(buttons_frame, text="", image=photo)
    photo_icon.place(x=10, y=10)
    button_info = ctk.CTkButton(buttons_frame, width=100, height=60, corner_radius=20, bg_color="#F2E1D0",
                             fg_color="#D4C7B4", hover_color="#B28753", text=f"{login}",
                             text_color="#854627", font=("Bahnschrift Light", 20), command=meny)
    button_info.pack(pady=10, anchor="e")
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Расписание",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=table)
    button_table.pack(pady=10)
    button_groups = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Группы",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=group)
    button_groups.pack(pady=10)
    button_stat = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Статистика",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=stat)
    button_stat.pack(pady=10)
    button_plan = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Уч план",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=plan_)
    button_plan.pack(pady=10)
    button_labs = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Лабораторные",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=labs)
    button_labs.pack(pady=10)
    button_exit = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Выход",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=exit)
    button_exit.pack(pady=10)


    menu_win.mainloop()


def main():
    global win
    win = ctk.CTk()

    win.geometry("800x600+400+100")
    win.title("Добро пожаловать!")
    win.resizable(False, False)
    win.iconbitmap("icon.ico")
    win.config(bg="#F2E1D0")

    title = ctk.CTkLabel(master=win, width=80, height=80, corner_radius=20, fg_color="#D4C7B4", bg_color="#F2E1D0",
                         text="  Добро пожаловать!  ",
                         text_color="#854627", font=("Bahnschrift Light", 50))
    title.pack(padx=20, pady=60)

    buttonReg = ctk.CTkButton(master=win, width=40, height=40, corner_radius=60, hover_color="#B28753",
                              bg_color="#F2E1D0", fg_color="#D4C7B4", text_color="#854627",
                              font=("Bahnschrift Light", 40), text="  Регистрация  ", command=registry)
    buttonReg.pack(padx=10, pady=40)

    buttonAvt = ctk.CTkButton(master=win, width=40, height=40, corner_radius=60, hover_color="#B28753",
                              bg_color="#F2E1D0", fg_color="#D4C7B4", text_color="#854627",
                              font=("Bahnschrift Light", 40), text=" Авторизация ", command=log_in)
    buttonAvt.pack(padx=10, pady=10)

    buttonEx = ctk.CTkButton(master=win, width=60, height=50, corner_radius=60, hover_color="#B28753",
                             bg_color="#F2E1D0", fg_color="#D4C7B4", text_color="#854627",
                             font=("Bahnschrift Light", 30), text=" Выход ", command=ex)
    buttonEx.pack(padx=10, pady=39)



    win.mainloop()


if __name__ == "__main__":
    main()

