import math


def euclidean(a, b) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def _min_puntaje_node(cola):
    mejor_indice = 0
    mejor_puntaje = cola[0][0]
    for i in range(1, len(cola)):
        if cola[i][0] < mejor_puntaje:
            mejor_puntaje = cola[i][0]
            mejor_indice = i
    return cola.pop(mejor_indice)


class AStarPathFinder:
    _DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(
            self,
            grid,
            start = (0, 0),
            end = None
    ):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.end = end or (self.rows - 1, self.cols - 1)

    def _neighbors(self, node):
        x, y = node
        for dx, dy in self._DIRS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                if (self.grid[nx][ny] == 0) or ((nx, ny) == self.end):
                    yield nx, ny

    def find_path(self):
        cola_abierta = [(0.0, self.start)]

        padre: dict = {}
        costo_g: dict = {self.start: 0.0}
        costo_f: dict = {self.start: euclidean(self.start, self.end)}

        while cola_abierta:
            f_actual, actual = _min_puntaje_node(cola_abierta)

            if actual == self.end:
                camino = [actual]
                while actual in padre:
                    actual = padre[actual]
                    camino.append(actual)
                return list(reversed(camino))

            for vecino in self._neighbors(actual):
                costo_temporal = costo_g[actual] + 1.0
                if costo_temporal < costo_g.get(vecino, math.inf):
                    padre[vecino] = actual
                    costo_g[vecino] = costo_temporal
                    costo_f[vecino] = costo_temporal + euclidean(vecino, self.end)

                    # Actualizar o agregar el vecino en la cola
                    encontrado = False
                    for i in range(len(cola_abierta)):
                        if cola_abierta[i][1] == vecino:
                            cola_abierta[i] = (costo_f[vecino], vecino)
                            encontrado = True
                            break
                    if not encontrado:
                        cola_abierta.append((costo_f[vecino], vecino))

        return None