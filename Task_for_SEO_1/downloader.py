
import calculations
import front
import pandas as pd
from tkinter import filedialog, messagebox


# Функция для загрузки и обработки файла CSV
def load_csv():
    read_file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv")],
        title="Выберите csv файл"
    )
    headers = pd.read_csv(read_file_path, nrows=0).columns.tolist()
    front.choise_column_window(headers, read_file_path)


# Функция для сохранения CSV-файла
def save_csv(total_headers, read_file_path):
    global data_csv
    data_csv = pd.read_csv(read_file_path, usecols=[total_headers[0]])
    new_data = calculations.calc_column(total_headers, data_csv)
    if 'data_csv' in globals():  # Проверка, загружены ли данные
        # Открытие диалога для сохранения файла
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Сохраните CSV файл"
        )
        if file_path:
            try:
                # Сохранение данных в новый файл
                new_data.to_csv(file_path, index=False)
                messagebox.showinfo("Успех", "Файл успешно сохранен!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при сохранении файла:\n{e}")
    else:
        messagebox.showwarning("Предупреждение", "Сначала загрузите данные.")


# Функция для загрузки и обработки файла CSV
def load_xlsx():
    global data_xlsx  # Глобальная переменная для хранения данных xlsx
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.xlsx")],
        title="Выберите xlsx файл"
    )
    headers = pd.read_csv(file_path, nrows=0).columns.tolist()
    print(headers)

    column_name = headers[
        int(input(f"Выберите колонку: {[f"{i} - {name}" for i, name in enumerate(headers, start=0)]}"))]
    data = pd.read_csv(file_path, usecols=[column_name])

    print(data)