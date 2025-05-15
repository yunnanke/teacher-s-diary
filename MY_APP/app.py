import customtkinter as ctk
from PIL import Image, ImageTk


def ex():
    global win
    win.destroy()

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
    login = entry_login.get()
    entry_mail = ctk.CTkEntry(master=root, width=350, height=60, corner_radius=20, bg_color="#F2E1D0",
                               fg_color="#D4C7B4", placeholder_text="Почта", placeholder_text_color="#c97349",
                               font=("Bahnschrift Light", 20), text_color="#854627",border_width=0)
    entry_mail.pack(pady=10)
    mail = entry_mail.get()
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
                                fg_color="#D4C7B4", hover_color="#B28753", text="Зарегистрироваться",
                                text_color="#854627", font=("Bahnschrift Light", 20))
    registration.pack(pady=30)
    back_button = ctk.CTkButton(root, width=130, height=40, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Назад",
                                text_color="#854627", font=("Bahnschrift Light", 20), command=back)
    back_button.pack(pady=0)



    root.mainloop()

def main():
    global win
    win = ctk.CTk()

    win.geometry("800x600+400+100")
    win.title("Добро пожаловать!")
    win.resizable(False, False)
    win.iconbitmap("icon.ico")
    win.config(bg="#F2E1D0")

    image = Image.open("ico.png")
    photo = ImageTk.PhotoImage(image)
    font = ctk.CTkFont(family="Copperplate Gothic Light")

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
                              font=("Bahnschrift Light", 40), text=" Авторизация ")
    buttonAvt.pack(padx=10, pady=10)

    buttonEx = ctk.CTkButton(master=win, width=60, height=50, corner_radius=60, hover_color="#B28753",
                             bg_color="#F2E1D0", fg_color="#D4C7B4", text_color="#854627",
                             font=("Bahnschrift Light", 30), text=" Выход ", command=ex)
    buttonEx.pack(padx=10, pady=39)

    win.mainloop()



main()

