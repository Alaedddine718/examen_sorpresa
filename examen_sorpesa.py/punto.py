import math

class Punto:
    def _init_(self, x=0, y=0):
        self.x = x
        self.y = y

    def _str_(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Origen"
        elif self.x == 0:
            return "Eje Y"
        elif self.y == 0:
            return "Eje X"
        elif self.x > 0 and self.y > 0:
            return "Cuadrante 1"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante 2"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante 3"
        else:
            return "Cuadrante 4"

    def vector(self, p):
        return f"({p.x - self.x}, {p.y - self.y})"

    def distancia(self, p):
        return math.sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)