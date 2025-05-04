from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            # Sort the word to use as a key
            key = ''.join(sorted(word))
            anagram_map[key].append(word)

        return list(anagram_map.values())
