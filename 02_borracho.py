import random


# Clase base para los borrachos
class Borracho:
    def __init__(self, nombre):
        self.nombre = nombre


# Subclase de Borracho
class BorrachoTradicional(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)

    # Retorna una tupla con la dirección en la que se moverá
    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
