class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i,n in enumerate(nums):
            d[n] = i

        for i,n in enumerate(nums):
            curr = target - n
            if curr in d and d[curr] != i:
                return [i, d[curr]]
           
        

        