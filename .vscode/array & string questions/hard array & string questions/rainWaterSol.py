class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #preamble
        #pointers left and right with a leftmax and rightmax
        #loop while left is less than right, meaning the pointers have not met
        #if: h[left] > or = leftmax,     else: added to the count at the rate of: size of current point, minus any heights inbetween
        # move left pointer to the right 
        # repeat steps for right pointer
        left, right = 0, len(height) - 1
        leftmax, rightmax = 0, 0
        counter = 0

        while left < right: 
            #left pointer
            if height[left] <= height[right]:
                if height[left] >= leftmax:
                    leftmax = height[left]
                else:
                    counter += leftmax - height[left]
                left += 1
            #right pointer
            else:
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    counter += rightmax - height[right]
                right -= 1

        return counter
