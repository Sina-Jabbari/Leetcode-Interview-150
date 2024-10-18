class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse = []
        word = []
        for char in s:
            if char == " ": # on space, append word into list and reset word
                if word:  
                    reverse.append("".join(word))
                    word = []  
            else:   #add char to word 
                word.append(char) 

        if word:  #for last word after last space
            reverse.append("".join(word))

        return " ".join(reverse[::-1])  #returns list starting at end and -1 reversing through it
