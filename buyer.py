# import tkinter as tk
# from tkinter import font
# import tkinter.messagebox as box
#
# #Создаем окно
# window = tk.Tk()
#
# #Создаем заголовок окна
# window.title("Ввод данных покупателя")
#
# # Создаём объект шрифта
# label_font = font.Font(family="Arial", size=20, weight="bold", slant="italic")
# frame_font = font.Font(family="Arial", size=14)
#
# # Section 1
# section_personal = tk.Label(window, text = "Данные покупателя", font = label_font)
# section_personal.pack(side = tk.TOP)
#
# # Фрейм для ввода персональных данных
# frame_personal = tk.LabelFrame(window, text = "Основные персональные данные", font = frame_font)
# frame_personal.pack(padx = 20, pady = 20)
#
# lb_empty_1 = tk.Label(frame_personal, text = " ", font = frame_font)
# lb_empty_2 = tk.Label(frame_personal, text = " ", font = frame_font)
# lb_empty_3 = tk.Label(frame_personal, text = " ", font = frame_font)
#
# # Фамилия
# entry_last_name = tk.Entry(frame_personal, font = label_font)
# lb_last_name = tk.Label(frame_personal, text = "Фамилия: ", font = label_font)
#
# # Имя
# entry_first_name = tk.Entry(frame_personal, font = label_font)
# lb_first_name = tk.Label(frame_personal, text = "Имя: ", font = label_font)
#
# # Отчество
# entry_patronymic = tk.Entry(frame_personal, font = label_font)
# lb_patronymic = tk.Label(frame_personal, text = "Отчество: ", font = label_font)
#
# # Дата рождения
# entry_date_birth = tk.Entry(frame_personal, font = label_font)
# lb_date_birth = tk.Label(frame_personal, text = "Дата рождения: ", font = label_font)
#
# # Располагаем метки в таблице
# lb_last_name.grid(row = 1, column = 1)
# entry_last_name.grid(row = 1, column = 2)
# lb_empty_1.grid(row = 2)
# lb_first_name.grid(row = 3, column = 1)
# entry_first_name.grid(row = 3, column = 2)
# lb_empty_2.grid(row = 4)
# lb_patronymic.grid(row = 5, column = 1)
# entry_patronymic.grid(row = 5, column = 2)
# lb_empty_3.grid(row = 6)
# lb_date_birth.grid(row = 7, column = 1)
# entry_date_birth.grid(row = 7, column = 2)
#
# # Фрейм для ввода паспортных данных
# frame_passport = tk.LabelFrame(window, text = "Паспортные данные", font = frame_font)
# frame_passport.pack(padx = 100, pady = 20)
#
# lb_empty_1_passport = tk.Label(frame_passport, text = " ", font = label_font)
# lb_empty_2_passport = tk.Label(frame_passport, text = " ", font = label_font)
# lb_empty_3_passport = tk.Label(frame_passport, text = " ", font = label_font)
#
# # Серия номер
# entry_series_number = tk.Entry(frame_passport, font = label_font)
# lb_series_number = tk.Label(frame_passport, text = "Серия номер: ", font = label_font)
#
# # Дата выдачи
# entry_date_issue = tk.Entry(frame_passport, font = label_font)
# lb_date_issue = tk.Label(frame_passport, text = "Дата выдачи: ", font = label_font)
#
# # Кем выдан
# entry_issue = tk.Text(frame_passport, width=30, height=5, font = frame_font, wrap = tk.WORD)
# lb_issue = tk.Label(frame_passport, text = "Кем выдан: ", font = label_font)
#
# lb_series_number.grid(row = 1, column = 1)
# entry_series_number.grid(row = 1, column = 2)
# lb_empty_1_passport.grid(row = 2)
# lb_date_issue.grid(row = 3, column = 1)
# entry_date_issue.grid(row = 3, column = 2)
# lb_empty_2_passport.grid(row = 4)
# lb_issue.grid(row = 5, column = 1)
# entry_issue.grid(row = 5, column = 2)
#
# def dialog():
#     var = box.askyesno("Выбор действий", "Завершить заполнение данных?")
#     if var == 1:
#         box.showwarning("Прекращение", "Данные внесены в договор")
#     else:
#         box.showinfo("Продолжение", "Продолжаем заполнение...")
#
# #Создаем кнопку для выхода из программы
# btn = tk.Button(window, text = "Выбор решения", bg = "red", fg = "#00ff00", width = 20, font = ("Arial", 16,
# "bold"), command = dialog)
# btn.pack(padx = 80, pady = 80) #Размещаем кнопку в окне
#
# # #Цикл обработки событий
# window.mainloop()