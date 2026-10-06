class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
        
        visiting = set()
        visited = set()

        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True        