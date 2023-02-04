class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size_1 = len(s1)
        size_2 = len(s2)
        
        count_dict = {l: 0 for l in string.ascii_lowercase}
        tmp_dict = count_dict.copy()

        for l in s1:
            count_dict[l] = count_dict[l]+1
        for l in s2[:size_1]:
            tmp_dict[l] += 1

        for idx in range(size_1, size_2):
            if count_dict == tmp_dict:
                return True
            tmp_dict[s2[idx-size_1]] -= 1
            tmp_dict[s2[idx]] += 1

        if count_dict == tmp_dict:
            return True
        return False
