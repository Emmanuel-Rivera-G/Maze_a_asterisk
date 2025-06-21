import pygame
from numpy import ndarray

from src.maze_a_asterisk.game_logic.game import Game


class MazeGame(Game):
    def __init__(
            self,
            cols: int,
            rows: int,
            cell_size: int = 20,
            margin: int = 2,
            background_color=(0, 0, 0),
            width_map: int = 0,
            height_map: int = 0
    ):
        super().__init__(cell_size, margin, background_color, width_map, height_map)
        # Maze grid dimensions (cells)
        self.cols = cols
        self.rows = rows

        # Compute surface size in pixels
        self.width_map = width_map if width_map > 0 else cols * (cell_size + margin) + margin
        self.height_map = height_map if height_map > 0 else rows * (cell_size + margin) + margin

        # Maze state
        self.obstacle_num = None
        self.grid = None
        self.path = None
        self.start = None
        self.end = None

        # Colors for maze elements
        self.color_start = (0, 255, 0)
        self.color_end = (255, 0, 0)
        self.color_obstacle = (100, 100, 100)
        self.color_path = (0, 0, 255)
        self.color_free = (255, 255, 255)

        # Pygame surface
        self.surface = None

    def set_obstacle_num(self, obstacle_num: int) -> None:
        self.obstacle_num = obstacle_num

    def set_maze(self, grid) -> None:
        self.grid = grid

    def set_start_end(self, start, end) -> None:
        self.start = start
        self.end = end

    def draw(self) -> pygame.Surface:
        surf = pygame.Surface((self.width_map, self.height_map))
        surf.fill(self.background_color)
        if self.grid is None:
            return surf

        for i in range(self.rows):
            for j in range(self.cols):
                x = j * (self.cell_size + self.margin) + self.margin
                y = i * (self.cell_size + self.margin) + self.margin

                if (i, j) == self.start:
                    color = self.color_start
                elif (i, j) == self.end:
                    color = self.color_end
                elif self.grid[i][j] == 1:
                    color = self.color_obstacle
                elif self.path and (i, j) in self.path:
                    color = self.color_path
                else:
                    color = self.color_free

                pygame.draw.rect(
                    surf, color,
                    (x, y, self.cell_size, self.cell_size)
                )
        self.surface = surf
        return surf

    def generate_maze(
            self,
            generator,
            PathfinderClass
    ) -> ndarray:
        if self.obstacle_num is None:
            raise ValueError("No hay número de obstaculos.")
        if self.start is None or self.end is None:
            # Default corners
            self.start = (0, 0)
            self.end = (self.rows - 1, self.cols - 1)

        grid = generator(self.cols, self.rows, self.obstacle_num)
        self.set_maze(grid)
        pathfinder = PathfinderClass(grid, self.start, self.end)
        self.path = pathfinder.find_path()

        self.draw()
        raw = self.surface_to_raw()
        return self.raw_to_image(raw)
