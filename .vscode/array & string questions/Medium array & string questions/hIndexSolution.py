class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        """SOLUTION: Nested forloop using the formula found on the wikipedia definition for h-index calculation"""
        hindex = 0
        for index in range(len(citations)):
            counter = 0
            for i in range(len(citations)):
                if citations[i] >= index + 1:  
                    counter += 1
            if counter >= index + 1:  
                hindex = index + 1
            else:
                break  
        return hindex