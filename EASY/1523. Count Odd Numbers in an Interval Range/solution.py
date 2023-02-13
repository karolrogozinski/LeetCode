class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low - low%2 - high%2) // 2 + low%2 + high%2
