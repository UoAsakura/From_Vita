import csv
import sys
import os

my_set_eng = {"c", "p", "o", "e", "x", "b", "k", "h", "a", "t"}
rus_alph = {'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'}


def check_string(s: str) -> dict:
    bad_ind = dict()
    for i in range(1, len(s) - 1):
        if s[i].lower() in my_set_eng and (s[i - 1].lower() in rus_alph or s[i + 1].lower() in rus_alph):
            bad_ind[i] = s[i]
    return bad_ind


def main():
    # Проверка на наличие трех аргументов (пути к файлам)
    if len(sys.argv) != 2:
        print("Usage: python3 task3.py <file.csv>")
        return

    # Указываем путь к исходному файлу CSV
    input_file_path = sys.argv[1]

    # Указываем путь для нового файла CSV
    output_file_path = input("Введите название для нового файла:")

    # Чтение данных из исходного файла и запись в новый CSV файл
    with (open(input_file_path, mode='r', encoding='utf-8') as infile,
          open(output_file_path, mode='w', encoding='utf-8',newline='') as outfile):

        # Чтение CSV файла как словаря
        csv_reader = csv.DictReader(infile)

        # Указываем исходные колонки и добавляем новую колонку
        columns_to_read = ['H1-1']  # Замените на нужные вам колонки
        new_column = 'Опечатки'  # Название новой колонки
        all_columns = columns_to_read + [new_column]

        # Создаем объект для записи CSV файла с новой колонкой
        csv_writer = csv.DictWriter(outfile, fieldnames=all_columns)

        # Записываем заголовки в новый файл
        csv_writer.writeheader()

        # Чтение и запись данных с добавлением новой колонки
        for i, row in enumerate(csv_reader):
            # Добавляем значение для новой колонки
            row[new_column] = check_string(row["Title 1"])  # Замените 'NewValue' на ваше значение
            # Записываем строку с новой колонкой в новый файл
            csv_writer.writerow({col: row.get(col, '') for col in all_columns})

    print(f"Отчет успешно создан в файле ")


if __name__ == "__main__":
    main()
