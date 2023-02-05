class Solution:
    def climbStairs(self, n: int) -> int:
        result = 1
        def factorial(n):
            return n*factorial(n-1) if n > 1 else 1
        for number in range(2, n+1, 2):
            result += factorial(n-number/2)/(factorial(n-number) * factorial(number/2))
        return int(result)
