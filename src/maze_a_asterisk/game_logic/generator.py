import random


def generate_matrix(
        cols,
        rows,
        obstacle_count,
        start_position=(0, 0),
        end_position=None
):
    if end_position is None:
        end_position = (rows - 1, cols - 1)

    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    all_positions = [
        (r, c)
        for r in range(rows)
        for c in range(cols)
        if (r, c) not in {start_position, end_position}
    ]

    max_obstacles = len(all_positions)
    if obstacle_count > max_obstacles:
        obstacle_count = max_obstacles

    obstacles = random.sample(all_positions, obstacle_count)
    for r, c in obstacles:
        grid[r][c] = 1

    return grid
