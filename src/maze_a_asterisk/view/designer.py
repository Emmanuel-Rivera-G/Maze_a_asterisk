import pygame


def draw_board_to_surface(grid,
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
                          vec_end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    surface = pygame.Surface((width, height))
    surface.fill(color_background)
    for i in range(rows):
        for j in range(cols):
            x = j * (cell_pixels + margin) + margin
            y = i * (cell_pixels + margin) + margin
            if (i, j) == vec_start:
                c = color_start
            elif (i, j) == vec_end:
                c = color_end
            elif grid[i][j] == 1:
                c = color_obstacle
            elif path and (i, j) in path:
                c = color_path
            else:
                c = color_free
            pygame.draw.rect(surface, c, (x, y, cell_pixels, cell_pixels))
    return surface
