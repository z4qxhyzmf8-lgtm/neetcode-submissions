class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_cost = sum(cost)
        total_gas = sum(gas)
        if total_cost > total_gas:
            return -1
        n = len(gas)
        total = 0
        for i in range(n):
            gas[i] = total + gas[i] - cost[i]
            total = gas[i]
        best = 0
        for i in range(n):
            if gas[i] < gas[best]:
                best = i
        return (best + 1) % n

        
        