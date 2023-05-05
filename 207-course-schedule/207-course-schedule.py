class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.finishable = set()
        # form graph from preqs
        self.c_preq = {i: [] for i in range(0, numCourses)} # from course returns preqs
        for preq in prerequisites:
            self.c_preq[preq[1]].append(preq[0])

        # all courses
        for i in range(0, numCourses):
            visited = set()
            status = self.preq_check(i, visited)
            if status is False:
                return False
        return True
                        
    def preq_check(self, course, visited):
        
        if len(self.c_preq[course]) == 0 or course in self.finishable:
            return True
        
        else:
            if course in visited:
                return False
            temp = visited
            visited.add(course)
            
            for preq in self.c_preq[course]:
                status = self.preq_check(preq, visited)
                if status is False:
                    return False
                else:
                    self.finishable.add(preq)
        return True
        
            