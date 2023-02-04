class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        count_dict = {l: 0 for l in'abcdefghijklmnopqrstuvwxyz'}
        for l in s1:
            count_dict[l] = count_dict[l]+1

        for idx in range(len(s2)-window_size+1):
            solution = True
            tmp = s2[idx:idx+window_size]
            
            for letter in tmp:
                if tmp.count(letter) != count_dict[letter]:
                    solution = False
                    break
            if solution:
                return True
        
        return False
