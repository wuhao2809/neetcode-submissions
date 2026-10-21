class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # how to do this?
        # check start, if it's impossible, then it's also impossible to start from any points before
        curr = 0
        start = 0
        total = 0
        for i in range(len(gas)):
            curr = curr + (gas[i] - cost[i])
            total += gas[i] - cost[i]
            if curr < 0:
                start = i + 1
                curr = 0
        return start if total >= 0 else -1