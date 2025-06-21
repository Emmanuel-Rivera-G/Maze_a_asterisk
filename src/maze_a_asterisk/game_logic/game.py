import pygame
import numpy as np
import matplotlib.pyplot as plt


class Game:
    def __init__(
            self,
            cell_size: int = 0,
            margin: int = 0,
            background_color=(0, 0, 0),
            width_map: int = 0,
            height_map: int = 0
    ):
        # Drawing parameters
        self.cell_size = cell_size
        self.margin = margin
        self.background_color = background_color

        # Computed surface size (in pixels)
        self.width_map = width_map
        self.height_map = height_map

        # Rendering surface
        self.surface = None

    def raw_to_image(self, raw: bytes) -> np.ndarray:
        return np.frombuffer(raw, dtype=np.uint8) \
            .reshape((self.height_map, self.width_map, 3))

    def surface_to_raw(self) -> bytes:
        if self.surface is None:
            raise RuntimeError("Surface has not been drawn yet.")
        return surface_to_raw(self.surface)

    def show_matplotlib(self, img: np.ndarray) -> None:
        dpi = 100
        figsize = (self.width_map / dpi, self.height_map / dpi)
        plt.figure(figsize=figsize, dpi=dpi)
        plt.axis('off')
        plt.imshow(img)
        plt.show()


def surface_to_raw(surface: pygame.Surface) -> bytes:
    return pygame.image.tostring(surface, 'RGB')
