from typing import List
from borracho import BorrachoTradicional, Borracho
from campo import Campo
from coordenada import Coordenada


def caminata(campo: Campo, borracho: Borracho, pasos: int):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminita(
    pasos: int,
    numero_de_intentos: int,
    tipo_de_borracho: Borracho,
) -> List[int]:
    borracho = tipo_de_borracho(nombre="David")
    origen = Coordenada(0, 0)
    distancias: List[int] = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simular_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simular_caminata, 1))

    return distancias


def main(
    distancias_de_caminata: List[int],
    numero_de_intentos: int,
    tipo_de_borracho: Borracho,
):
    for pasos in distancias_de_caminata:
        distancias = simular_caminita(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)

        print(f"{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos")
        print(f"Media = {distancia_media}")
        print(f"Máxima = {distancia_maxima}")
        print(f"Mínima = {distancia_minima}")


if __name__ == "__main__":
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)
