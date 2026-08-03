def score(x, y):
    distancia = (x**2 + y**2)**0.5

    if distancia <= 1:
        puntuacion = 10
    elif distancia <= 5:
        puntuacion = 5
    elif distancia <= 10:
        puntuacion = 1
    else:
        puntuacion = 0

    return puntuacion
