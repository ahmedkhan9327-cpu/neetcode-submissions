class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = [0, num]
            count[num][0] += 1
        
        num_freq = sorted(count.keys(), key=lambda x: count[x], reverse=True)

        return num_freq[:k]



        