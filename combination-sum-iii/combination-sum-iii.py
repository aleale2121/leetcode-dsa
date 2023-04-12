class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(path,curr,i):
            if len(path)==k:
                if curr==n:
                    ans.append(path[:])
                return
            
            for num in range(i,10):
                if curr+num<=n:
                    path.append(num)
                    backtrack(path,curr+num,num+1)
                    path.pop()       
            return 
        ans=[]
        backtrack([],0,1)
        return ans
        