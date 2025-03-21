#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Dmitriy Aldunin @DMcraft
# Created Date: 16/03/2025
# version ='1.0'
# Copyright 2025 Dmitriy Aldunin
# Licensed under the MIT License
# ---------------------------------------------------------------------------

import re
import argparse
import sys


# Функция для обработки текста
def process_text(text):
    # Регулярное выражение для поиска строк в кавычках
    pattern = r"'(.*?)'"

    # Функция для замены строк
    def replace_long_string(match):
        string = match.group(1)
        utf8_bytes = string.encode('windows-1251')
        try:
            windows_1251_string = utf8_bytes.decode('utf-8')
        except UnicodeDecodeError:
            windows_1251_string = string
        except Exception as e:
            print(f'Ошибка выполнения {e}')
            sys.exit(1)

        return f"'{windows_1251_string}'"

    # Заменяем строки в кавычках согласно условию
    processed_text = re.sub(pattern, replace_long_string, text)
    return processed_text


def convert_encoding(input_file, output_file):
    # Чтение исходного файла
    with open(input_file, 'r') as file:
        text = file.read()

    # Обработка текста
    processed_text = process_text(text)

    # Запись результата в новый файл
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(processed_text)

    print(f"Файл успешно перекодирован и сохранён как {output_file}")


def main():
    # Настройка парсера аргументов командной строки
    parser = argparse.ArgumentParser(description="Перекодировка дампа SQL со смешенными кодировками.")
    parser.add_argument('input_file', help="Имя входного файла")
    parser.add_argument('output_file', help="Имя выходного файла")
    args = parser.parse_args()

    # Вызов функции перекодировки
    convert_encoding(args.input_file, args.output_file)

if __name__ == "__main__":
    main()