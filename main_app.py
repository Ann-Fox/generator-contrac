import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import sys
import shutil

def select_file():
    global selected_file
    file_path = filedialog.askopenfilename(initialdir=".", title="Выберите файл")
    if file_path:
        selected_file = file_path
        label.config(text=f"Выбран: {file_path}")

        choice_file_path = os.path.basename(file_path)

        label2.config(text=f"Имя файла: {choice_file_path}")
        label2.pack(pady=20)

        # Передаём полный путь к файлу как аргумент
        subprocess.Popen([sys.executable, "choiсe_user.py", file_path])

        print(selected_file)
        # Выводим только имя файла
        print("Имя файла:", os.path.basename(file_path))
        return choice_file_path
    else:
        print("Файл не выбран")


def create_new_file():
    global selected_file
    template_path = "dogovor.txt"
    if not os.path.exists(template_path):
        label.config(text="Шаблон dogovor.txt не найден!", fg="red")
        return

    # Генерируем имя нового файла на основе текущей даты
    from datetime import datetime
    base_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    new_file_name = f"{base_name}.txt"

    # Если файл уже существует, добавляем суффикс _1, _2 и т.д.
    # counter = 1
    # original_name = new_file_name
    # while os.path.exists(new_file_name):
    #     new_file_name = f"{base_name}_{counter}.txt"
    #     counter += 1

    # Копируем шаблон
    shutil.copy(template_path, new_file_name)

    selected_file = os.path.abspath(new_file_name)
    label.config(text=f"Создан: {new_file_name}")
    label2.config(text=f"Имя файла: {new_file_name}")
    label2.pack(pady=20)

    # Запускаем окно выбора роли, передавая путь к новому файлу
    subprocess.Popen([sys.executable, "choiсe_user.py", selected_file])
    print("Создан файл:", new_file_name)


root = tk.Tk()
root.title("Выбор файла")
root.geometry("500x350")

selected_file = ""

btn = tk.Button(root, text="Выбрать файл", command=select_file)
btn.pack(pady=20)

btn_create = tk.Button(root, text="Создать документ", command=create_new_file)
btn_create.pack(pady=5)

label = tk.Label(root, text="Файл не выбран")
label.pack(pady=10)

label2 = tk.Label(root)

root.mainloop()