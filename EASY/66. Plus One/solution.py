class Solution:
    def plusOne(digits: list[int]) -> list[int]:
        if len(digits) == digits.count(9):
            result = [1]
            result.extend(0 for _ in range(len(digits)))
            return result

        for idx in range(len(digits)):
            digits[-(idx+1)] += 1
            if digits[-(idx+1)] != 10:
                break
            digits[-(idx+1)] = 0
        
        return digits
