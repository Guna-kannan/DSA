class Solution:

    def reverseInGroups(self, arr, k):
        """code here"""
        left=0
        right=len(arr)-1
        
        def rotate(arr,left,right):
            while left<right:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1
        
        for i in range(0,len(arr),k):
            left=i
            right=min(i+k-1,len(arr)-1)
        
            rotate(arr,left,right)