import pygame
import sys
import os
from src.maze_a_asterisk.game_logic.maze_game import MazeGame
from src.maze_a_asterisk.game_logic.generator import generate_matrix
from src.maze_a_asterisk.algorithm.a_star_path_finder import AStarPathFinder
from src.maze_a_asterisk.ui.menu import Menu
from src.maze_a_asterisk.utils.gift_loader import load_gif_frames

# --- Constantes de configuración ---
GRID_COLS, GRID_ROWS = 10, 10
CELL_SIZE = 60
MARGIN = 2
BACKGROUND_COLOR = (220, 220, 220)

COLOR_FREE = (255, 255, 255)
COLOR_OBSTACLE = (50, 50, 50)
COLOR_START = (0, 255, 0)
COLOR_END = (255, 0, 0)
COLOR_PATH = (0, 100, 255)

# --- Cargar assets desde la misma carpeta que main.py ---
current_dir = os.path.dirname(__file__)

# Ratita animada
rat_frames = load_gif_frames(os.path.join(current_dir, "ratitas.gif"))
rat_frames = [pygame.transform.scale(f, (CELL_SIZE, CELL_SIZE)) for f in rat_frames]

# Fondo de pasto animado
grass_frames = load_gif_frames(os.path.join(current_dir, "grass.gif"))
grass_frames = [pygame.transform.scale(f, (CELL_SIZE, CELL_SIZE)) for f in grass_frames]

# Imagen de queso (meta)
cheese_img = pygame.image.load(os.path.join(current_dir, "cheese.png"))
cheese_img = pygame.transform.scale(cheese_img, (CELL_SIZE, CELL_SIZE))

# Imagen del camino
path_img = pygame.image.load(os.path.join(current_dir, "path.png"))
path_img = pygame.transform.scale(path_img, (CELL_SIZE, CELL_SIZE))


def elegir_inicio_y_fin(screen, cols, rows, cell_size, margin) -> tuple:
    clock = pygame.time.Clock()
    start = None
    end = None

    ancho = cols * (cell_size + margin) + margin
    alto = rows * (cell_size + margin) + margin
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Selecciona INICIO y FIN")

    while True:
        screen.fill((255, 255, 255))

        for i in range(rows):
            for j in range(cols):
                x = j * (cell_size + margin) + margin
                y = i * (cell_size + margin) + margin
                color = (200, 200, 200)
                if (i, j) == start:
                    color = (0, 255, 0)
                elif (i, j) == end:
                    color = (255, 0, 0)
                pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                col = mx // (cell_size + margin)
                row = my // (cell_size + margin)
                if 0 <= row < rows and 0 <= col < cols:
                    pos = (row, col)
                    if not start:
                        start = pos
                    elif not end and pos != start:
                        end = pos
                        return start, end

        clock.tick(30)


def main():
    pygame.init()
    menu_screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Maze A* Pathfinder")
    font = pygame.font.SysFont("arial", 36)

    menu = Menu(menu_screen, font)
    menu.show_main_menu()
    obstacle_count = menu.prompt_obstacles()

    start, end = elegir_inicio_y_fin(menu_screen, GRID_COLS, GRID_ROWS, CELL_SIZE, MARGIN)

    maze_game = MazeGame(
        cols=GRID_COLS,
        rows=GRID_ROWS,
        cell_size=CELL_SIZE,
        margin=MARGIN,
        background_color=BACKGROUND_COLOR
    )
    

    maze_game.set_obstacle_num(obstacle_count)
    maze_game.set_start_end(start, end)

    # Colores por defecto (opcional si tienes imágenes)
    maze_game.color_free = COLOR_FREE
    maze_game.color_obstacle = COLOR_OBSTACLE
    maze_game.color_start = COLOR_START
    maze_game.color_end = COLOR_END
    maze_game.color_path = COLOR_PATH

    # 🧩 Asignar assets
    maze_game.rat_frames = rat_frames
    maze_game.grass_frames = grass_frames
    maze_game.cheese_img = cheese_img
    maze_game.set_path_texture(path_img)


    # Generar laberinto y mostrar animación
    maze_game.generate_maze(generate_matrix, AStarPathFinder)
    maze_game.animate_rat(rat_frames, frame_delay=300)

    pygame.quit()


if __name__ == '__main__':
    main()
