class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        #create graph
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
        #visit each node
        for i in range(numCourses):
            if not self.dfs(graph,visited,i):
                return False
        return True
        
    def dfs(self,graph,visited, i):
        """
        if a node v has not been visted, mark it as 0
        if a node v is being visited, then mark it as -1. during dfs , if we find a vertex marked as -, then
            we have found a cycle.
            if a node v has been visited, then mark it as 1. during dfs, if a vertex was marked 1, then no cycle has v or its successors
        """
        ## if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        ## if it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        # mark as being visited
        visited[i] = -1
        #visit all the neighbors
        for j in graph[i]:
            if not self.dfs(graph,visited,j):
                return False
        #after visit all the neighbors, mark it as done visited
        visited[i] = 1
        return True