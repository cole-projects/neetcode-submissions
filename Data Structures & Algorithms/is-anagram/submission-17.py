from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        else:
            return False
        
        
        
        
        # if len(s) != len(t):
        #     return False
            
        # return sorted(s) == sorted(t)
