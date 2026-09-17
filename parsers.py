from models import Planet, Moon, Crater


def extract_quoted(text):
    start = text.find('"')
    end = text.find('"', start + 1)
    quoted = text[start + 1:end]
    rest = (text[:start] + text[end + 1:]).split()
    return quoted, rest


def parse_planet(text):
    name, parts = extract_quoted(text)
    return Planet(name, parts[1], float(parts[2]),
                  float(parts[3]), float(parts[4]))


def parse_moon(text):
    name, parts = extract_quoted(text)
    planet_name = parts[2].strip('"')
    return Moon(name, parts[1], planet_name, float(parts[3]))


def parse_crater(text):
    name, parts = extract_quoted(text)
    planet_name = parts[2].strip('"')
    return Crater(name, parts[1], planet_name,
                  float(parts[3]), float(parts[4]))


PARSERS = {
    "планета": parse_planet,
    "луна": parse_moon,
    "кратер": parse_crater,
}


def parse_line(text):
    parts = text.split(" ", 1)

    obj_type = parts[0]
    body = parts[1]

    obj_type = obj_type.lower()

    if obj_type == "planet":
        return parse_planet(body)
    elif obj_type == "moon":
        return parse_moon(body)
    elif obj_type == "crater":
        return parse_crater(body)
    else:
        raise ValueError(f"Неизвестный тип объекта: {obj_type}")


def parse_file(filename, encoding="utf-8"):
    objects = []
    with open(filename, encoding=encoding) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            objects.append(parse_line(line))
    return objects