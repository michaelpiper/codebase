from collections import defaultdict
import heapq

class Solution:
    def __init__(self):
        pass
    
    def minCostForRepair(self, n, edges, edgesToRepair):
        graph=defaultdict(list)
        addedEdges=set()
        for edge in edgesToRepair:
            graph[edge[0]].append((edge[2], edge[1]))
            graph[edge[1]].append((edge[2], edge[0]))
            addedEdges.add((edge[0], edge[1]))
            addedEdges.add((edge[1], edge[0]))
        for edge in edges:
            if tuple(edge) not in addedEdges:
                graph[edge[0]].append((0, edge[1]))
                graph[edge[1]].append((0, edge[0]))

        res=0
        priorityQueue=[(0, 1)]
        heapq.heapify(priorityQueue)
        visited=set()

        while priorityQueue:
            minCost, node=heapq.heappop(priorityQueue)
            if node not in visited:
                visited.add(node)
                res+=minCost
                for cost, connectedNode in graph[node]:
                    if connectedNode not in visited:
                        heapq.heappush(priorityQueue, (cost, connectedNode))

        return res


s=Solution()

print(s.minCostForRepair(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], [[1, 2, 12], [3, 4, 30], [1, 5, 8]]))
print(s.minCostForRepair(6, [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], [[1, 6, 410], [2, 4, 800]]))
print(s.minCostForRepair(6, [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]], [[1, 5, 110], [2, 4, 84], [3, 4, 79]]))