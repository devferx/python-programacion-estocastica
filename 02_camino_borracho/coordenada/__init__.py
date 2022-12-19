class Coordenada:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # Retorna una nueva coordenada con la suma de las coordenadas
    def mover(self, delta_x: int, delta_y: int):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    def distancia(self, otra_coordenada: "Coordenada") -> float:
        x_diff = (self.x - otra_coordenada.x) ** 2
        y_diff = (self.y - otra_coordenada.y) ** 2

        return (x_diff + y_diff) ** 0.5
