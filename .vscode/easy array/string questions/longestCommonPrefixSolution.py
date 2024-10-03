class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = strs[0]
        preLen = len(pre)

        for s in strs[1:]:
            while pre != s[0:preLen]:
                preLen -= 1
                if preLen == 0:
                    return ""

                pre = pre[0:preLen]
        return pre
