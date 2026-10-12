class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOne(num):
            out = 0
            while num:
                num &= (num-1)
                out += 1
            return out
        res = [0] * (n + 1)
        for i in range(1, n+1):
            res[i] = countOne(i)
        return res
        