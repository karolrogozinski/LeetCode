class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        dict_red = {x: [] for x in range(n)}
        dict_blue = {x: [] for x in range(n)}

        for edge in redEdges:
            dict_red[edge[0]].append((edge[1], True))

        for edge in blueEdges:
            dict_blue[edge[0]].append((edge[1], False))

        blue_len = len(blueEdges)
        red_len = len(redEdges)

        result = [0] + [blue_len+red_len+1] * (n-1)
        queue = dict_blue.pop(0) + dict_red.pop(0)
        dict_blue[0] = list()
        dict_red[0] = list()

        iteration = 1
        while queue:
            for idx in range(len(queue)):
                edge = queue.pop(0)
                if edge[1]:
                    queue.extend(dict_blue.pop(edge[0]))
                    dict_blue[edge[0]] = list()
                else:
                    queue.extend(dict_red.pop(edge[0]))
                    dict_red[edge[0]] = list()

                result[edge[0]] = min(result[edge[0]], iteration)

            iteration += 1             

        for idx in range(n):
            if result[idx] == blue_len+red_len+1:
                result[idx] = -1

        return result
