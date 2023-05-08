class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg=0
        for n in nums:
            if n==0:
                return 0
            if n < 0:
                neg+=1
        if neg%2==1:
            return -1
        return 1
                
            
    
        