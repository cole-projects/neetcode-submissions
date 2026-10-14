# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         max_right = -1
        
#         for i in range(len(arr) - 1, -1, -1):
#             temp = arr[i]
#             arr[i] = max_right
#             max_right = max(max_right, temp)

#         return arr


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans
        