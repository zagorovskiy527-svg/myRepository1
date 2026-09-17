from models import Planet, Moon, Crater
from parsers import parse_file
from processing import (
    find_planets_in_area,
    filter_by_type,
    find_craters_by_planet,
)


def show_menu():
    print("1. Добавить планету")
    print("2. Вывести список планет")
    print("3 - Закрыть")

def input_planet():
    name = input("Название планеты: ").strip()
    date = input("Дата открытия: ").strip()
    radius = float(input("Радиус: "))
    x = float(input("Координата x: "))
    y = float(input("Координата y: "))
    return Planet(name, date, radius, x, y)

def print_planets(planets):
    if not planets:
        print("Список планет пуст.")
        return
    print(f"Всего планет: {len(planets)}")
    i = 1
    for planet in planets:
        print(f"{i}. {planet}")
        i = i + 1




def main():
    planets = []

    while True:
        show_menu()
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            planet = input_planet() 
            planets.append(planet)
            print(f"Планета '{planet.name}' добавлена.")

        elif choice == "2":
            print_planets(planets)

        elif choice == "3":
            print("Выход.")
            break

        else:
            print("Неверный пункт. Попробуйте снова.")
            

if __name__ == "__main__":
    main()