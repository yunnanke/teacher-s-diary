import customtkinter as ctk

def back():
    from main_menu import menu
    stat_win.destroy()
    menu()

def statistics_win():
    global stat_win
    stat_win = ctk.CTk()
    stat_win.geometry("1000x800+300+50")
    stat_win.title("Группы")
    stat_win.config(bg="#F2E1D0")
    stat_win.iconbitmap("icon.ico")
    stat_win.resizable(False, False)

    up_buttons_frame = ctk.CTkFrame(stat_win, width=200, height=200, corner_radius=20, bg_color="#F2E1D0",
                                    fg_color="#F2E1D0")
    up_buttons_frame.pack(side="top", padx=30, pady=50, anchor="w")
    buttons_frame = ctk.CTkFrame(stat_win, width=200, height=200, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#F2E1D0")
    buttons_frame.pack(side="top", padx=30, pady=80, anchor="w")

    notes_frame = ctk.CTkFrame(stat_win, width=650, height=700, corner_radius=20, bg_color="#F2E1D0",
                               fg_color="#D4C7B4")
    notes_frame.place(x=300, y=50)
    button_info = ctk.CTkButton(up_buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Группы",
                                text_color="#854627", font=("Bahnschrift Light", 20))
    button_info.pack(pady=10)
    button_info = ctk.CTkButton(up_buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                fg_color="#D4C7B4", hover_color="#B28753", text="Предмет",
                                text_color="#854627", font=("Bahnschrift Light", 20))
    button_info.pack(pady=10)
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Успеваемость",
                                 text_color="#854627", font=("Bahnschrift Light", 20))
    button_table.pack(pady=10)
    button_table = ctk.CTkButton(buttons_frame, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Посещаемость",
                                 text_color="#854627", font=("Bahnschrift Light", 20))
    button_table.pack(pady=10)
    button_table = ctk.CTkButton(stat_win, width=200, height=60, corner_radius=20, bg_color="#F2E1D0",
                                 fg_color="#D4C7B4", hover_color="#B28753", text="Назад",
                                 text_color="#854627", font=("Bahnschrift Light", 20), command=back)
    button_table.place(x=30, y=692)

    stat_win.mainloop()


"""if "__name__" == "__main__":
    groups()"""
statistics_win()