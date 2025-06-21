import pygame


class Game:
    def __init__(
            self,
            cols: int = 0,
            rows: int = 0,
            cell_size: int = 20,
            margin: int = 2,
            background_color = (0, 0, 0)
    ):
        # Grid dimensions (in cells)
        self.cols = cols
        self.rows = rows

        # Drawing parameters
        self.cell_size = cell_size
        self.margin = margin
        self.background_color = background_color

        # Computed surface size (in pixels)
        self.width_map = self.cols * (cell_size + margin) + margin
        self.height_map = self.rows * (cell_size + margin) + margin

        # Rendering surface
        self.surface = None

    def set_map_dimensions(
            self,
            cols: int,
            rows: int,
            cell_size = None,
            margin = None
    ) -> None:
        self.cols = cols
        self.rows = rows
        if cell_size is not None:
            self.cell_size = cell_size
        if margin is not None:
            self.margin = margin
        self.width_map = self.cols * (self.cell_size + self.margin) + self.margin
        self.height_map = self.rows * (self.cell_size + self.margin) + self.margin

    def set_game_color(self, background_color) -> None:
        self.background_color = background_color

    def set_cell_pixels(self, cell_size: int, margin = None) -> None:
        self.cell_size = cell_size
        if margin is not None:
            self.margin = margin
        self.width_map = self.cols * (self.cell_size + self.margin) + self.margin
        self.height_map = self.rows * (self.cell_size + self.margin) + self.margin

    def create_surface(self) -> pygame.Surface:
        surf = pygame.Surface((self.width_map, self.height_map))
        surf.fill(self.background_color)
        self.surface = surf
        return surf
