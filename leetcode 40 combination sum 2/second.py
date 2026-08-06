class Solution(object):
    def combinationSum2(self, candidates, target):
        result = []
        def back(cand,target,res,i = 0, total = 0, ):
            res.append(cand[i])
            total += cand[i]
            if total == target:
                copy = list(res)
                copy.sort()
                if copy in result:
                    return
                result.append(copy)
                return
            if total > target:
                return 
            for n in range(i+1,len(cand)):
                back(cand,target,list(res),n,total)
        for x in range(len(candidates)):
            back(candidates,target,[],x,0)
        return result
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
sol = Solution()
print(sol.combinationSum2([1,1,1,1,1,1,1,2,2],8))