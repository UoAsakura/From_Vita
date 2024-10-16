
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

error_sign = "❗️"
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


# Функция для прочтения файла и создания нового.
def calc_column(name_headers: list[str], data_csv: DataFrame):
    number_column = "Места опечаток"  # Нумерация строк с опечатками.
    place_in_column = 'Опечатки'  # Название новой колонки
    data = {number_column: [],
            name_headers[0]: [],
            place_in_column: []}
    # Чтение и запись данных с добавлением новой колонки
    for i, row in enumerate(data_csv[name_headers[0]], start=2):
        if not isinstance(row, str): # Проверка на не пустую строку.
            continue
        var = check_string(row) # Словарь с ошибками.
        if var: # Если словарь не пустой, то начинаем цикл по генерации новой строки с подстветкой мест ошибок.
            new_string = "" # Создаём новую строку с подсветкой неточностей.
            flag = True
            for j in range(len(row)):
                if flag == True:
                    if j + 1 in var:
                        new_string += error_sign + row[j:j + 2] + error_sign
                        flag = False
                    else:
                        new_string += row[j]
                else:
                    flag = True
            row = new_string
            data[number_column].append(int(i))
            data[name_headers[0]].append(row)
            data[place_in_column].append(var)

    df = pd.DataFrame(data)
    return df