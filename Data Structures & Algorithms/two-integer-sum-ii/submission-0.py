class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            if target - numbers[i] in numbers and numbers.index(target-numbers[i]) != i:
                if i < numbers.index(target-numbers[i]):
                    return [i+1,numbers.index(target-numbers[i])+1]
                else:
                    return [numbers.index(target-numbers[i])+1,i+1]