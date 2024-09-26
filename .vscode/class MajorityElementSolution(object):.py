class  MajorityElementSolution(object):
    def majorityElement(self, nums):
        "init variables conuter to track instances of majority element"
        counter = 0
        ans = None
        """
        go through each int in array and make a counter for each of them, higher counter will be the majority element
        
        if counter is 0 then the current number is the current majority element
        if the int is equal to the current majority element, inc counter
        if the int is not equal to the current majority element, dec counter
        """
        for num in nums:
            if counter == 0:
                ans = num
            if num == ans:
                counter +=1
            else:
                counter -=1
        return ans
