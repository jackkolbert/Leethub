class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj = {i:[] for i in range(len(points))}
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for k in range(i+1, len(points)):
                x2, y2 = points[k]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((dist, k))
                adj[k].append((dist, i))
        #print(adj)
        
        res = 0
        visited = set()
        
        minHeap = [[0, 0]]  # cost, point
        
        while len(visited) < len(points):
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiCost, nei])
        return res
        
        
        