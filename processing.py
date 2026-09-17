
def planet_in(planet, x_min, y_min, x_max, y_max):
    p_left   = planet.x - planet.radius 
    p_right  = planet.x + planet.radius 
    p_bottom = planet.y - planet.radius 
    p_top    = planet.y + planet.radius

    if p_right < x_min:
        return False
    if p_left > x_max:
        return False
    if p_top < y_min:
        return False
    if p_bottom > y_max:
        return False

    return True


def find_planets_in_area(planets, x_min, y_min, x_max, y_max):
    result = []
    for planet in planets:
        if planet_in(planet, x_min, y_min, x_max, y_max):
            result.append(planet)
    return result


def filter_by_type(objects, cls):
    result = []
    for obj in objects:
        if isinstance(obj, cls):
            result.append(obj)
    return result


def find_craters_by_planet(craters, planet_name):
    result = []
    for crater in craters:
        if crater.planet_name == planet_name:
            result.append(crater)
    return result