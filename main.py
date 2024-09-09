# This is a sample Python script.
import math


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def get_r(x, y):
    return (x ** 2 + y ** 2) ** 0.5

def get_r_sphere(x, y,z):
    return (x ** 2 + y ** 2 + z**2) ** 0.5

def get_arccos(x, y):
    return math.acos(x/y)

def get_omega(x, y):
    return math.atan2(y, x)

def from_decart_to_polar(x, y, symbols_to_point):
    try:
        return (round(get_r(x, y),symbols_to_point), round(get_omega(x, y), symbols_to_point))
    except:
        return "Invalid input"

#r - радиус вектор omega - угол между положительным направлением оси x и радиусом-вектором r
def from_polar_to_decart(r, omega, symbols_to_point):
    try:
        x = r * math.cos(omega)
        y = r * math.sin(omega)
        return (round(x, symbols_to_point),round(y, symbols_to_point))
    except:
        return "Invalid input"

def from_decart_to_cylinder(x, y, z, symbols_to_point):
    try:
        r = get_r(x, y)
        omega = get_omega(x, y)
        return (round(r, symbols_to_point), round(math.degrees(omega), symbols_to_point), z)
    except:
        return "Invalid input"
#r - радиус вектор omega - угол между положительным направлением оси x и радиусом-вектором r
def from_cylinder_to_decart(r, omega, z, symbols_to_point):
    try:
        x = r * math.cos(omega)
        y = r * math.sin(omega)
        return (round(x, symbols_to_point),round(y, symbols_to_point),round(z,symbols_to_point))
    except:
        return "Invalid input"

def from_decart_to_sphere(x, y, z, symbols_to_point):
    try:
        r = math.sqrt(x ** 2 + y ** 2 + z ** 2)

        theta = math.acos(z / r) if r != 0 else 0

        phi = math.atan2(y, x)

        return round(r, symbols_to_point), round(theta, symbols_to_point), round(phi,symbols_to_point)
    except:
        return "Invalid input"

#r - радиус вектор omega - угол между положительным направлением оси x и радиусом-вектором r, psi - азимутальный угол (угол между осью x и проекцией вектора на плоскость xy
def from_sphere_to_decart(r, omega, psi, symbols_to_point):
    try:
        x = r * math.sin(omega)*math.cos(psi)
        y = r * math.sin(psi)*math.sin(omega)
        z = r * math.cos(omega)
        return (round(x, symbols_to_point),round(y, symbols_to_point), round(z, symbols_to_point))
    except:
        return "Invalid input"




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x, y, z = map(float, input().split())
    print(from_decart_to_sphere(x, y, z))
    r, omega, z = from_decart_to_sphere(x, y, z)
    print(from_sphere_to_decart(r, omega, z))
