class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solution one n2 brute force 
        # 2 pointer n
        # solution 3: dictionary keying, also n
        dind = dict()
        for i in range(len(nums)):
            dind[nums[i]] = i
        for i in range(len(nums)):
            curr = target - nums[i]
            if curr in dind and dind[curr] != i:
                return [i, dind[curr]]
        