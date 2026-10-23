class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k=k%len(nums)
        left=0
        right=len(nums)-1
        def reverse(nums,left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        
        reverse(nums,0,k-1)
        reverse(nums,k,right)
        reverse(nums,left,right)
