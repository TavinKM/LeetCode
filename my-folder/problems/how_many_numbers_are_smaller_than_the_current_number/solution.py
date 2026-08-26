class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        temp= 0
        ans = []
        for i in nums:
            for j in nums:
                if(i > j):
                    temp += 1
            ans.append(temp)
            temp = 0
        return ans
        