import heapq
class Solution(object):
    def kClosest(self, points, k):
        heap = []
        for x in points:
            square = abs(x[0]*x[0])+ abs(x[1]*x[1])
            heapq.heappush(heap,(-square,x))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        while heap:
            value,point = heapq.heappop(heap)
            result.append(point)
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