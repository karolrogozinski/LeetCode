class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            '}': '{',
            ')': '(',
            ']': '['
        }
    
        temp = []
        for b in s:
            if b in '([{':
                temp.append(b)
                continue
            if temp and bracket_dict[b] == temp[-1]:
                temp.pop()
                continue
            return False

        return not temp
