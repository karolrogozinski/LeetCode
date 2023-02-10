class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        ones = [(idx, idx_2) for idx, row in enumerate(grid) for idx_2, col in enumerate(row) if col]

        n = len(grid)
        if len(ones) == n**2:
            return -1

        result = 0
        while ones:
            for _ in range(len(ones)):
                one = ones.pop(0)
                for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    new_x, new_y = one[0]+direction[0], one[1]+direction[1]

                    if not 0 <= new_x < n or not 0 <= new_y < n or grid[new_x][new_y]:
                        continue
                    
                    grid[new_x][new_y] = 1
                    ones.append((new_x, new_y))

            result += 1

        return result -1
