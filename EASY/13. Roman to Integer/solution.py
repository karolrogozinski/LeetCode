class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        temp = num_dict[s[0]]
        result = temp

        for letter in s[1:]:
            num = num_dict[letter]
            result += num
            if temp < num:
                result -= 2*temp
            temp = num

        return result
