import heapq
import math


def euclidean(vec1, vec2):
    return math.sqrt((vec1[0] - vec2[0]) ** 2 + (vec1[1] - vec2[1]) ** 2)


class AStarPathFinder:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(
        self,
        grid,
        start=(0,0),
        end=None,
    ):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.end = end if end is not None else (self.rows - 1, self.cols - 1)

    def neighbors(self, cur_vec):
        for dx, dy in self.directions:
            dir_vec = (cur_vec[0] + dx, cur_vec[1] + dy)
            x_into_0_and_n = 0 <= dir_vec[0] < self.n
            y_into_0_and_n = 0 <= dir_vec[1] < self.n
            is_into_maze = x_into_0_and_n and y_into_0_and_n
            is_not_obstacle = self.grid[dir_vec[0]][dir_vec[1]] == 0 if is_into_maze else False
            is_end = dir_vec == self.end
            if is_into_maze and (is_not_obstacle or is_end):
                yield dir_vec

    def find_path(self):
        open_set = [(0, self.start)]
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: euclidean(self.start, self.end)}
        while open_set:
            _, current = heapq.heappop(open_set)

            if current == self.end:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)

                inverse_path = path[::-1]
                return inverse_path

            for neighbor in self.neighbors(current):
                tentative = g_score[current] + 1
                if tentative < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative
                    f_score[neighbor] = tentative + euclidean(neighbor, self.end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None
