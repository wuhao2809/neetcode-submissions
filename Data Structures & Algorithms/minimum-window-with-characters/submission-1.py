class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # maintain a sliding window, it will keep slding until window_s contains all t
        # slide left pointer, until window_s < t, update res
        res_start = 0
        res_end = -1
        curr_start = 0

        curr_freq = {}
        for char in t:
            if char not in curr_freq:
                curr_freq[char] = 1
            else:
                curr_freq[char] += 1
        
        num_needed = len(curr_freq)
        for i, char in enumerate(s):
            if char in curr_freq:
                curr_freq[char] -= 1
                if curr_freq[char] == 0:
                    num_needed -= 1
            
            # check if curr window meets the demand
            while num_needed == 0:
                #  update res
                if res_end - res_start < 0 or res_end - res_start > i - curr_start:
                    res_end = i
                    res_start = curr_start
                # move left
                if s[curr_start] in curr_freq:
                    curr_freq[s[curr_start]] += 1
                    if curr_freq[s[curr_start]] > 0:
                        num_needed += 1
                curr_start += 1
        
        # check res
        if res_end - res_start >= 0:
            return s[res_start : res_end + 1]
        else:
            return ""
        
        