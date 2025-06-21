from src.maze_a_asterisk.view.display import generate_and_display

# Parámetros del tablero
GRID_SIZE = 10
CELL_PIXELS = 50
MARGIN = 2
WIDTH = GRID_SIZE * (CELL_PIXELS + MARGIN) + MARGIN
HEIGHT = WIDTH

# Colores RGB
COLOR_FREE = (255, 255, 255)
COLOR_OBSTACLE = (0, 0, 0)
COLOR_START = (0, 255, 0)
COLOR_END = (0, 0, 255)
COLOR_PATH = (255, 0, 0)
COLOR_BG = (200, 200, 200)


# int(input("Obstaculos: "))
def main():
    generate_and_display(15,
                         GRID_SIZE,
                         HEIGHT,
                         WIDTH,
                         COLOR_BG,
                         COLOR_START,
                         COLOR_END,
                         COLOR_OBSTACLE,
                         COLOR_PATH,
                         COLOR_FREE,
                         CELL_PIXELS,
                         MARGIN,
                         (0, 0),
                         (GRID_SIZE - 1, GRID_SIZE - 1))


if __name__ == 'main':
    main()
