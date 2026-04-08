class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted so binary search? 
        # but you go through each element using binary search for the next element
        for i,n in enumerate(numbers):
            # binary search for the next element
            l,r = i + 1, len(numbers) - 1
            diff = target - n
            while l <= r:
                p = l + (r-l)//2
                if numbers[p] == diff:
                    return [i + 1, p + 1]
                elif numbers[p] < diff:
                    l = p + 1
                else:
                    r = p - 1
        return []
            

        