class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [] 
        #sum of 3 numbers must be 0 where no two sets are the same
        #attempt 1: one for loop with 2 pointers that arent the current num in the loop. if i != j != k and i+left+right = 0
        for n in range(len(nums)):
            if n > 0 and nums[n] == nums[n-1]: #handle dupes
                continue

            left = n+1
            right = len(nums)-1
            while left<right:
                #ensure they add to 0
                if nums[left] + nums[right] + nums[n] == 0:
                    result.append([nums[n], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    #ensure no repeating triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif nums[left] + nums[right] + nums[n] < 0:
                    left += 1
                else:
                    right -= 1

        return result