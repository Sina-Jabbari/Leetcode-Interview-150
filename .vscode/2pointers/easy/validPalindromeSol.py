class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        leftchar, rightchar = ' ', ' '

        while left < right:
            leftchar = s[left].lower()
            rightchar = s[right].lower()
            while (leftchar.isalnum() != True or rightchar.isalnum() != True):
                if left < right:
                    if (leftchar.isalnum() != True):
                        left += 1                
                        leftchar = s[left].lower()
                    if rightchar.isalnum() != True:
                        right -= 1      
                        rightchar = s[right].lower()
                else: 
                    return True

            if leftchar == rightchar:
                left += 1
                right -= 1
            else:
                return False

        return True