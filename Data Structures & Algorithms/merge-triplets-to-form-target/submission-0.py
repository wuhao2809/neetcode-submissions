class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        state1 = state2 = state3 = False
        for triplet in triplets:
            first, second, third = triplet
            if first <= target[0] and second <= target[1] and third <= target[2]:
                if first == target[0]:
                    state1 = True
                
                if second == target[1]:
                    state2 = True
                
                if third == target[2]:
                    state3 = True
        return state1 and state2 and state3
