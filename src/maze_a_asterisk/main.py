from src.maze_a_asterisk.game_logic.maze_game import MazeGame
from src.maze_a_asterisk.game_logic.generator import generate_matrix
from src.maze_a_asterisk.algorithm.a_star_path_finder import AStarPathFinder

# Parameters
GRID_COLS, GRID_ROWS = 5, 5
CELL_SIZE = 50
MARGIN = 2
OBSTACLES = 5
BACKGROUND_COLOR = (200, 200, 200)

# Element colors (override defaults if desired)
COLOR_FREE = (255, 255, 255)
COLOR_OBSTACLE = (0, 0, 0)
COLOR_START = (0, 255, 0)
COLOR_END = (0, 0, 255)
COLOR_PATH = (255, 0, 0)

START = (0, 0)
END = (GRID_ROWS - 1, GRID_COLS - 1)


def main():
    maze_game = MazeGame(
        cols=GRID_COLS,
        rows=GRID_ROWS,
        cell_size=CELL_SIZE,
        margin=MARGIN,
        background_color=BACKGROUND_COLOR
    )
    maze_game.set_obstacle_num(OBSTACLES)
    maze_game.set_start_end(START, END)
    # Override element colors
    maze_game.color_free = COLOR_FREE
    maze_game.color_obstacle = COLOR_OBSTACLE
    maze_game.color_start = COLOR_START
    maze_game.color_end = COLOR_END
    maze_game.color_path = COLOR_PATH

    img = maze_game.generate_maze(generate_matrix, AStarPathFinder)
    maze_game.show_matplotlib(img)


if __name__ == '__main__':
    main()
