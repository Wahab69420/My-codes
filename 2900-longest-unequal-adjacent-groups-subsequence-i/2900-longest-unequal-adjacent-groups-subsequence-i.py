class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        prev_group = None

        for word, group in zip(words, groups):
            if prev_group is None or group != prev_group:
                result.append(word)
                prev_group = group

        return result
