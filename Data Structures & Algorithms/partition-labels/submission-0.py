class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, char in enumerate(s):
            last_index[char] = i
        
        res = []
        end = 0
        size = 0
        for i in range(len(s)):
            curr = s[i]
            size += 1
            end = max(end, last_index[curr])

            if i == end:
                res.append(size)
                size = 0
                end = 0
        return res