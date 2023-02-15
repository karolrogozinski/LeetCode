class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        return [int(digit) for digit in str(int(''.join(str(n) for n in num)) + k)]
