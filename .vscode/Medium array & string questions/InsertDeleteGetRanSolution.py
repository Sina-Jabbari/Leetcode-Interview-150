import random

class RandomizedSet(object):

    def __init__(self):
        self.variable = []          
        

    def insert(self, val):
        boolean = 0
        for i in self.variable:
            if val == i:
                boolean = 1
                """val in set"""
        if boolean == 0:
            self.variable.append(val)
            return True
        else:
            return False
        """
        :type val: int
        :rtype: bool
        if val not in set, add it and return true. else return false.
        """
        

        

    def remove(self, val):
        boolean = 0
        for i in self.variable:
            if val == i:
                boolean = 1
                """val in set"""
        if boolean == 1:
            self.variable.remove(val)
            return True
        else:
            return False
        """
        :type val: int
        :rtype: bool
        if val in set, remove it and return true. else return false.
        """
        
        

    def getRandom(self):
        """
        :rtype: int
        return random element in the set, assume always at leasy 1 element exists
        """
        return random.choice(self.variable)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()