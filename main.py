from models import Planet, Moon, Crater
from parsers import parse_file
from processing import (
    find_planets_in_area,
    filter_by_type,
    find_craters_by_planet,
)


def main():
    objects = parse_file("input.txt", encoding="utf-8")

    planets = filter_by_type(objects, Planet)
    moons = filter_by_type(objects, Moon)
    craters = filter_by_type(objects, Crater)

    print(f"Всего объектов: {len(objects)}")
    print(f"Планет: {len(planets)}, спутников: {len(moons)}, кратеров: {len(craters)}")
    print("-" * 60)

    x_min, y_min = 0.0, 0.0
    x_max, y_max = 50.0, 30.0
    found = find_planets_in_area(planets, x_min, y_min, x_max, y_max)

    print(f"Область: ({x_min}, {y_min}) — ({x_max}, {y_max})")
    print(f"Планет в области: {len(found)}")
    for p in found:
        print(p)
    print("-" * 60)

    mars_craters = find_craters_by_planet(craters, "Марс")
    print(f"Кратеров на Марсе: {len(mars_craters)}")
    for c in mars_craters:
        print(c)
    print("-" * 60)

    print("Все объекты:")
    for obj in objects:
        print(obj)


if __name__ == "__main__":
    main()