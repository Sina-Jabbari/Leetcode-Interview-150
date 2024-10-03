class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        array = s.split()
        "splits string ' cat in the  hat' to ['cat','in','the','hat']"
        return len(array[-1])
        
