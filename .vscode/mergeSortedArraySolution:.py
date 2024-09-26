class Solution(object):
    def merge(self, nums1, m, nums2, n):
        import numpy as np

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        """
        store num2 into num1, must start writing into the array after 'm'th index
        sort array
        """
        #nums1 = nums1[:m]  # Keep only the elements up to index m (removes everything after m)
        for i in range(n):
            nums1[m + i] = nums2[i]

        #now sort, bubblesort
        n = len(nums1)
    
        for i in range(n):
            for j in range(0, n-i-1):
                if nums1[j] > nums1[j+1]:
                    nums1[j], nums1[j+1] = nums1[j+1], nums1[j]
