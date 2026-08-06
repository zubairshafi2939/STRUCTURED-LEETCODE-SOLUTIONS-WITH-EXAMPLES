nums = [1,2,3]
class Solution(object):
    def permute(self, nums):
        result = []
        data = set()
        def back(nums,data,res,i = 0):
            data.add(nums[i])
            res.append(nums[i])
            if len(res) == len(nums):
                # print("True")
                result.append(list(res))
                res.pop()
                data.remove(nums[i])
                return
            for n in range(len(nums)):
                if nums[n] not in data:
                    back(nums,data,res,n)
            res.pop()
            data.remove(nums[i])
        for x in range(len(nums)):
            back(nums,data,[],x)
        return result


        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


sol = Solution()
print(sol.permute(nums))
