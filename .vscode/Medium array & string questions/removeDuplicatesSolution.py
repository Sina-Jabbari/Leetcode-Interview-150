class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        java solution:
class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 1;
        for (int i = 1; i < nums.length; i++) {
            for every int thing in the array
            if (nums[i] != nums[i - 1]) {
                if current number doesnt equal prev number, make the first(or next)
                index of array that number
                nums[k] = nums[i];
                k++; go to next index of array
            }
        }
        return k;
        returns how many index's you got up to
    }
}
        """
        k = 0
        for i in range(len(nums)):
            "tweaked to allow one duplicate since the description allows for at most 2 of each int"
            if k < 2 or nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1

        return k
        
        