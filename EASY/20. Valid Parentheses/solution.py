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
            else:
                if temp and bracket_dict[b] == temp[-1]:
                    temp.pop()
                else:
                    return False

        return not temp
