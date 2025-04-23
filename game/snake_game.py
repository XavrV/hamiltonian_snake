import random
from typing import List, Tuple
from dataclasses import dataclass
from common.point import Point


# Acciones: [straight, right, left] para compatibilidad con RL y lógica futura
Action = List[int]


class SnakeGame:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.direction = "RIGHT"
        self.head = Point(0, 0)  # ← Alineado con inicio del ciclo
        self.body = [self.head]
        self.score = 0
        self._place_food()
        self.frame_iteration = 0

    def _place_food(self):
        while True:
            food = Point(
                random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            )
            if food not in self.body:
                self.food = food
                break

    def get_head(self) -> Point:
        return self.head

    def get_food(self) -> Point:
        return self.food

    def get_snake_body(self) -> List[Point]:
        return list(self.body)  # copia superficial

    def direction_to(self, target: Point) -> Action:
        dx = target.x - self.head.x
        dy = target.y - self.head.y
        if dx == 1:
            return [1, 0, 0]  # derecha
        if dx == -1:
            return [0, 1, 0]  # izquierda
        if dy == -1:
            return [0, 0, 1]  # arriba
        if dy == 1:
            return [0, 0, 1]  # abajo
        return [1, 0, 0]  # por defecto

    def play_step(self, action: Action) -> Tuple[int, bool, int]:
        self.frame_iteration += 1
        self._move(action)
        self.body.insert(0, self.head)

        reward = 0
        game_over = False

        if self._is_collision():
            game_over = True
            reward = -10
            return reward, game_over, self.score

        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.body.pop()

        return reward, game_over, self.score

    def _move(self, action: Action):
        directions = ["RIGHT", "DOWN", "LEFT", "UP"]
        idx = directions.index(self.direction)

        if action == [1, 0, 0]:  # recto
            new_dir = directions[idx]
        elif action == [0, 1, 0]:  # derecha
            new_dir = directions[(idx + 1) % 4]
        else:  # izquierda
            new_dir = directions[(idx - 1) % 4]

        self.direction = new_dir
        x, y = self.head.x, self.head.y
        if self.direction == "RIGHT":
            x += 1
        elif self.direction == "LEFT":
            x -= 1
        elif self.direction == "UP":
            y -= 1
        elif self.direction == "DOWN":
            y += 1

        self.head = Point(x, y)

    def _is_collision(self, pt=None) -> bool:
        if pt is None:
            pt = self.head
        # Bordes
        if pt.x < 0 or pt.x >= self.width or pt.y < 0 or pt.y >= self.height:
            return True
        # Contra sí misma
        if pt in self.body[1:]:
            return True
        return False
