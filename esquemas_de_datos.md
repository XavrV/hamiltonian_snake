## 🧩 ESQUEMAS DE DATOS Y ESTRUCTURAS CLAVE

---

### 1. **Entidad central: `Point(x: int, y: int)`**
- Representa coordenadas en el tablero.
- Estructura **inmutable** (tipo `namedtuple` o `dataclass(frozen=True)`).
- Usado en **todo**: cabeza, comida, cuerpo, caminos, ciclos, obstáculos.
- Necesario definir `__eq__`, `__hash__`, y orden si usamos `heapq`.

🟩 **Propuesta**:
```python
@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int
```

---

### 2. **Estado de la serpiente (`SnakeGame`)**

```python
class SnakeGame:
    width: int
    height: int
    head: Point
    food: Point
    body: List[Point]
    direction: str  # 'LEFT', 'RIGHT', etc.
```

- `body[0]` puede o no ser la cabeza (dependiendo del diseño).
- Necesitamos **copias profundas** del cuerpo para simulaciones en `safety.py`.
- El estado actual debe ser **observable pero no modificable externamente**.

---

### 3. **Acciones**
```python
Action = List[int]  # [1,0,0], [0,1,0], etc.
```

- Estructura vectorial, útil para compatibilidad con RL en el futuro.
- Alternativa más legible:
```python
from enum import Enum
class Direction(Enum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3
```
- Se puede mapear fácilmente a vectores con función `direction_to_action()`.

---

### 4. **Ciclo Hamiltoniano**

```python
hamiltonian_path: List[Point]
```

- Es una lista ordenada fija y cíclica que cubre todas las celdas del tablero.
- Lo ideal es que se **genere una vez** y se reutilice.
- Se puede almacenar como `Dict[Point, Point]` para obtener el siguiente punto en O(1).

🟩 **Propuesta adicional**:
```python
# Mapeo de cada punto a su sucesor
next_point_in_cycle: Dict[Point, Point]
```

---

### 5. **Camino A\* y obstáculos**

```python
path: Optional[List[Point]]  # Camino óptimo a la comida
obstacles: Set[Point]        # Posiciones ocupadas por el cuerpo
```

- `obstacles` debe actualizarse en cada paso.
- El path debe ser evaluado antes de ejecutarlo, no asumido como seguro.

---

### 6. **Simulación de seguridad (`safety.py`)**

```python
def is_path_safe(path: List[Point], body: List[Point], future_growth: int = 1) -> bool
```

- Internamente mantiene una copia del cuerpo y simula el avance.
- Posible optimización: usar un `deque` para manejo eficiente de cabeza/cola.
- Evaluar incluir “buffer de escape” en caso de encierros cercanos.

---

### 7. **Decisión del agente**

```python
class HybridAgent:
    def get_action() -> Action
```

- Internamente mantiene:
  - Referencia a `SnakeGame`
  - Referencia al `hamiltonian_path`
  - `last_action`, `last_path`, etc. para depuración o aprendizaje futuro.

---

## 🔗 Relaciones clave entre módulos

- `agent.py` necesita:
  - acceso a `SnakeGame`
  - `hamiltonian_path` generado por `hamiltonian.py`
  - resultados de `astar.py`
  - validación de `safety.py`

- `astar.py` y `safety.py` dependen de:
  - conocimiento del tablero (ancho/alto)
  - obstáculos (cuerpo actual)
  - posibles estados futuros

---

## 🔄 Inmutabilidad vs Mutabilidad

| Estructura | ¿Mutable? | ¿Reutilizable? |
|-----------|-----------|----------------|
| `Point` | ❌ | ✅ |
| `List[Point]` (caminos, cuerpo) | ✅ | Copias profundas necesarias |
| `Set[Point]` (obstáculos) | ✅ | Puede derivarse de `body` |
| `Dict[Point, Point]` (ciclo) | ❌ | ✅ ciclo fijo |
| `SnakeGame` | ✅ | Estado mutable del entorno |
| `HybridAgent` | ✅ | Memoria interna, ajustable |
