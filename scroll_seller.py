import tkinter as tk
from datetime import datetime
from tkinter import font
import tkinter.messagebox as box
from tkcalendar import Calendar


# Ограничение ввода только цифрами
def validate_input_only_numbers(in_str, acttyp):
    if acttyp == '1':
        return in_str.isdigit()
    return True

# Ограничение ввода только буквами
def validate_input_only_letters(in_str, acttyp):
    if acttyp == '1':
        return in_str[-1].isalpha()
    return True

# Записываем данные из формы в словарь
def replace_in_contract(data):
    # Словарь соответствия между ключами data и метками в файле
    mapping = {
        "entry_last_name_seller": "%last_name_seller%",
        "entry_first_name_seller": "%first_name_seller%",
        "entry_patronymic_seller": "%patronymic_seller%",
        "entry_date_birth_seller": "%date_birth_seller%",
        "entry_series_number_seller": "%series_number_seller%",
        "entry_date_issue_seller": "%date_issue_seller%",
        "entry_issue_seller": "%issue_seller%",
        "entry_cadastral_number_seller": "%cadastral_number_seller%",
        "entry_address_seller": "%address_seller%",

    }
    print('replace_in_contract', data)
    print('mapping', mapping)

    file_path = 'dogovor.txt'
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
        print(content)

    for key, value in mapping.items():
        if key in data:
            content = content.replace(value, data[key])

    print(content)

    # Генерируем новое имя файла: договор_Фамилия_ГГГГ_ММ_ДД.txt
    # last_name = data.get("entry_last_name_seller", "продавец")
    # timestamp = datetime.now().strftime("%Y_%m_%d")
    # new_file_name = f"dogovor_{last_name}_{timestamp}.txt"
    # print(last_name, timestamp, new_file_name)

    # with open(new_file_name, 'w', encoding="utf-8") as file:
    #     file.write(content)
    # 
    # print(f'Договор сохранён в файл: {new_file_name}')

    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(content)

        # print(f'Договор сохранён в файл: {new_file_name}')
    print(f'Договор успешно обновлен')

# Записываем данные из формы в словарь
def write_values():
    data = {
        "entry_last_name_seller": entry_last_name_seller.get(),
        "entry_first_name_seller": entry_first_name_seller.get(),
        "entry_patronymic_seller": entry_patronymic_seller.get(),
        "entry_date_birth_seller": entry_date_birth_seller.get(),
        "entry_series_number_seller": entry_series_number_seller.get(),
        "entry_date_issue_seller": entry_date_issue_seller.get(),
        "entry_issue_seller": entry_issue_seller.get("1.0", tk.END).strip(),
        "entry_cadastral_number_seller": entry_cadastral_number_seller.get(),
        "entry_address_seller": entry_address_seller.get("1.0", tk.END).strip(),
    }
    print(data)
    replace_in_contract(data)
    return data

# Добавляем функцию для показа календаря
def show_calendar(entry_widget):
    """Открывает окно с календарем и вставляет выбранную дату в поле ввода."""
    def select_date():
        # Получаем выбранную дату в формате ДД.ММ.ГГГГ
        selected_date = cal.get_date() #возвращает выбранную пользователем дату в нужном формате (dd.mm.yyyy)
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, selected_date)
        top.destroy()

    top = tk.Toplevel()
    top.title("Выбор даты")
    top.geometry("300x250")
    top.grab_set()  # Делаем окно модальным (гарантирует, что пользователь не сможет взаимодействовать с главным окном, пока не закроет календарь)

    # Создаем виджет календаря
    cal = Calendar(top, selectmode='day', date_pattern='dd.mm.yyyy')
    cal.pack(pady=20)

    # Кнопка для подтверждения выбора
    select_btn = tk.Button(top, text="Выбрать", command=select_date)
    select_btn.pack()


# ----------- Tkinter -----------
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

lb_last_name_seller = tk.Label(frame_personal, text = "Фамилия: ", font = label_font)
entry_last_name_seller = tk.Entry(frame_personal, font = label_font,  validate='key')
entry_last_name_seller['validatecommand'] = (entry_last_name_seller.
                                       register(validate_input_only_letters),
                                       '%P', '%d')

lb_first_name_seller = tk.Label(frame_personal, text = "Имя: ", font = label_font)
entry_first_name_seller = tk.Entry(frame_personal, font = label_font,  validate='key')
entry_first_name_seller['validatecommand'] = (entry_first_name_seller.
                                       register(validate_input_only_letters),
                                       '%P', '%d')

