class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i:[] for i in range(numCourses)}
        #map class to prerequisites
        for cr, pr in prerequisites:
            pre[cr].append(pr)

        visit = set()

        def dfs(cr):
            # if our current class has already been visited, cycle
            if cr in visit:
                return False
            # if our current class has no more prereqs, we can take!
            if pre[cr] == []:
                return True
            
            visit.add(cr) #mark visited
            for p in pre[cr]: #for each prereq
                if not dfs(p): # if it is in a cycle
                    return False #Falses propogate
            visit.remove(cr) #backtrack
            pre[cr] = [] # all cr prereqs satisfieable
            return True 
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
