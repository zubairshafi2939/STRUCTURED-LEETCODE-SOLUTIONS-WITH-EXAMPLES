class Solution(object):
    def combinationSum2(self, candidates, target):
        nums = candidates
        nums.sort()
        result = []
        array = []
        def backtrack(arr,total,index,target):
            arr.append(nums[index])
            total += nums[index]
            if total > target or index >= len(nums):
                arr.pop()
                return 
            if total == target:
                result.append(list(arr))
                arr.pop()
                return
            for i in range(index+1,len(nums)):
                if i > index+1 and nums[i] == nums[i-1]:
                    continue
                if (total+nums[i])> target:
                    break
                backtrack(arr,total,i,target)
            arr.pop()
            return
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            
            backtrack(array,0,x,target)

        return result
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
sol = Solution()
print(sol.combinationSum2([1,1,1,1,1,1,1,2,2],8))