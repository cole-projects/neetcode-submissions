class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best_count = current_count = 0
        for num in nums:
            if num == 1:
                current_count += 1
            else:
                best_count = max(current_count, best_count)
                current_count = 0

        return max(current_count, best_count)
        
        
        
        
        # best_count = current_count = 0
        # for i in nums:
        #     if i == 1:
        #         current_count += 1
        #     else:
        #         if current_count > best_count:
        #             best_count = current_count
        #         current_count = 0

        # return max(best_count, current_count)