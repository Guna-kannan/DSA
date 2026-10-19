class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)//2
        c={}
        for i in nums:
            if(i in c):
                c[i]+=1
            else:
                c[i]=1
        
        for key,val in c.items():
            if(val>n):
                return key

