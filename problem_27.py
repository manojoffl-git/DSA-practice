class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write = 0
        for i in nums:
            if i != val:
                nums[write] = i
                write +=1
        return write