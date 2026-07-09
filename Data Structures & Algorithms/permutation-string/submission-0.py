class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # continuous, sliding window
        s1_n = len(s1)
        s2_n = len(s2)
        if s2_n < s1_n:
            return False

        s1_freq = {}
        for char in s1:
            if char not in s1_freq:
                s1_freq[char] = 1
            else:
                s1_freq[char] += 1
            
        print(s1_freq)
        
        num_not_matched = len(s1_freq)
        # create the window
        for i, char in enumerate(s2):
            if char in s1_freq:
                s1_freq[char] -= 1
                if s1_freq[char] == 0:
                    num_not_matched -= 1
            
            if i >= s1_n:
                prev_char = s2[i - s1_n]
                if prev_char in s1_freq:
                    s1_freq[prev_char] += 1
                    if s1_freq[prev_char] == 1:
                        num_not_matched += 1
            
            if num_not_matched == 0:
                return True
        return False

                
            
            
        
        
        