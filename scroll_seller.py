import tkinter as tk
from tkinter import font
import tkinter.messagebox as box

window = tk.Tk()
window.title("Ввод данных продавца")
window.geometry("600x800")

# Настраиваем сетку окна (1 столбец, 3 строки)
window.grid_rowconfigure(0, weight = 0)   # заголовок – не растягивается
window.grid_rowconfigure(1, weight = 1)   # прокручиваемая область – растягивается
window.grid_rowconfigure(2, weight = 0)   # кнопка – не растягивается
window.grid_columnconfigure(0, weight = 1)

label_font = font.Font(family = "Arial", size = 18, weight = "bold", slant = "italic")
frame_font = font.Font(family = "Arial", size = 14)

# Заголовок (row = 0)
section_personal = tk.Label(window, text = "Данные продавца", font = label_font)
section_personal.grid(row = 0, column = 0, pady = 10, sticky = "n")   # прижат к верху, по центру

# --- Прокручиваемая область (row = 1) ---
canvas = tk.Canvas(window, highlightthickness = 0)
scrollbar = tk.Scrollbar(window, orient = tk.VERTICAL, command = canvas.yview)
canvas.configure(yscrollcommand = scrollbar.set)

# Помещаем canvas и scrollbar в row = 1, column = 0
canvas.grid(row = 1, column = 0, sticky = "nsew")     # растягивается по всем направлениям
scrollbar.grid(row = 1, column = 1, sticky = "ns")    # располагается справа, растягивается по высоте

# Внутренний фрейм для содержимого
scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window = scrollable_frame, anchor = "nw")

def update_scrollregion(event = None):
    canvas.configure(scrollregion = canvas.bbox("all"))

def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

scrollable_frame.bind("<Configure>", update_scrollregion)
canvas.bind("<Configure>", update_scrollregion)
canvas.bind("<MouseWheel>", on_mousewheel)

# Все фреймы с данными (внутри scrollable_frame)
frame_personal = tk.LabelFrame(scrollable_frame, text = "Основные персональные данные", font = frame_font)
frame_personal.pack(padx = 20, pady = 20, fill = tk.X)

lb_empty_1 = tk.Label(frame_personal, text = " ", font = frame_font)
lb_empty_2 = tk.Label(frame_personal, text = " ", font = frame_font)
lb_empty_3 = tk.Label(frame_personal, text = " ", font = frame_font)

entry_last_name = tk.Entry(frame_personal, font = label_font)
lb_last_name = tk.Label(frame_personal, text = "Фамилия: ", font = label_font)

entry_first_name = tk.Entry(frame_personal, font = label_font)
lb_first_name = tk.Label(frame_personal, text = "Имя: ", font = label_font)

entry_patronymic = tk.Entry(frame_personal, font = label_font)
lb_patronymic = tk.Label(frame_personal, text = "Отчество: ", font = label_font)

entry_date_birth = tk.Entry(frame_personal, font = label_font)
lb_date_birth = tk.Label(frame_personal, text = "Дата рождения: ", font = label_font)

lb_last_name.grid(row = 1, column = 1)
entry_last_name.grid(row = 1, column = 2)
lb_empty_1.grid(row = 2)
lb_first_name.grid(row = 3, column = 1)
entry_first_name.grid(row = 3, column = 2)
lb_empty_2.grid(row = 4)
lb_patronymic.grid(row = 5, column = 1)
entry_patronymic.grid(row = 5, column = 2)
lb_empty_3.grid(row = 6)
lb_date_birth.grid(row = 7, column = 1)
entry_date_birth.grid(row = 7, column = 2)

frame_passport = tk.LabelFrame(scrollable_frame, text = "Паспортные данные", font = frame_font)
frame_passport.pack(padx = 20, pady = 20, fill = tk.X)

lb_empty_1_passport = tk.Label(frame_passport, text = " ", font = label_font)
lb_empty_2_passport = tk.Label(frame_passport, text = " ", font = label_font)
lb_empty_3_passport = tk.Label(frame_passport, text = " ", font = label_font)

entry_series_number = tk.Entry(frame_passport, font = label_font)
lb_series_number = tk.Label(frame_passport, text = "Серия номер: ", font = label_font)

entry_date_issue = tk.Entry(frame_passport, font = label_font)
lb_date_issue = tk.Label(frame_passport, text = "Дата выдачи: ", font = label_font)

entry_issue = tk.Text(frame_passport, width = 30, height = 5, font = frame_font, wrap = tk.WORD)
lb_issue = tk.Label(frame_passport, text = "Кем выдан: ", font = label_font)

lb_series_number.grid(row = 1, column = 1)
entry_series_number.grid(row = 1, column = 2)
lb_empty_1_passport.grid(row = 2)
lb_date_issue.grid(row = 3, column = 1)
entry_date_issue.grid(row = 3, column = 2)
lb_empty_2_passport.grid(row = 4)
lb_issue.grid(row = 5, column = 1)
entry_issue.grid(row = 5, column = 2)

frame_object = tk.LabelFrame(scrollable_frame, text = "Объект недвижимости", font = frame_font)
frame_object.pack(padx = 20, pady = 20, fill = tk.X)

lb_empty_1_object = tk.Label(frame_object, text = " ", font = label_font)
lb_empty_2_object = tk.Label(frame_object, text = " ", font = label_font)
lb_empty_3_object = tk.Label(frame_object, text = " ", font = label_font)

entry_cadastral_number = tk.Entry(frame_object, font = label_font)
lb_cadastral_number = tk.Label(frame_object, text = "Кадастровый номер: ", font = label_font)

entry_address = tk.Text(frame_object, width = 23, height = 5, font = frame_font, wrap = tk.WORD)
lb_address = tk.Label(frame_object, text = "Адрес: ", font = label_font)

lb_cadastral_number.grid(row = 1, column = 1)
entry_cadastral_number.grid(row = 1, column = 2)
lb_empty_1_object.grid(row = 2)
lb_address.grid(row = 3, column = 1)
entry_address.grid(row = 3, column = 2)

# --- Кнопка (row = 2) ---
def dialog():
    var = box.askyesno("Выбор действий", "Завершить заполнение данных?")
    if var == 1:
        box.showwarning("Прекращение", "Данные внесены в договор")
    else:
        box.showinfo("Продолжение", "Продолжаем заполнение...")

btn = tk.Button(window, text = "Выбор решения", bg = "red", fg = "#00ff00",
                width = 20, font = ("Arial", 16, "bold"), command = dialog)
btn.grid(row = 2, column = 0, pady = 20)   # pady - отступ снизу, кнопка автоматически центрируется по горизонтали

# Принудительно обновляем scrollregion
scrollable_frame.update_idletasks()
canvas.configure(scrollregion = canvas.bbox("all"))

window.mainloop()