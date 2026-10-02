class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord("a")] += 1

            key = tuple(count)
            output[key] = output.get(key, []) + [s]

        return list(output.values())
        