import heapq

heap = []
nums = [3,2,2,1,52,6,4,5]
for x in nums:
    heapq.heappush(heap,x)

# for x in nums:
#     print(heapq.heappop(heap))
print(heap[0])