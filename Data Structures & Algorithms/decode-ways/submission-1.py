class Solution:
    def numDecodings(self, s: str) -> int:
        prev2 = 1
        prev1 = 0 if s[0] == "0" else 1

        for i in range(2, len(s) + 1):
            current = 0

            if s[i-1] != "0":
                current += prev1
            if 10 <= int(s[i-2:i]) <= 26:
                current += prev2
            
            prev2 = prev1
            prev1 = current
        
        return prev1

        