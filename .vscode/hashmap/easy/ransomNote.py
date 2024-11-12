from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dictionary = Counter(magazine)  # Count the occurrences of each character in magazine
        
        for char in ransomNote:
            if dictionary[char] > 0:  # If there's at least one of this character in magazine
                dictionary[char] -= 1  # Use this character
            else:
                return False  # If the character is not available or used up
        
        return True  # All characters in ransomNote were found in magazine
