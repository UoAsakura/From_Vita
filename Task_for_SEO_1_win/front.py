
import downloader
import tkinter as tk
from PIL import Image, ImageTk
from time import sleep

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
def choise_column_window(args, read_file_path, format):
    new_window = tk.Toplevel()  # Создание нового окна
    # Задаем желаемые размеры окна
    window_width = 400; window_height = len(args) * 50 if len(args) > 100 else 500
    center_window(new_window, window_width, window_height)
    # Загружаем изображение (необходимо чтобы оно было в одном каталоге с программой или указать полный путь)
    image = Image.open("static/sunset.jpg")
    # Преобразуем изображение для использования в tkinter
    bg_image = ImageTk.PhotoImage(image)
    # Создаем Label, который будет фоном, и устанавливаем изображение
    background_label = tk.Label(new_window, image=bg_image)
    background_label.place(relwidth=1, relheight=1)  # Располагаем его на весь размер окна
    # Чтобы изображение не удалилось при сборке мусора, сохраняем его ссылку
    background_label.image = bg_image

    def print_selection():
        selection = lbox.curselection() # Список выбраных колонок.
        if [lbox.get(i) for i in selection]:
            match format:
                case "csv":
                    downloader.save_csv([lbox.get(i) for i in selection], read_file_path)
                case "xlsx":
                    downloader.save_xlsx([lbox.get(i) for i in selection], read_file_path)
            new_window.destroy() # Закрытие окна после записи нового файла.
        else:
            tk.Label(new_window, text="Ни одна из колонок не выбрана!", font=("Arial", 12),).pack()

    new_window.title("Выбор колонок")  # Заголовок окна
    tk.Label(new_window, text="Все колонки из файла:", font=("Arial", 11),).pack()
    # Список полей для выбора с возможностью множественного выбора.
    lbox = tk.Listbox(new_window, width=20, height=len(args) + 1, selectmode=tk.MULTIPLE)
    lbox.pack(pady=10)

    for i, name in enumerate(args):
        lbox.insert(i, name)
    tk.Button(new_window,
              text="Выбрать колонки",
              font=("Arial", 12),
              bg="lightblue",
              command=print_selection).pack(pady=10)




# Функция для развёртывания главного окна.
def create_open_window():
    root = tk.Tk()  # Создаем главное окно приложения
    # Задаем желаемые размеры окна
    window_width = 600; window_height = 300
    center_window(root, window_width, window_height)
    root.title("Обработчик файлов")  # Заголовок окна

    # Загружаем изображение (необходимо чтобы оно было в одном каталоге с программой или указать полный путь)
    image = Image.open("static/sea.jpg")
    # Преобразуем изображение для использования в tkinter
    bg_image = ImageTk.PhotoImage(image)
    # Создаем Label, который будет фоном, и устанавливаем изображение
    background_label = tk.Label(root, image=bg_image)
    background_label.place(relwidth=1, relheight=1)  # Располагаем его на весь размер окна
    # Чтобы изображение не удалилось при сборке мусора, сохраняем его ссылку
    background_label.image = bg_image

    # Начальное окно приветствия.
    tk.Label(root, text="Добро пожаловать! \n Выберите тип файла:", font=("Arial", 14, "bold")).pack()
    # Создаем кнопку для загрузки CSV
    load_button_csv = tk.Button(root,
                                text="Загрузить csv ",
                                font=("Arial", 14),
                                bg="lightblue",
                                command=downloader.load_csv).pack(pady=10)
    load_button_xlsx = tk.Button(root,
                                 text="Загрузить xlsx",
                                 font=("Arial", 14),
                                 bg="lightblue",
                                 command=downloader.load_xlsx).pack(pady=10)

    # Запуск GUI
    root.mainloop()


