
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
    front.choise_column_window(headers, read_file_path, "csv")


# Функция для сохранения CSV-файла
def save_csv(total_headers, read_file_path):
    global data_csv
    temporary_data = []
    for i in total_headers:
        data_csv = pd.read_csv(read_file_path, usecols=[i])
        temporary_data.append(calculations.calc_column([i], data_csv))
    res_data = pd.concat([i for i in temporary_data], axis=1)

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
                res_data.to_csv(file_path, index=False)
                messagebox.showinfo("Успех", "Файл успешно сохранен!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при сохранении файла:\n{e}")
    else:
        messagebox.showwarning("Предупреждение", "Сначала загрузите данные.")


# Функция для загрузки и обработки файла XLSX
def load_xlsx():
    global data_xlsx  # Глобальная переменная для хранения данных xlsx
    read_file_path = filedialog.askopenfilename(
        filetypes=[("XLSX files", "*.xlsx")],
        title="Выберите xlsx файл"
    )
    df = pd.read_excel(read_file_path, nrows=0)
    headers = df.columns.tolist() # Получаем заголовки как список
    front.choise_column_window(headers, read_file_path, "xlsx")


# Функция для сохранения CSV-файла
def save_xlsx(total_headers, read_file_path):
    global data_xlsx
    temporary_data = []
    for i in total_headers:
        data_xlsx = pd.read_excel(read_file_path, usecols=[i])
        temporary_data.append(calculations.calc_column([i], data_xlsx))
    res_data = pd.concat([i for i in temporary_data], axis=1)
    if 'data_xlsx' in globals():  # Проверка, загружены ли данные
        # Открытие диалога для сохранения файла
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel файлы", "*.xlsx"), ("Все файлы", "*.*")],
            title="Сохраните XLSX файл"
        )
        if file_path:
            try:
                # Сохранение данных в новый файл
                res_data.to_excel(file_path, index=False)
                messagebox.showinfo("Успех", "Файл успешно сохранен!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при сохранении файла:\n{e}")
    else:
        messagebox.showwarning("Предупреждение", "Сначала загрузите данные.")