class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a counter?
        # niave solution is just
        # bucket sort?
        counter = defaultdict(int)
        bucket = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counter[n] += 1

        for key,value in counter.items():
            bucket[value].append(key)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        


    
            
        