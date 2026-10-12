class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        nums.sort()
        for i in range(0,n-1,2):
            if(nums[i+1]!=nums[i]):
                return nums[i]
        return nums[n-1]
        
