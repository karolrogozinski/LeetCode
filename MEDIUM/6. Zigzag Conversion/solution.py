class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s

        table = ['' for _ in range(numRows)]
        curr_row, direction = 0, 1

        for letter in s:
            table[curr_row] += letter
            if not curr_row:
                direction = 1
            elif curr_row == numRows-1:
                direction = -1
            curr_row += direction

        return ''.join(s for s in table)
