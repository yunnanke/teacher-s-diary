from tkinter import filedialog
import customtkinter as ctk
from PIL import Image, ImageTk


def ex():
    global menu_win
    menu_win.destroy()

def info_window():
    global win, root

    def choose_photo():
        global photo
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if file_path:
            image = Image.open(file_path)
            image.thumbnail((400, 600))
            photo = ImageTk.PhotoImage(image)

            image_label.image = photo
            image_label.configure(image=photo)
            image_label.configure(text="")

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

    image_frame = ctk.CTkFrame(info_win, width=800, height=400, fg_color="#D4C7B4", bg_color="#F2E1D0")
    image_frame.pack(side=ctk.RIGHT,padx=30, pady=30,anchor="e")

    image_label = ctk.CTkLabel(image_frame, width=800, height=400, fg_color="#D4C7B4", bg_color="#F2E1D0", text="Фото",
                                text_color="#854627", font=("Bahnschrift Light", 20))
    image_label.pack()

    info_win.mainloop()


def menu():
    global menu_win

    def table():
        global menu_win
        menu_win.destroy()
        from table_window import table_wind
        table_wind()

    def group():
        global menu_win
        menu_win.destroy()
        from grups_window import groups
        groups()

    def stat():
        global menu_win
        menu_win.destroy()
        from statistics_window import statistics_win
        statistics_win()

    def plan_():
        global menu_win
        menu_win.destroy()
        from plan_window import plan_wind
        plan_wind()

    def labs():
        global menu_win
        menu_win.destroy()
        from Labs_window import labs_win
        labs_win()

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

    #photo_icon =
    button_info = ctk.CTkButton(buttons_frame, width=100, height=60, corner_radius=20, bg_color="#F2E1D0",
                             fg_color="#D4C7B4", hover_color="#B28753", text="{login}",
                             text_color="#854627", font=("Bahnschrift Light", 20))
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
                                text_color="#854627", font=("Bahnschrift Light", 20), command=ex)
    button_exit.pack(pady=10)


    menu_win.mainloop()

if "__name__" == "__main__":
    menu()