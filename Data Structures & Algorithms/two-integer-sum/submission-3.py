class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 3, 7, 12, 18
        # brute force lol
        d = dict()
        ind = -1
        for n in nums:
            ind += 1
            d[n] = ind
        print(d)
        
        for i,n in enumerate(nums):
            curr = target - n
            if curr in d:
                print(curr)
                print(i, d[curr])
                if i != d[curr]:
                    return [i, d[curr]]
                




        