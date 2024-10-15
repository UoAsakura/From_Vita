
import downloader
import tkinter as tk


# Функция для центрирования окна
def center_window(window, width, height):
    # Получаем размеры экрана
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Вычисляем координаты для размещения окна по центру
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    # Устанавливаем размеры и позицию окна
    window.geometry(f"{width}x{height}+{x}+{y}")


# Фнукция для выбора колонок.
def choise_column_window(args, read_file_path):
    new_window = tk.Toplevel()  # Создание нового окна
    # Задаем желаемые размеры окна
    window_width = 400; window_height = len(args) * 50 if len(args) > 100 else 500
    center_window(new_window, window_width, window_height)

    def print_selection():
        selection = lbox.curselection()
        # print([lbox.get(i) for i in selection])
        # print(selection)
        downloader.save_csv([lbox.get(i) for i in selection], read_file_path)

    new_window.title("Выбор колонок")  # Заголовок окна
    tk.Label(new_window, text="Все колонки из файла:").pack(pady=5)
    lbox = tk.Listbox(new_window, width=20, height=len(args) + 1, selectmode=tk.MULTIPLE)
    lbox.pack()
    for i, name in enumerate(args):
        lbox.insert(i, name)
    return_data = tk.Button(new_window, text="Выбрать колонки", command=print_selection).pack(pady=10)
    # for i, name in enumerate(args):
    #     tk.Label(new_window, text=f"{i}.{name}").pack()
    #
    # def get_vars():
    #     if not select_columns.get():
    #         tk.Label(new_window, text="Введите номер(а) колонок").pack()
    #     elif not all(i.isdigit() for i in select_columns.get().split()):
    #         tk.Label(new_window, text="Введите номер(а) колонок через пробел").pack()
    #     else:
    #         # result = select_columns.get()
    #         downloader.save_csv()
    #
    # select_columns = tk.Entry(new_window)
    # select_columns.pack(pady=5)
    # tk.Button(new_window, text="Выбрать", command=get_vars).pack(pady=5)


# Функция для развёртывания главного окна.
def create_open_window():
    root = tk.Tk()  # Создаем главное окно приложения
    # Задаем желаемые размеры окна
    window_width = 400; window_height = 300
    center_window(root, window_width, window_height)
    root.title("Обработчик файлов")  # Заголовок окна
    # Начальное окно приветствия.
    tk.Label(root, text="Добро пожаловать! \n Выберите тип файла:").pack()
    # Создаем кнопку для загрузки CSV
    load_button_csv = tk.Button(root, text="Загрузить csv", command=downloader.load_csv).pack(pady=10)
    load_button_xlsx = tk.Button(root, text="Загрузить xlsx", command=downloader.load_xlsx).pack(pady=10)

    # Запуск GUI
    root.mainloop()
