### — Planificación General del Sistema Snake IA Híbrido

---

## 🐍 Nombre del Proyecto
**Snake AI — Agente Híbrido con Ciclo Hamiltoniano + A\***

---

## 🎯 Objetivo General

Diseñar e implementar un **agente autónomo híbrido** para el clásico juego Snake, que combine de forma estratégica:
- Un **ciclo Hamiltoniano** como base de navegación segura.
- Algoritmo **A\*** como mecanismo de atajo optimizado hacia la comida.
- Validación de seguridad de cada acción futura para evitar colisiones.
- Una estructura modular extensible orientada a experimentación, visualización y mejora continua.

---

## 📌 Objetivos Específicos

- ✅ Implementar un entorno de juego Snake completamente funcional y desacoplado.
- ✅ Generar un ciclo Hamiltoniano para cualquier tamaño de tablero rectangular.
- ✅ Adaptar A* a un entorno con obstáculos móviles (cuerpo de la serpiente).
- ✅ Validar la seguridad de los caminos con simulación interna paso a paso.
- ✅ Diseñar un agente híbrido que elija entre A* y ciclo según contexto.
- ✅ Modularizar todo el sistema con separación clara de responsabilidades.
- ✅ Establecer infraestructura para análisis visual y testing automatizado.
- ✅ Documentar exhaustivamente cada componente y su lógica.

---

## 🧱 Stack Tecnológico

| Componente | Herramienta/Tech |
|-----------|------------------|
| Lenguaje principal | Python 3.10+ |
| Visualización | Pygame |
| Testing | `pytest` + scripts dedicados |
| Simulación interactiva | Jupyter Notebooks |
| Organización del proyecto | Estructura de paquetes (`agent`, `game`, `logic`) |
| Control de versiones | Git + convenciones de commits semánticos |
| Documentación | Markdown + comentarios inline |

---

## 🚧 Viabilidad Técnica

- ✅ **Experiencia previa del usuario**: ya se cuenta con una versión funcional y se busca ampliarla.
- ✅ **Separación de responsabilidades**: cada módulo es responsable de una tarea específica, lo que facilita testing y mejora incremental.
- ⚠️ **Desafíos esperados**:
  - Generación eficiente del ciclo Hamiltoniano para tableros grandes.
  - Simulación de seguridad que no afecte negativamente el rendimiento.
  - Gestión de estados futuros (crecimiento del cuerpo) de forma precisa.

---

## 🧩 Arquitectura Modular

```plaintext
hamiltonian_snake/
├── agent/
│   └── agent.py              ← Lógica de decisiones híbrida (A* vs Hamiltoniano)
├── game/
│   └── snake_game.py         ← Motor de juego Snake desacoplado
├── logic/
│   ├── hamiltonian.py        ← Generación y recorrido del ciclo Hamiltoniano
│   ├── astar.py              ← Algoritmo A* adaptado
│   └── safety.py             ← Evaluación de seguridad de caminos
├── notebooks/
│   └── tests_*.ipynb         ← Exploraciones, simulaciones y pruebas
├── tests/
│   └── test_*.py             ← Unit testing por módulo
├── main.py                   ← Script principal de ejecución visual
└── 00_PROYECTO.md            ← Documento maestro de planificación
```

---

## ⚙️ Funcionalidades por módulo

### `snake_game.py`
- Crear entorno con dimensiones y estado inicial.
- Retornar cabeza, comida, cuerpo, y aplicar acciones.
- Detectar colisiones, finalización y reinicios.

### `hamiltonian.py`
- Algoritmo de generación del ciclo.
- Recorrido incremental del camino.
- Posibilidad de visualizar el ciclo.

### `astar.py`
- A* para grilla 2D con obstáculos variables.
- Caminos únicos, óptimos y reproducibles.

### `safety.py`
- Simulación interna con avance de cuerpo.
- Capacidad de evaluar múltiples caminos.
- Consideración de crecimiento por comida.

### `agent.py`
- Selección entre A* o Hamiltoniano.
- Validación de seguridad.
- Adaptación a situaciones límite (bloqueos, encierros).

---

## 📊 Formatos y estructuras de datos

| Objeto | Descripción |
|--------|-------------|
| `Point(x, y)` | Coordenada discreta en la grilla |
| `List[Point]` | Camino ordenado |
| `action: List[int]` | `[1,0,0]` = derecha, `[0,1,0]` = izquierda, etc. |

---

## 🧪 Criterios de éxito

- ✅ El agente puede jugar indefinidamente en modo ciclo sin colisionar.
- ✅ Se toma el atajo A* solo cuando es seguro y rentable.
- ✅ La IA logra scores altos de manera consistente.
- ✅ El sistema es fácilmente extendible y modificable.
- ✅ Existen visualizaciones claras del comportamiento.
- ✅ El sistema resiste pruebas unitarias, integración y de estrés.

---

## 📈 Métricas a evaluar

- Score promedio por sesión.
- Porcentaje de veces que se toma un atajo.
- Porcentaje de atajos seguros vs fatales.
- Tiempo promedio por decisión.
- Heatmap de zonas visitadas.

---

## 🧠 Futuras extensiones

- Reemplazo de `safety.py` por red neuronal predictiva.
- Sistema de entrenamiento supervisado con dataset generado.
- Versión multijugador (turnos, simetría, IA-vs-IA).
- Entrenamiento por refuerzo como optimización de decisiones.
- Motor visual de análisis y exploración de estrategias.