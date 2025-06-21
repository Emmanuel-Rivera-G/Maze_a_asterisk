import pygame


class Game:
    def __init__(
            self,
            cols: int = 0,
            rows: int = 0,
            cell_size: int = 20,
            margin: int = 2,
            background_color=(0, 0, 0)
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
