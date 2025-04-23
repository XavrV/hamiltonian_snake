from common.point import Point

from logic.hamiltonian import HamiltonianCycle
from logic.astar import a_star
from logic.safety import is_path_safe

from typing import Optional, List, Set


class HybridAgent:
    def __init__(self, game: SnakeGame):
        self.game = game
        self.cycle = HamiltonianCycle(game.width, game.height)

    def get_action(self) -> List[int]:
        head = self.game.get_head()
        food = self.game.get_food()
        body = self.game.get_snake_body()

        # Obstáculos = cuerpo (excepto cabeza)
        obstacles: Set[Point] = set(body[1:])

        # 1. Intentar camino A*
        path = a_star(head, food, self.game.width, self.game.height, obstacles)
        if path and is_path_safe(path, body, future_growth=1):
            next_point = path[1]  # [0] es la cabeza
            print("🚀 Usando ATAJO A*")
        else:
            # 2. Seguir ciclo Hamiltoniano
            next_point = self.cycle.next_from(head)
            print("🔄 Usando CICLO HAMILTONIANO")

        return self.game.direction_to(next_point)
