class Solution:
    def findDisappearedNumbers(self, nums):
        for n in nums:
            i = abs(n) - 1
            nums[i] = -abs(nums[i])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]