lb_patronymic_seller = tk.Label(frame_personal, text = "Отчество: ", font = label_font)
entry_patronymic_seller = tk.Entry(frame_personal, font = label_font,  validate='key')
entry_patronymic_seller['validatecommand'] = (entry_patronymic_seller.
                                       register(validate_input_only_letters),
                                       '%P', '%d')

lb_date_birth_seller = tk.Label(frame_personal, text = "Дата рождения: ", font = label_font)
entry_date_birth_seller = tk.Entry(frame_personal, font = label_font,  validate='key')
entry_date_birth_seller.bind("<Button-1>", lambda event: show_calendar(entry_date_birth_seller))

lb_last_name_seller.grid(row = 1, column = 1)
entry_last_name_seller.grid(row = 1, column = 2)
lb_empty_1.grid(row = 2)
lb_first_name_seller.grid(row = 3, column = 1)
entry_first_name_seller.grid(row = 3, column = 2)
lb_empty_2.grid(row = 4)
lb_patronymic_seller.grid(row = 5, column = 1)
entry_patronymic_seller.grid(row = 5, column = 2)
lb_empty_3.grid(row = 6)
lb_date_birth_seller.grid(row = 7, column = 1)
entry_date_birth_seller.grid(row = 7, column = 2)

frame_passport = tk.LabelFrame(scrollable_frame, text = "Паспортные данные", font = frame_font)
frame_passport.pack(padx = 20, pady = 20, fill = tk.X)

lb_empty_1_passport = tk.Label(frame_passport, text = " ", font = label_font)
lb_empty_2_passport = tk.Label(frame_passport, text = " ", font = label_font)
lb_empty_3_passport = tk.Label(frame_passport, text = " ", font = label_font)

lb_series_number_seller = tk.Label(frame_passport, text = "Серия номер: ", font = label_font)
entry_series_number_seller = tk.Entry(frame_passport, font = label_font,  validate='key')
entry_series_number_seller['validatecommand'] =\
    (entry_series_number_seller.register(validate_input_only_numbers), '%P', '%d')

lb_date_issue_seller = tk.Label(frame_passport, text = "Дата выдачи: ", font = label_font)
entry_date_issue_seller = tk.Entry(frame_passport, font = label_font)
entry_date_issue_seller.bind("<Button-1>", lambda event: show_calendar(entry_date_issue_seller))

lb_issue_seller = tk.Label(frame_passport, text = "Кем выдан: ", font = label_font)
entry_issue_seller = tk.Text(frame_passport, width = 30, height = 5, font = frame_font, wrap = tk.WORD)

lb_series_number_seller.grid(row = 1, column = 1)
entry_series_number_seller.grid(row = 1, column = 2)
lb_empty_1_passport.grid(row = 2)
lb_date_issue_seller.grid(row = 3, column = 1)
entry_date_issue_seller.grid(row = 3, column = 2)
lb_empty_2_passport.grid(row = 4)
lb_issue_seller.grid(row = 5, column = 1)
entry_issue_seller.grid(row = 5, column = 2)

frame_object = tk.LabelFrame(scrollable_frame, text = "Объект недвижимости", font = frame_font)
frame_object.pack(padx = 20, pady = 20, fill = tk.X)

lb_empty_1_object = tk.Label(frame_object, text = " ", font = label_font)
lb_empty_2_object = tk.Label(frame_object, text = " ", font = label_font)
lb_empty_3_object = tk.Label(frame_object, text = " ", font = label_font)

lb_cadastral_number_seller = tk.Label(frame_object, text = "Кадастровый номер: ", font = label_font)
entry_cadastral_number_seller = tk.Entry(frame_object, font = label_font)

lb_address_seller = tk.Label(frame_object, text = "Адрес: ", font = label_font)
entry_address_seller = tk.Text(frame_object, width = 23, height = 5, font = frame_font, wrap = tk.WORD)

lb_cadastral_number_seller.grid(row = 1, column = 1)
entry_cadastral_number_seller.grid(row = 1, column = 2)
lb_empty_1_object.grid(row = 2)
lb_address_seller.grid(row = 3, column = 1)
entry_address_seller.grid(row = 3, column = 2)

# --- Кнопка (row = 2) ---
def dialog():
    var = box.askyesno("Выбор действий", "Завершить заполнение данных?")
    if var == 1:
        write_values()
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