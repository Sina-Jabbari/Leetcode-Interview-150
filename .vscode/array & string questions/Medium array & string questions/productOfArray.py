class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        ans = [1]*n

        left_ans = 1
        for i in range(n):
            ans[i] = left_ans
            left_ans *= nums[i]
        
        # Right pass: accumulate product of all elements to the right of each element
        right_ans = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right_ans
            right_ans *= nums[i]

        return ans
        