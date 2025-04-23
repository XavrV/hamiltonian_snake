# 🐍 Snake AI - Agente Híbrido con Ciclo Hamiltoniano + A*

Este proyecto implementa un agente autónomo para el clásico juego de Snake, capaz de recorrer el tablero de forma segura usando un **ciclo Hamiltoniano** y tomar **atajos estratégicos con A\*** hacia la comida cuando sea viable y seguro hacerlo.

---

## 🎯 Objetivo del sistema

> Crear una serpiente inteligente, segura y eficiente, que combine:
>
> - Navegación basada en ciclo Hamiltoniano para **cobertura total sin colisión**.
> - Atajos hacia la comida usando **algoritmo A*** con verificación de **seguridad futura**.
> - Modularidad y extensibilidad para futuras mejoras o reemplazo de componentes.

---

## 🧩 Componentes del sistema

### 1. `snake_game.py`
Simula el entorno clásico de Snake.

#### Métodos clave:
- `get_head()` → retorna `Point(x, y)` con la posición de la cabeza.
- `get_food()` → retorna la posición actual de la comida.
- `get_snake_body()` → devuelve lista de segmentos `Point(x, y)` del cuerpo.
- `direction_to(Point)` → traduce un destino a una acción `[1, 0, 0]`, `[0, 1, 0]`, etc.
- `play_step(action)` → ejecuta una acción en el entorno.

### 2. `hamiltonian.py`
Genera y gestiona un **ciclo Hamiltoniano fijo** para un tablero rectangular.

#### Métodos:
- `generate(width, height)` → genera el camino completo como lista ordenada de `Point`.
- `next_from(current: Point)` → devuelve el siguiente punto en el ciclo.


### 3. `astar.py`
Algoritmo A* adaptado para el entorno Snake (rejilla 2D + obstáculos móviles).

#### Función principal:
- `a_star(start, goal, width, height, obstacles) → List[Point] | None`

Internamente usa `heapq` con desempate estable para evitar errores de ordenamiento.


### 4. `safety.py`
Simulador que evalúa si un camino es seguro de seguir.

#### Método:
- `is_path_safe(path: List[Point], body: List[Point], future_growth=1)`

Simula paso a paso el avance de la serpiente sobre el `path` y verifica si colisionaría con su propio cuerpo en el proceso.


### 5. `agent.py`
Contiene el `HybridAgent`, el cerebro de la IA.

#### Estrategia:
1. Intenta encontrar un camino A* hacia la comida.
2. Si el camino existe y es seguro según `is_path_safe` → se toma (imprime "Usando ATAJO A*").
3. Si no → se sigue el siguiente punto del ciclo Hamiltoniano ("Usando CICLO HAMILTONIANO").

---

## 🔁 Flujo de ejecución

1. Inicia el entorno con `SnakeGame()`.
2. En cada iteración:
   - El agente analiza el entorno.
   - Decide la acción óptima (atajo o ciclo).
   - Ejecuta la acción en el entorno.
3. Se repite hasta que la serpiente muere (colisión).

---

## 🧪 Ejecución del agente

Ejemplo con visualización Pygame:

```python
from agent import HybridAgent
from game.snake_game import SnakeGame

import pygame

game = SnakeGame()
agent = HybridAgent(game)

pygame.init()

while True:
    action = agent.get_action()
    reward, done, score = game.play_step(action)

    game.render_pygame(speed=10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if done:
        print(f"Score: {score}")
        game.reset()
```

---

## 🛠 Requisitos

- Python 3.10+
- Pygame (`pip install pygame`)
- Estructura modular del proyecto como sigue:

```
hamiltonian_snake
├── agent/
│   └── agent.py
├── game/
│   └── snake_game.py
├── logic/
│   ├── hamiltonian.py
│   ├── astar.py
│   └── safety.py
├── main.py
└── README.md
```

---

## 🧠 Ideas para mejoras futuras

- Integrar un modelo supervisado entrenado con dataset generado por el agente.
- Agregar una red neuronal de predicción de seguridad en vez de simulación paso a paso.
- Implementar un evaluador visual (score promedio, distribución de muertes, heatmap de zonas peligrosas).
- Extensión al modo multijugador o agente contra agente.

---

## 🤝 Agradecimientos
Este diseño surge de la colaboración con una mente creativa que buscaba fusionar estrategias seguras, heurísticas de atajo, visualización y estructura progresiva.

---

## 📬 Contacto
Para preguntas o desarrollo adicional, contacta al desarrollador responsable o contribuye al repositorio.

> Que el ciclo Hamiltoniano te guíe, y A* te ilumine el camino 🍀

