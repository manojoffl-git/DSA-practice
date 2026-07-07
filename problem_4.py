class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)

        if len(nums) % 2 == 0:
            i = len(nums) // 2
            return (nums[i - 1] + nums[i]) / 2.0
        else:
            return nums[len(nums) // 2]