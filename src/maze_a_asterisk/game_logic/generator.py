import random


def generate_matrix(size,
                    obstacle_count,
                    start_position=(0, 0),
                    end_position=None):
    if end_position is None:
        end_position = (size - 1, size - 1)
    grid = [[0] * size for _ in range(size)]
    placed = 0
    while placed < obstacle_count:
        obs_x = random.randrange(size)
        obs_y = random.randrange(size)
        random_position = (obs_x, obs_y)
        is_not_start_end = random_position not in [start_position, end_position]
        if is_not_start_end and grid[random_position[0]][random_position[1]] == 0:
            grid[random_position[0]][random_position[1]] = 1
            placed += 1
    return grid
