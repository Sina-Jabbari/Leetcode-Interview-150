class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 0: #handles edge case
            return 0

        candies = [1] * n 
        #an array of how much candy each child has, default 1. this helps track heigherachy of neighbours candy 

        #loop once from left to right 
        for i in range(1, n):
            # if previous neighbour rating less than current, give current candies one more than the previous neighbour candies
            if ratings[i] > ratings[i - 1]: 
                candies[i] = candies[i - 1] + 1

        #second loop to go from right to left and get the other half of relationships
        for i in range(n - 2, -1, -1):
            # if next neighbour rating less than current, give current candies one more than the next neighbour candies
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
                
        #sum the candies array and return that value
        return sum(candies)