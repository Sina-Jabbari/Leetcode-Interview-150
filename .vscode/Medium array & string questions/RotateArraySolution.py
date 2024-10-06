import array
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """ 
        k = k % (len(nums))
        end = (len(nums))
        new = array.array('i')
        
        for i in range(end - k, end):
            new.append(nums[i])

    # Append the remaining elements from the start of the array
        for i in range(0, end - k):
            new.append(nums[i])

    # Copy back the new array to nums
        for i in range(end):
            nums[i] = new[i]