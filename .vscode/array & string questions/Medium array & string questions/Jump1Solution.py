class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x=0
        end = len(nums)
        """
        SECTION 1
        DEALING WITH EDGE CASES
        """
        if end == 1:
            return True
        if nums[0]==0:
            return False

        """
        SECTION 2
        CAN END BE REACHED:
        """
        for i in range(end-1,-1,-1):
            
            print (i, nums[i],x)
            if nums[i] >= x and x != 0: 
                return True
            x += 1

        "CAN START REACH POINT THAT CAN REACH END:"
        """
        start at 0, 
        path a jump to x 
        (x is the point at which end can be reached in the previous section)
        if you can reach x, start can reach end. return true
        """
        
        return False
        
        