class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        left, right = 0,len(numbers)-1

        while left < right:            
            if (numbers[left]+numbers[right]) == target:
                result.append(left+1)
                result.append(right+1)

            if numbers[left]+numbers[right] < target: #move left up
                left += 1
            else: #move right down
                right -= 1

        return result