class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordHash = defaultdict(int)
        for word in s:
            wordHash[word] += 1

        wordHash2 = defaultdict(int)
        for word in t:
            wordHash2[word] += 1

        if wordHash == wordHash2:
            return True
        return False