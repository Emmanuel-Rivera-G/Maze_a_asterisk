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
        self.cols = cols
        self.rows = rows
        self.width_map = width_map if width_map > 0 else cols * (cell_size + margin) + margin
        self.height_map = height_map if height_map > 0 else rows * (cell_size + margin) + margin

        self.obstacle_num = None
        self.grid = None
        self.path = None
        self.start = None
        self.end = None

        # Colores por defecto
        self.color_start = (0, 255, 0)
        self.color_end = (255, 0, 0)
        self.color_obstacle = (100, 100, 100)
        self.color_path = (0, 0, 255)
        self.color_free = (255, 255, 255)

        # Imágenes/texturas
        self.grass_frames = None
        self.cave_img = None
        self.cheese_img = None
        self.rat_frames = None
        self.path_texture = None

        self.frame_index = 0
        self.surface = None

    def set_obstacle_num(self, obstacle_num: int) -> None:
        self.obstacle_num = obstacle_num

    def set_maze(self, grid) -> None:
        self.grid = grid

    def set_start_end(self, start, end) -> None:
        self.start = start
        self.end = end

    def set_path_texture(self, image: pygame.Surface) -> None:
        """Asigna imagen PNG para el camino recorrido."""
        self.path_texture = pygame.transform.scale(image, (self.cell_size, self.cell_size))

    def draw(self) -> pygame.Surface:
        surf = pygame.Surface((self.width_map, self.height_map))
        surf.fill(self.background_color)
        if self.grid is None:
            return surf

        for i in range(self.rows):
            for j in range(self.cols):
                x = j * (self.cell_size + self.margin) + self.margin
                y = i * (self.cell_size + self.margin) + self.margin
                pos = (i, j)

                # Fondo de pasto (animado)
                if self.grass_frames:
                    grass_frame = self.grass_frames[self.frame_index % len(self.grass_frames)]
                    surf.blit(grass_frame, (x, y))
                else:
                    pygame.draw.rect(surf, self.color_free, (x, y, self.cell_size, self.cell_size))

                # Elementos
                if pos == self.start and self.cave_img:
                    surf.blit(self.cave_img, (x, y))
                elif pos == self.end and self.cheese_img:
                    surf.blit(self.cheese_img, (x, y))
                elif self.grid[i][j] == 1:
                    pygame.draw.rect(surf, self.color_obstacle, (x, y, self.cell_size, self.cell_size))
                elif self.path and pos in self.path:
                    if self.path_texture:
                        surf.blit(self.path_texture, (x, y))
                    else:
                        pygame.draw.rect(surf, self.color_path, (x, y, self.cell_size, self.cell_size))

        self.surface = surf
        self.frame_index += 1
        return surf

    def animate_rat(self, rat_frames, frame_delay=300):
        if not self.path:
            return

        clock = pygame.time.Clock()
        frame_index = 0
        window = pygame.display.set_mode((self.width_map, self.height_map))
        pygame.display.set_caption("Animación: Ratita recorriendo el camino")

        for pos in self.path:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.draw()
            x = pos[1] * (self.cell_size + self.margin) + self.margin
            y = pos[0] * (self.cell_size + self.margin) + self.margin

            frame = rat_frames[frame_index % len(rat_frames)]
            window.blit(self.surface, (0, 0))
            window.blit(frame, (x, y))
            pygame.display.flip()

            frame_index += 1
            pygame.time.delay(frame_delay)
            clock.tick(30)

    def generate_maze(self, generator, PathfinderClass) -> ndarray:
        if self.obstacle_num is None:
            raise ValueError("No hay número de obstáculos.")
        if self.start is None or self.end is None:
            self.start = (0, 0)
            self.end = (self.rows - 1, self.cols - 1)

        grid = generator(self.cols, self.rows, self.obstacle_num)
        self.set_maze(grid)
        pathfinder = PathfinderClass(grid, self.start, self.end)
        self.path = pathfinder.find_path()

        self.draw()
        raw = self.surface_to_raw()
        return self.raw_to_image(raw)

