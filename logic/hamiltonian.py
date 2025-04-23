from typing import List, Dict
from common.point import Point


def generate(width: int, height: int) -> List[Point]:
    """
    Genera un ciclo Hamiltoniano en orden serpenteante.
    Solo válido si al menos uno de los lados es par.
    """
    if width % 2 == 1 and height % 2 == 1:
        raise ValueError(
            "Imposible generar ciclo Hamiltoniano si ambos lados son impares."
        )

    path = []
    for y in range(height):
        row = [Point(x, y) for x in range(width)]
        if y % 2 == 1:
            row.reverse()
        path.extend(row)

    return path


def make_lookup(path: List[Point]) -> Dict[Point, Point]:
    """
    Crea un diccionario de acceso rápido: Point → siguiente Point en el ciclo.
    """
    return {p: path[(i + 1) % len(path)] for i, p in enumerate(path)}


class HamiltonianCycle:
    def __init__(self, width: int, height: int):
        self.path = generate(width, height)
        self.lookup = make_lookup(self.path)

    def next_from(self, current: Point) -> Point:
        """
        Retorna el siguiente punto en el ciclo desde el actual.
        """
        return self.lookup[current]
