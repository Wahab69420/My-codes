class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = -1
        k = -1
        for i in range(len(nums2)):
            nums1[j] = nums2[k]
            j = j -1
            k -= 1
        return nums1.sort()
        
        