class Solution:
    def jump(self, nums: list[int]) -> int:
        layer = 0
        left = 0
        right = 0

        while right < len(nums) - 1:
            left, right = right + 1, max(idx + nums[idx] for idx in range(left, right + 1))
            layer += 1
        
        return layer
