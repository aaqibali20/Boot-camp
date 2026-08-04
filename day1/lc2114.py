from typing import List
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 0

        for sentence in sentences:
            words = len(sentence.split())
            maxi = max(maxi, words)

        return maxi