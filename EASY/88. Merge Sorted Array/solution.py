class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """  
        idx = 0
        inserted = 0
        nums1[:] = nums1[:m]
        while nums2 and idx < m:
            if nums2[0] < nums1[idx+inserted]:
                nums1.insert(idx+inserted, nums2.pop(0))
                inserted += 1
                continue
            idx += 1
        nums1[:] = [*nums1, *nums2]
