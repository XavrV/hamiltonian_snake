from typing import List, Optional, Set, Dict, Tuple
import heapq
from common.point import Point


def manhattan(a: Point, b: Point) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


def a_star(
    start: Point, goal: Point, width: int, height: int, obstacles: Set[Point]
) -> Optional[List[Point]]:
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from: Dict[Point, Point] = {}
    g_score: Dict[Point, int] = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current, width, height, obstacles):
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + manhattan(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    return None  # No path found


def get_neighbors(
    point: Point, width: int, height: int, obstacles: Set[Point]
) -> List[Point]:
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dx, dy in moves:
        nx, ny = point.x + dx, point.y + dy
        neighbor = Point(nx, ny)
        if 0 <= nx < width and 0 <= ny < height and neighbor not in obstacles:
            neighbors.append(neighbor)
    return neighbors


def reconstruct_path(came_from: Dict[Point, Point], current: Point) -> List[Point]:
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
