class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force is dictionary counter + sorting keys
        d = Counter(nums)
        most = d.most_common(k)
        print(most)
        a = map(lambda x: x[0], most)
        return list(a)