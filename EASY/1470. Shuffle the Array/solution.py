class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = list()
        for idx in range(n):
            result.append(nums[idx])
            result.append(nums[idx+n])
        return result
