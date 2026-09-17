class SpaceObjects:
    def __init__ (self, name, date):
        self.name = name
        self.data = date

    def str (self):
        return f"{self.__class__.__name__}: {self.name}, дата {self.date}"


class Planet(SpaceObjects):
    def __init__(self, name, date, radius, x, y):
        super().__init__(name, date)
        self.radius = radius
        self.x = x          
        self.y = y          

    def __str__(self):
        return (f"Планета: {self.name}, дата открытия: {self.date}, "
                f"радиус: {self.radius}, координаты: ({self.x}, {self.y})")


class Moon(SpaceObjects):
    def __init__ (self, name, date, planet_name, distance):
        super().__init__(name, date)
        self.planet_name = planet_name
        self.distance = distance

    def str(self):
        return (f"Спутник: {self.name}, дата открытия: {self.date}, "
                f"планета: {self.planet_name}, расстояние: {self.distance}")


class Crater(SpaceObjects):
    def __init__(self, name, date, planet_name, diameter, depth):
            super().__init__(name, date)
            self.planet_name = planet_name
            self.diameter = diameter
            self.depth = depth

    def __str__(self):
        return (f"Кратер: {self.name}, дата: {self.date}, "
                f"планета: {self.planet_name}, "
                f"диаметр: {self.diameter}, глубина: {self.depth}")

    