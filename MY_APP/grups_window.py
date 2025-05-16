import customtkinter as ctk

def back():
    from main_menu import menu
    groups_win.destroy()
    menu()

def groups():
    global groups_win
    groups_win = ctk.CTk()
    groups_win.geometry("1000x800+300+50")
    groups_win.title("Группы")
    groups_win.config(bg="#F2E1D0")
    groups_win.iconbitmap("icon.ico")
    groups_win.resizable(False, False)

    buttons_frame = ctk.CTkFrame(groups_win, width=200, height=400, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#F2E1D0")
    buttons_frame.pack(side=ctk.LEFT, padx=30, pady=50,  anchor="n")

    notes_frame = ctk.CTkFrame(groups_win, width=650, height=700, corner_radius=20, bg_color="#F2E1D0", fg_color="#D4C7B4")
    notes_frame.pack(side=ctk.RIGHT, padx=30)
    button_info = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Группы",
                                text_color="#854627", font=("Bahnschrift Light", 20))
    button_info.pack(pady=10)
    button_info = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Редактировать",
                                text_color="#854627", font=("Bahnschrift Light", 20))
    button_info.pack(pady=10)
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Отметки",
                                 text_color="#854627", font=("Bahnschrift Light", 20))
    button_table.pack(pady=10)
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Посещаемость",
                                 text_color="#854627", font=("Bahnschrift Light", 20))
    button_table.pack(pady=10)
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Лабораторные",
                                 text_color="#854627", font=("Bahnschrift Light", 20))
    button_table.pack(pady=10)
    button_table = ctk.CTkButton(groups_win, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Назад",
                                 text_color="#854627", font=("Bahnschrift Light", 20), command=back)
    button_table.place(x=30, y=692)

    groups_win.mainloop()


"""if "__name__" == "__main__":
    groups()"""
groups()