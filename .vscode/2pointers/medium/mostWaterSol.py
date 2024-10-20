class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        volume, left, right = 0, 0, len(height)-1
        #how to calc volume: height (lower height) x width (difference)
        #volume = low x (right-left)
        #loop and compare next possible height  
        while left < right:
            #find lowest height between two pointers
            low = min(height[left], height[right])

            high = low * (right - left)
            #ensure the highest pair is the volume
            volume = max(volume, high)
            
            #movea pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return volume
