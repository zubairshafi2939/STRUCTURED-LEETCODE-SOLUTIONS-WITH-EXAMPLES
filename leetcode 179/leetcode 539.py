class Solution(object):
    def findMinDifference(self, timePoints):
        nums = []
        for time in timePoints:
            hours = int(time[:2])*60
            minutes = int(time[3:])
            nums.append(hours+minutes)
        nums.sort
        rest = float('INF')
        for x in range(len(nums)-1,-1,-1):
            value = abs((nums[x])-nums[x-1])
            rest = min(rest,min(value,abs((1440-nums[x])+nums[x-1])))
        return rest

        """
        :type timePoints: List[str]
        :rtype: int
        """
timePoints =["00:00","23:59","00:00"]
sol = Solution()
print(sol.findMinDifference(timePoints))