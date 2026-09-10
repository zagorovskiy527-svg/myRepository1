class Planet:
    def __init__(self, name, date, radius, x, y):
        self.name = name
        self.date = date
        self.radius = radius
        self.x = x          
        self.y = y          
    
    def __str__(self):
        return (f"Планета: {self.name}, дата открытия: {self.date}, "
                f"радиус: {self.radius}, координаты: ({self.x}, {self.y})")


def parse_planet(text):
    start = text.find('"')
    end = text.find('"', start + 1)
    name = text[start + 1:end]
    
    rest = text[:start] + text[end + 1:]
    parts = rest.split()
    
    date = parts[1]
    radius = float(parts[2])
    x = float(parts[3])     
    y = float(parts[4])    
    
    return Planet(name, date, radius, x, y)


planets = []
with open('input.txt', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        planets.append(parse_planet(line))

def in_figure(planet, x_min, y_min, x_max, y_max):
    if planet.x < x_min or planet.x > x_max:
        return False
    if planet.y < y_min or planet.y > y_max:
        return False
    return True

def planets_in_figure(planets, x_min, y_min, x_max, y_max):
    result = []
    for planet in planets:
        if in_figure(planet, x_min, y_min, x_max, y_max):
            result.append(planet)
    return result

x_min, y_min = 0.0, 0.0
x_max, y_max = 50.0, 30.0

found = planets_in_figure(planets, x_min, y_min, x_max, y_max)

print(f"Область: ({x_min}, {y_min}) — ({x_max}, {y_max})")
print(f"Найдено планет: {len(found)}")
print(f'Всего планет: {len(planets)}')
for p in found:
    print(p)