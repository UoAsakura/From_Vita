import tkinter as tk

def command_one():
    print("Команда 1 выполнена!")

def command_two():
    print("Команда 2 выполнена!")

def combined_command():
    command_one()
    command_two()

# Основное окно приложения
root = tk.Tk()
root.title("Несколько команд")
root.geometry("300x200")

# Кнопка, вызывающая комбинированную команду
button = tk.Button(root, text="Нажми меня", command=combined_command)
button.pack(pady=50)

# Запуск основного цикла приложения
root.mainloop()
