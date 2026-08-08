class Solution(object):
    def combinationSum3(self, k, n):
        nums = 1,2,3,4,5,6,7,8,9
        result = []
        arr = [0]*(k)
        def backtrack(arr,index,total,n,number):
            total += number
            arr[index] = number
            if index >= (k-1):
                if total == n:
                    result.append(list(arr))
                return
            for i in range(number+1,10):
                if (total + i) > n:
                    break
                backtrack(arr,index+1,total,n,i)
            return
        for x in range(1,10):
            if x > n:
                break
            backtrack(arr,0,0,n,x)
        return result
                    
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

sol = Solution()
print(sol.combinationSum3(3,9))