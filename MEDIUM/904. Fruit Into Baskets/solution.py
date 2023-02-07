class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        max_length = 0
        unique = 0
        start_idx = 0
        basket = dict()

        for idx in range(len(fruits)):
            fruit = fruits[idx]
            if fruit not in basket or not basket[fruit]:
                basket[fruit] = 1
                unique += 1
            else:
                basket[fruit] += 1
            
            if unique <= 2:
                max_length += 1
                continue

            start_fruit = fruits[start_idx]
            start_idx += 1
            basket[start_fruit] -= 1
            if not basket[start_fruit]:
                unique -= 1

        return max_length
