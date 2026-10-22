from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        # looping thru array O(n)
        for num in nums:
        # add to defaultdict with frequencies
            count[num] += 1
        # find k most frequent keys 
        return sorted(count, key=count.get, reverse=True)[:k]
