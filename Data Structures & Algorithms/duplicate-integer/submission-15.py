class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False
        
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
        


        