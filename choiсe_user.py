import tkinter as tk
import subprocess
import sys

# Получаем путь к файлу договора из аргумента командной строки
if len(sys.argv) > 1:
    contract_file = sys.argv[1]
else:
    contract_file = 'dogovor.txt'  # значение по умолчанию, если аргумент не передан

def run_buyer():
    """Запускает скрипт для ввода данных покупателя."""
    subprocess.Popen([sys.executable, "scroll_buyer.py", contract_file])

def run_seller():
    """Запускает скрипт для ввода данных продавца."""
    subprocess.Popen([sys.executable, "scroll_seller.py", contract_file])

# Создаём главное окно
main = tk.Tk()
main.title("Выбор роли")
main.geometry("300x150")
main.resizable(False, False)

# Заголовок
label = tk.Label(main, text="Выберите участника сделки", font=("Arial", 16))
label.pack(pady=10)

# Кнопка "Покупатель"
btn_buyer = tk.Button(main, text="Покупатель", font=("Arial", 14), width=15, command=run_buyer)
btn_buyer.pack(pady=5)

# Кнопка "Продавец"
btn_seller = tk.Button(main, text="Продавец", font=("Arial", 14), width=15, command=run_seller)
btn_seller.pack(pady=5)

# Кнопка "Выход"
btn_exit = tk.Button(main, text="Выход", font=("Arial", 12), command=main.destroy)
btn_exit.pack(pady=10)

main.mainloop()