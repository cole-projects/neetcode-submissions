

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # for i in range(len(arr) - 1, -1, -1):
        #     # save current element value
        #     temp = arr[i]

        #     #overwrite position
        #     arr[i] = max_right

        #     #update max_right
        #     max_right = max(max_right, temp)

        # return arr