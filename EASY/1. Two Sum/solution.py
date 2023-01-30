class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            missing = target - num
            if missing in hashmap:
                return [hashmap[missing], idx]
            
            hashmap[num] = idx
