class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_index = {}
        t_index = {}#create hashmap for each string

        for i in range(len(s)):#loop through the chars on one string

            if s[i] not in s_index: #the char at i not indexed, will be added and set its value to i at index char.
                s_index[s[i]] = i

            if t[i] not in t_index: #same principle
                t_index[t[i]] = i

            if s_index[s[i]] != t_index[t[i]]: #if the index (not value) of s and t match, then keep looping. otherwise, return false
                return False

        return True