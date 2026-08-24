class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()

        print(nums1)
        l, r = 0, len(nums1) - 1

        if len(nums1) % 2 != 0:
            return nums1[(l + r) // 2]
        else:
            return (nums1[(l + r) // 2] + nums1[((l + r) // 2) + 1]) / 2
            