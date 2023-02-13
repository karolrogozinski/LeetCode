import math

class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        road_map = {x: [] for x in range(len(roads) + 1)}
        result = 0

        for road in roads:
            road_map[road[0]].append(road[1])
            road_map[road[1]].append(road[0])

        def go_deeper(node: int, previous: int) -> int:
            nonlocal result
            num_seats = 1

            for child in road_map[node]:
                if child == previous:
                    continue
                num_seats += go_deeper(child, node)

            result += math.ceil(num_seats/seats) if node else 0
            return num_seats

        go_deeper(0, 0)
        return result
