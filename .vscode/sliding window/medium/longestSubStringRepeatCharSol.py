class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: 
            return 0  #handle edge case where input string is empty

        ans = 0
        temp = 0
        used = {}  #ditionary to store last seen index of each char
        start = 0  #starting index of the current substring

        for i in range(len(s)):
            current = s[i]

            #if char alr in dictionary AND in current window
            if current in used and used[current] >= start:
                start = used[current] + 1  #move the start to avoid repeating chars

            #update the last seen index of the current char
            used[current] = i

            #calc length of current non-repeating substring
            temp = i - start + 1

            #update max len
            ans = max(ans,temp)

        return ans
