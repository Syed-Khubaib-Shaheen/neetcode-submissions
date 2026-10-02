class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count ={}
        max_length = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) + 1
            max_frequency = max(count.values())

            while (right-left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1
            
            current_length =(right-left) + 1
            max_length = max(current_length, max_length)
        
        return max_length
            
        