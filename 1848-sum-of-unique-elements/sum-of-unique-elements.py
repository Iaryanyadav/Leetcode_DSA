class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

        total = 0
        for num in count:
            if count[num] == 1:
                total += num
        
        return total