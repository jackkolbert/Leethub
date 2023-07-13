class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = prerequisites
        adj = {}

        for i in range(numCourses):
            adj[i] = []
        for i in range(len(preq)):
            adj[preq[i][0]].append((preq[i][1]))
            
        def dfs(course, visited):
            if len(adj[course]) == 0:
                return True
            
            if course in visited:
                return False
            visited.add(course)
            
            for i in range(len(adj[course])):
                if dfs(adj[course][i], visited) is False:
                    return False
            adj[course] = []
            return True
            
            
            
        for i in range(numCourses):
            if dfs(i, set()) is False:
                return False
            else:
                adj[i] = []
        return True
            