class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.adj = {}
        safe = []

        for ind in range(len(graph)):
            self.adj[ind] = graph[ind]
        print(self.adj)
        for ind in range(len(graph)):
            if self.dfs(ind, set()) is True:
                safe.append(ind)
                
                
        return safe
                
    def dfs(self, ind, visited):
        
        if len(self.adj[ind]) == 0:
            return True
        
        elif ind in visited:
            return False
        
        else:    
            found = True
            for i in self.adj[ind]:
                visited.add(ind)
                if self.dfs(i, visited) is False:
                    found = False
                    break
            if found is True:
                self.adj[ind] = []
            return found