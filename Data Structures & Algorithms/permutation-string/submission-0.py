class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = {}
        count2 = {}

        for char in s1:
            count1[char] = count1.get(char, 0) + 1

        for char in s2[:len(s1)]:
            count2[char] = count2.get(char, 0) + 1

        if count1 == count2:
            return True

        for right in range(len(s1), len(s2)):
            left_char = s2[right - len(s1)]
            right_char = s2[right]

            count2[left_char] -= 1

            if count2[left_char] == 0:
                del count2[left_char]

            count2[right_char] = count2.get(right_char, 0) + 1

            if count1 == count2:
                return True

        return False