class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        ans = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            for i in range (left,right+1):
                ans.append(matrix[top][i])
            top += 1

            for i in range (top,bottom+1):
                ans.append(matrix[i][right])
            right -= 1

            #case where double counting rows 
            if top <= bottom:
                for i in range(right, left - 1, -1): 
                    ans.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans
