class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        
        return len(set(nums))
