class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        target = [0] * 26
        window = [0] * 26

        for i in range(k):
            target[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if window == target:
            return True

        for right in range(k, len(s2)):
            # 新字符进入窗口，旧字符离开窗口
            window[ord(s2[right]) - ord('a')] += 1
            window[ord(s2[right - k]) - ord('a')] -= 1

            if window == target:
                return True

        return False

                
            
            
        
        
        