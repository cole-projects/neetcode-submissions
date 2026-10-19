class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Create array
        n = len(nums)
        ans = [0] * (2 * n)
        # add values back to array using ans[i] == nums[i] and ans[i + n] == nums[i]
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        
        return ans
        