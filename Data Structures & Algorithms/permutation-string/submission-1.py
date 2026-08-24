class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = [s for s in s1]
        letters2 = []
        for i, char in enumerate(s2):
            if char in letters:
                for j in range(i,i+len(letters)):
                    try:
                        letters2.append(s2[j])
                    except:
                        letters2 = []
                if sorted(letters) == sorted(letters2):
                    return True
                letters2 = []
        return False