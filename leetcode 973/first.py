import heapq
class Solution(object):
    def kClosest(self, points, k):
        heap = []
        data = {-1:[-1]}
        for x in points:
            square = abs(x[0]*x[0])+ abs(x[1]*x[1])
            if square in data:
                data[square].append(x)
            else:
                data[square] = [x]
            heapq.heappush(heap,square)
        result = []
        while heap:
            num = heapq.heappop(heap)
            for x in data[num]:
                if len(result) == k:
                    return result
                result.append(x)
        return result
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        

points = [[3,3],[5,-1],[-2,4]]
k = 2
sol = Solution()
print(sol.kClosest(points,k))