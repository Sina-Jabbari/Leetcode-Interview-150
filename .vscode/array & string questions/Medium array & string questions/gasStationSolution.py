class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        dont never buy no gas station from the gas station
        """
        total_gas = total_cost = tank = 0
        start = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]
            
            # If the tank goes negative, reset the start point to i+1
            # and reset the tank because this route failed
            if tank < 0:
                start = i + 1
                tank = 0

        # If the total gas is less than the total cost, completing the circuit is impossible
        if total_gas < total_cost:
            return -1

        return start
