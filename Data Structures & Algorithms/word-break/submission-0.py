class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp, for each char, for each word, check if dp[i-n(word)] is True
        # init dp[0] is true, idx + 1
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for word in wordDict:
                word_l = len(word)
                # i is idx
                if i >= word_l - 1 and dp[i - word_l + 1] and s[i-word_l+1:i+1] == word:
                    dp[i + 1] = True
        return dp[-1]