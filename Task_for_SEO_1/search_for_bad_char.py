import csv
import sys
import os

eng_alph = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
rus_alph = {'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
            'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'}
RUS = "рус"
ENG = "eng"

def check_string(s: str) -> dict:
    # Добавляем номер элемента, что бы считалось с единицы, а не с нуля.
    add_ind = 1
    bad_ind = dict()
    for i in range(1, len(s)):
        if (s[i - 1] in eng_alph and s[i] in rus_alph) or (s[i - 1] in rus_alph and s[i] in eng_alph):
            bad_ind[i] = s[i - 1], RUS if ord(s[i - 1]) > 500 else ENG
            bad_ind[i + add_ind] = s[i], RUS if ord(s[i]) > 500 else ENG
    return bad_ind


def main():
    # Проверка на наличие трех аргументов (пути к файлам)
    if len(sys.argv) != 2:
        print("Usage: python3 search_for_bad_char.py <file.csv>")
        return

    # Указываем путь к исходному файлу CSV
    input_file_path = sys.argv[1]

    # Указываем путь для нового файла добавляя формат CSV
    output_file_path = input("Введите имя для нового файла: ") + ".csv"
    # Директория для результатов.
    res_dir = "./results/"
    # Первичное чтения файла для уточнения наименования колонок.
    with open(input_file_path, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        titles = {i:j for i, j in enumerate(next(reader))}

    # Чтение данных из исходного файла и запись в новый CSV файл
    with (open(input_file_path, mode='r', encoding='utf-8') as infile,
          open(res_dir + output_file_path, mode='w', encoding='utf-8',newline='') as outfile):

        # Чтение CSV файла как словаря
        csv_reader = csv.DictReader(infile)
        # Демонстрация пользователю выбора возможных колонок.
        print()
        print(*[f"{m} - {n}" for m, n in titles.items()], sep="\n")
        print()
        # Указываем исходные колонки и добавляем новую колонку
        columns_to_read = titles[int(input("Введите номер колонки: "))]  # Замените на нужные вам колонки

        new_column = 'Опечатки'  # Название новой колонки
        total_column = "Места опечаток"  # Нумерация строк с опечатками.
        all_columns = [total_column] + [columns_to_read]  + [new_column]

        # Создаем объект для записи CSV файла с новой колонкой
        csv_writer = csv.DictWriter(outfile, fieldnames=all_columns)

        # Записываем заголовки в новый файл
        csv_writer.writeheader()

        # Чтение и запись данных с добавлением новой колонки
        for i, row in enumerate(csv_reader):
            # Добавляем значение для новой колонки
            row[new_column] = check_string(row[columns_to_read])  # Замените 'NewValue' на ваше значение
            if row[new_column]:
                row[total_column] = i + 2
                # Записываем строку с новой колонкой в новый файл
                csv_writer.writerow({col: row.get(col, '') for col in all_columns})

    print(f"Отчет {output_file_path} успешно создан в папке {res_dir}")


if __name__ == "__main__":
    main()
