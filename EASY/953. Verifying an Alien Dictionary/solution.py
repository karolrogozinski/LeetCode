class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        a_dict = {v: k for k, v in zip('abcdefghijklmnopqrstuvwxyz', order)}

        for idx in range(len(words)):
            words[idx] = ''.join(a_dict[s] for s in words[idx])

        unsorted = words[:]
        words.sort()

        return unsorted == words
