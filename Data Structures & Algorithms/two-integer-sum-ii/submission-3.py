class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            complement = target - num
            for j, num2 in enumerate(numbers):
                if j != i and num2 == complement:
                    return [i+1,j+1]