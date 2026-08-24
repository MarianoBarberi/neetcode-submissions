class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        left, right  = 0, 1
        res = []
        while left < right:
            if right == len(temperatures):
                res.append(0)
                left += 1
                right = left + 1
                if right == len(temperatures) + 1:
                    left = right
            elif temperatures[right] > temperatures[left]:
                res.append(right-left)
                left += 1
                right = left + 1
            else:
                right += 1
        return res