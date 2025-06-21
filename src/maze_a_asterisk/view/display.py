import pygame
import numpy as np
import matplotlib.pyplot as plt
from src.maze_a_asterisk.game_logic.generator import generate_matrix
from src.maze_a_asterisk.algorithm.a_star_path_finder import AStarPathFinder
from src.maze_a_asterisk.view.designer import draw_board_to_surface


def generate_and_display(obstacle_count,
                         grid_size,
                         height,
                         width,
                         color_background,
                         color_start,
                         color_end,
                         color_obstacle,
                         color_path,
                         color_free,
                         cell_pixels,
                         margin,
                         vec_start,
                         vec_end):
    grid = generate_matrix(grid_size, obstacle_count)
    pathfinder = AStarPathFinder(grid)
    path = pathfinder.find_path()
    surface = draw_board_to_surface(grid,
                                    path,
                                    width,
                                    height,
                                    color_background,
                                    color_start,
                                    color_end,
                                    color_obstacle,
                                    color_path,
                                    color_free,
                                    cell_pixels,
                                    margin,
                                    vec_start,
                                    vec_end)
    raw = pygame.image.tostring(surface, 'RGB')
    img = np.frombuffer(raw, dtype=np.uint8).reshape((height, width, 3))
    plt.figure(figsize=vec_end)
    plt.axis('off')
    plt.imshow(img)
    plt.show()
