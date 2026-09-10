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


with open('input.txt', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        planet = parse_planet(line)
        print(planet)