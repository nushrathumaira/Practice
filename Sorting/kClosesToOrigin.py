import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_heap = []
        for (x,y) in points:
            dist = -(x**2+y**2)
            if len(distance_heap) == k:
                heapq.heappushpop(distance_heap,(dist,x,y))
            else:
                heapq.heappush(distance_heap,(dist,x,y))
        return [(x,y) for (dist,x,y) in distance_heap]