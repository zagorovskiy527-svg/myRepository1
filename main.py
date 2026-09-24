# Главный модуль программы.

from datetime import datetime

from models import Planet
from parsers import parse_file
from processing import filter_by_type


PLANETS_FILE = "planets.txt"


def show_menu():
    print()
    print("МЕНЮ")
    print("1. Добавить планету")
    print("2. Вывести список планет")
    print("3. Закрыть")


def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка: строка не может быть пустой.")


def input_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value.replace(",", "."))
        except ValueError:
            print("Ошибка: нужно ввести число.")


def input_date(prompt):
    while True:
        value = input(prompt).strip()
        try:
            datetime.strptime(value, "%Y.%m.%d")
            return value
        except ValueError:
            print("Ошибка: дата должна быть в формате гггг.мм.дд.")


def input_choice():
    while True:
        value = input("Выберите пункт: ").strip()
        if value in ("1", "2", "3"):
            return value
        print("Неверный пункт. Введите 1, 2 или 3.")


def input_planet():
    name = input_non_empty("Название планеты: ")
    date = input_date("Дата открытия (гггг.мм.дд): ")
    radius = input_float("Радиус: ")
    x = input_float("Координата x: ")
    y = input_float("Координата y: ")
    return Planet(name, date, radius, x, y)


def print_planets(planets):
    if not planets:
        print("\nСписок планет пуст.")
        return
    print(f"\nВсего планет: {len(planets)}")
    print("-" * 60)
    i = 1
    for planet in planets:
        print(f"{i}. {planet}")
        i += 1
    print("-" * 60)


def find_planet_by_name(planets, name):
    for planet in planets:
        if planet.name.lower() == name.lower():
            return planet
    return None


def save_planet_to_file(planet, filename):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f'planet {planet.name} "{planet.name}" {planet.date} '
                   f'{planet.radius} {planet.x} {planet.y}\n')


def add_planet(added_planets, filename):
    planet = input_planet()

    existing = find_planet_by_name(added_planets, planet.name)
    if existing is not None:
        print(f"\nПланета '{planet.name}' уже есть в списке добавленных!")
        print(f"Существующая запись: {existing}")
        print("Добавление отменено.")
        return

    added_planets.append(planet)
    save_planet_to_file(planet, filename)
    print(f"\nПланета '{planet.name}' добавлена.")


def main():
    objects, errors = parse_file("input.txt", encoding="utf-8")

    if errors:
        print("Ошибки при чтении input.txt:")
        for e in errors:
            print(f"  - {e}")

    planets = filter_by_type(objects, Planet)

    added_objects, added_errors = parse_file(PLANETS_FILE, encoding="utf-8")
    if added_errors:
        print("Ошибки при чтении planets.txt:")
        for e in added_errors:
            print(f"  - {e}")

    added_planets = filter_by_type(added_objects, Planet)

    while True:
        show_menu()
        choice = input_choice()

        if choice == "1":
            add_planet(added_planets, PLANETS_FILE)

        elif choice == "2":
            all_planets = planets + added_planets
            print_planets(all_planets)

        elif choice == "3":
            print("Выход.")
            break


if __name__ == "__main__":
    main()