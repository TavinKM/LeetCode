class Solution(object):
    def findErrorNums(self, nums):
        ans = set()
        for i in nums:
            if i not in ans:
                ans.add(i)
            else:
                dup = i
        for i in range(1,len(nums)+1):
            if i not in ans:
                miss = i
        return [dup,miss]
        