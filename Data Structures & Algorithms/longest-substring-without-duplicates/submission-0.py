class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n<=1:
            return n
        left, right = 0, 0
        freq = defaultdict(int)
        res = 0
        while right < n:
            freq[s[right]] += 1
            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1
            right += 1
            res = max(res, right - left)
        return res