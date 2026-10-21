class Solution:
    def checkValidString(self, s: str) -> bool:
        asteroids = 0
        low_left = 0
        high_left = 0
        for char in s:
            if char == '(':
                low_left += 1
                high_left += 1
            elif char == ')':
                low_left -= 1
                high_left -= 1
            else:
                low_left -= 1
                high_left += 1
            
            if high_left < 0:
                return False
            
            low_left = max(0, low_left)
            
        return low_left == 0