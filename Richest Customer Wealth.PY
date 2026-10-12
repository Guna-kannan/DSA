class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        a=len(accounts)
        b=[]
        for i in range(0,len(accounts)):
            sum1=0
            for j in range(0,len(accounts[i])):
                sum1+=accounts[i][j]
            b.append(sum1)
        return max(b)
        