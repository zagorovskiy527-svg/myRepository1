class Planet:
    def __init__(self, name, date, radius):
        self.name = name
        self.date = date
        self.radius = radius
    
    def __str__(self):
        return f"Планета: {self.name}, дата открытия: {self.date}, радиус: {self.radius}"


def parse_planet(text):
    start = text.find('"')
    end = text.find('"', start + 1)
    name = text[start + 1:end]
    
    rest = text[:start] + text[end + 1:]
    parts = rest.split()
    
    date = parts[1]
    radius = float(parts[2])
    
    return Planet(name, date, radius)

with open('input.txt') as file:
    for line in file:                
        line = line.strip()          
        if not line:                 
            continue
        planet = parse_planet(line)  
        print(planet)               