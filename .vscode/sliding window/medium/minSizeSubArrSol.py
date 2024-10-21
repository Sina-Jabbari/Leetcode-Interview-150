class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        window = 0
        ans = 1000000001
        for right in range(len(nums)):
            window += nums[right]
            #while statement instead of if, in case of multiple skips needed on left pointer
            while window >= target:
                #update answer
                ans = min((right-left) + 1, ans)
                #increment left 
                window -= nums[left]
                left += 1

        if ans == (1000000001):
            return 0

        return ans