# main.py

import pygame
from agent.agent import HybridAgent
from game.snake_game import SnakeGame

# Inicialización Pygame
pygame.init()
font = pygame.font.SysFont("Consolas", 24)

# Crear juego y agente
game = SnakeGame(width=20, height=20)
agent = HybridAgent(game)

CELL_SIZE = 20
WIDTH, HEIGHT = game.width * CELL_SIZE, game.height * CELL_SIZE
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT + 40))  # extra espacio para UI
pygame.display.set_caption("Snake Hybrid AI")

clock = pygame.time.Clock()
FPS = 10

modo_actual = "INICIO"


def draw_board():
    SCREEN.fill((30, 30, 30))

    # Dibujar cuerpo completo (cabeza + cuerpo)
    for i, p in enumerate(game.get_snake_body()):
        color = (0, 255, 0) if i == 0 else (0, 100, 0)
        pygame.draw.rect(
            SCREEN,
            color,
            pygame.Rect(p.x * CELL_SIZE, p.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )

    # Dibujar comida
    f = game.get_food()
    pygame.draw.rect(
        SCREEN,
        (255, 50, 50),
        pygame.Rect(f.x * CELL_SIZE, f.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    )

    # Dibujar barra inferior
    pygame.draw.rect(SCREEN, (50, 50, 50), (0, HEIGHT, WIDTH, 40))
    text = font.render(
        f"Score: {game.score}   Longitud: {len(game.body)}   Modo: {modo_actual}",
        True,
        (255, 255, 255),
    )
    SCREEN.blit(text, (10, HEIGHT + 8))

    pygame.display.flip()


# Bucle principal
while True:
    action = agent.get_action()

    # Captura la impresión del agente
    import sys
    from io import StringIO

    temp_stdout = StringIO()
    sys.stdout = temp_stdout
    action = agent.get_action()
    output = temp_stdout.getvalue()
    sys.stdout = sys.__stdout__
    if "ATAJO A*" in output:
        modo_actual = "A*"
    elif "CICLO HAMILTONIANO" in output:
        modo_actual = "Ciclo"

    reward, done, score = game.play_step(action)
    draw_board()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if done:
        print(f"☠️ Juego terminado. Puntuación: {score}")
        game.reset()
        modo_actual = "INICIO"
