class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # check if can be split into these groups
        # use freq map, everytime start from the smallest
        # group * n * group
        if len(hand) % groupSize > 0:
            return False
        
        n = len(hand)
        freq = {}
        for num in hand:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        for num in hand:
            start = num
            if freq[start] > 0:
                # find the start of this group
                while freq.get(start - 1, 0) > 0:
                    start -= 1
                for start in range(start, start + groupSize):
                    if freq.get(start, 0) <= 0:
                        return False
                    freq[start] -= 1
        return True
                    
        