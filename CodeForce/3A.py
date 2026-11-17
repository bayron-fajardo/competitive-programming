s = input().strip()
t = input().strip()

d = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8
}

punto_rey = [d.get(s[0], 0), int(s[-1])]
punto_rey_destino = [d.get(t[0], 0), int(t[-1])]


def calcular_distancia(punto_rey, punto_rey_destino):
    dx = abs(punto_rey_destino[0] - punto_rey[0])
    dy = abs(punto_rey_destino[1] - punto_rey[1])
    return max(dx, dy)


def movimiento_rey(punto_rey, punto_rey_destino):
    movimientos = []

    while punto_rey != punto_rey_destino:
        paso = ""

        if punto_rey[0] < punto_rey_destino[0]:
            paso += "R"
            punto_rey[0] += 1
        elif punto_rey[0] > punto_rey_destino[0]:
            paso += "L"
            punto_rey[0] -= 1

        if punto_rey[1] < punto_rey_destino[1]:
            paso += "U"
            punto_rey[1] += 1
        elif punto_rey[1] > punto_rey_destino[1]:
            paso += "D"
            punto_rey[1] -= 1

        movimientos.append(paso)

    return movimientos


def mostrar_movimientos(movimientos):
    for movimiento in movimientos:
        print(movimiento)


distancia = calcular_distancia(punto_rey, punto_rey_destino)
print(distancia)
movimientos = movimiento_rey(punto_rey, punto_rey_destino)
mostrar_movimientos(movimientos)