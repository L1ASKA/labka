import re


def number_to_words(number):
    """
    Преобразует целую часть числа в строку, где каждая цифра представлена прописью.
    """
    digit_to_word = {
        '0': 'ноль',
        '1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'четыре',
        '5': 'пять',
        '6': 'шесть',
        '7': 'семь',
        '8': 'восемь',
        '9': 'девять'
    }
    return ' '.join(digit_to_word[digit] for digit in number)


def process_file(filename):
    """
    Читает файл, распознает объекты и преобразует их в соответствии с правилом.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Разделение объектов по пробелам
        objects = content.split()

        result = []

        for obj in objects:
            # Проверка, является ли объект вещественным числом в кавычках
            match = re.fullmatch(r'"(\d+)\.(\d+)"|\'(\d+)\.(\d+)\'', obj)
            if match:
                integer_part = match.group(1) or match.group(3)  # Целая часть числа
                # Преобразование целой части числа в слова
                result.append(number_to_words(integer_part))
            else:
                # Оставляем текстовые объекты без изменений
                result.append(obj)

        # Вывод результата
        print(' '.join(result))

    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    filename = "laba 4.txt"
    process_file(filename)
