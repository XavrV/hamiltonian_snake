from typing import List
from collections import deque
from common.point import Point


def is_path_safe(path: List[Point], body: List[Point], future_growth: int = 1) -> bool:
    """
    Simula paso a paso el recorrido de la serpiente sobre `path`
    y verifica si colisionaría consigo misma.
    """
    if not path or path[0] != body[0]:
        raise ValueError("El path debe comenzar en la cabeza actual de la serpiente.")

    sim_body = deque(body)

    for i, next_pos in enumerate(path[1:], start=1):
        sim_body.appendleft(next_pos)

        # Simula crecimiento solo si hay comida en el paso actual
        if i > future_growth:
            sim_body.pop()

        if next_pos in list(sim_body)[1:]:
            return False

    return True
