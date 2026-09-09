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


text = 'Земля "Земля" 2024.01.15 6371.0'
planet = parse_planet(text)
print(planet)