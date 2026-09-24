# Разбор строк в объекты с обработкой ошибок.

from datetime import datetime

from models import Planet, Moon, Crater
from errors import ParseError


class Parser:

    def __init__(self):
        self.parsers = {
            "planet": self.parse_planet,
            "планета": self.parse_planet,
            "moon": self.parse_moon,
            "луна": self.parse_moon,
            "спутник": self.parse_moon,
            "crater": self.parse_crater,
            "кратер": self.parse_crater,
}

    def extract_quoted(self, text):
        start = text.find('"')
        if start == -1:
            raise ParseError("нет значения в кавычках")
        end = text.find('"', start + 1)
        if end == -1:
            raise ParseError("не закрыта кавычка")

        quoted = text[start + 1:end]
        if not quoted:
            raise ParseError("пустое значение в кавычках")

        rest = (text[:start] + text[end + 1:]).split()
        return quoted, rest

    def to_float(self, text):
        try:
            return float(text)
        except ValueError:
            raise ParseError(f"'{text}' — не число")

    def to_date(self, text):
        # Проверяет формат даты гггг.мм.дд.
        try:
            datetime.strptime(text, "%Y.%m.%d")
        except ValueError:
            raise ParseError(f"'{text}' — не дата в формате гггг.мм.дд")
        return text

    def parse_planet(self, text):
        name, parts = self.extract_quoted(text)
        if len(parts) < 5:
            raise ParseError(f"для планеты нужно 5 значений, получено {len(parts)}")
        date = self.to_date(parts[1])
        radius = self.to_float(parts[2])
        x = self.to_float(parts[3])
        y = self.to_float(parts[4])
        return Planet(name, date, radius, x, y)

    def parse_moon(self, text):
        name, parts = self.extract_quoted(text)
        if len(parts) < 4:
            raise ParseError(f"для спутника нужно 4 значения, получено {len(parts)}")
        planet_name = parts[2].strip('"')
        date = self.to_date(parts[1])
        distance = self.to_float(parts[3])
        return Moon(name, date, planet_name, distance)

    def parse_crater(self, text):
        # 'Гершель "Гершель" 2024.03.12 "Марс" 120.5 3.2'
        name, parts = self.extract_quoted(text)
        if len(parts) < 5:
            raise ParseError(f"для кратера нужно 5 значений, получено {len(parts)}")
        planet_name = parts[2].strip('"')
        date = self.to_date(parts[1])
        diameter = self.to_float(parts[3])
        depth = self.to_float(parts[4])
        return Crater(name, date, planet_name, diameter, depth)

    def parse_line(self, text):
        parts = text.split(" ", 1)
        if len(parts) < 2:
            raise ParseError(f"строка без описания: '{text}'")

        obj_type, body = parts
        obj_type = obj_type.lower()

        parser = self.parsers.get(obj_type)
        if parser is None:
            raise ParseError(f"неизвестный тип объекта: '{obj_type}'")

        return parser(body)


def parse_file(filename, encoding="utf-8"):
    parser = Parser()
    objects = []
    errors = []

    try:
        with open(filename, encoding=encoding) as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    objects.append(parser.parse_line(line))
                except ParseError as e:
                    errors.append(f"Строка {line_number}: {e}")
    except FileNotFoundError:
        errors.append(f"Файл '{filename}' не найден")
    except UnicodeDecodeError:
        errors.append(f"Не удалось прочитать файл '{filename}' "
                      f"в кодировке {encoding}")

    return objects, errors