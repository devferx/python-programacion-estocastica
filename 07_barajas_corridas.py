import random

PALOS = ["espada", "corazon", "rombo", "trebol"]
VALORES = ["as", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jota", "reina", "rey"]


def crear_baraja():
    return [(palo, valor) for palo in PALOS for valor in VALORES]


def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    return mano


def escalera_color(tamano_mano, intentos):
    # Creamos una baraja de cartas
    cartas = crear_baraja()

    # Creamos tantas manos como nos indicó el usuario
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(cartas, tamano_mano)
        manos.append(mano)

    escaleras = 0
    for mano in manos:
        # Creamos una lista con todos los palos de la mano
        palos = [carta[0] for carta in mano]
        valores = []
        # Creamos un conjunto para eliminar los elementos repetidos, y preguntamos si la
        # longitud de este conjunto es igual a 1 (es decir, todas las cartas son del mismo palo)
        if len(set(palos)) == 1:
            for carta in mano:
                # Convertimos las cartas a listas, para poder manipularlas
                carta = list(carta)

                # Convertimos las letras a números, para evaluar posteriormente la escalera de color
                if carta[1] == "A":
                    carta[1] = "1"
                if carta[1] == "J":
                    carta[1] = "11"
                if carta[1] == "Q":
                    carta[1] = "12"
                if carta[1] == "K":
                    carta[1] = "13"
                # Transformamos los valores en str a int, para facilitar la comparación posterior
                carta[1] = int(carta[1])

                valores.append(carta[1])

            # Ordenamos los valores
            valores.sort()

            es_escalera = True
            # Comprobamos que todos los valores sean consecutivos
            for i, valor in enumerate(valores):
                if i != 0:
                    if valor - valores[i - 1] != 1:
                        es_escalera = False
                        break

            # Si todo se cumplió, sumamos uno al contador de escaleras
            if es_escalera:
                escaleras += 1

    print(f"Escaleras: {escaleras}")
    probabilidad_de_encontrar_escalera = (escaleras / intentos) * 100
    print(
        f"La probabilidad de encontrar una escalera de color en una mano de {tamano_mano} cartas es de {probabilidad_de_encontrar_escalera}%"
    )


if __name__ == "__main__":
    tamano_mano = int(input("De cuantas barajas sera la mano: "))
    intentos = int(input("Cuantos intentos para calcular la probabilidad: "))

    escalera_color(tamano_mano, intentos)
