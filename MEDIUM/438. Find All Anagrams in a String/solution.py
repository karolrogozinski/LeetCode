class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        size_p = len(p)
        size_s = len(s)

        count_p = {l: 0 for l in string.ascii_lowercase}
        count_s = count_p.copy()

        for letter in p:
            count_p[letter] += 1
        for letter in s[:size_p]:
            count_s[letter] += 1

        result = list()
        if count_p == count_s:
            result.append(0)
        for idx in range(size_p, size_s):
            count_s[s[idx]] += 1
            count_s[s[idx-size_p]] -= 1
            if count_p == count_s:
                result.append(idx-size_p+1)

        return result
