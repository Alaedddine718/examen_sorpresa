from punto import Punto
from rectangulo import Rectangulo

if __name__ == "__main__":
    A = Punto(2, 3)
    B = Punto(5, 5)
    C = Punto(-3, -1)
    D = Punto(0, 0)

    print("Puntos:")
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")
    print(f"D: {D}")

    print("\nCuadrantes:")
    print(f"A pertenece al {A.cuadrante()}")
    print(f"B pertenece al {B.cuadrante()}")
    print(f"C pertenece al {C.cuadrante()}")
    print(f"D pertenece al {D.cuadrante()}")

    print("\nVectores:")
    print(f"Vector AB: {A.vector(B)}")
    print(f"Vector BA: {B.vector(A)}")

    print("\nDistancias:")
    print(f"Distancia entre A y B: {A.distancia(B)}")
    print(f"Distancia entre B y A: {B.distancia(A)}")

    distancias = {
        "A": A.distancia(D),
        "B": B.distancia(D),
        "C": C.distancia(D)
    }
    punto_mas_lejano = max(distancias, key=distancias.get)
    print(f"\nEl punto más lejano del origen es: {punto_mas_lejano}")

    rectangulo = Rectangulo(A, B)

    print("\nRectángulo:")
    print(f"Base: {rectangulo.base()}")
    print(f"Altura: {rectangulo.altura()}")
    print(f"Área: {rectangulo.area()}")