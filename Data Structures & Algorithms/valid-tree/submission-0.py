class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        def dfs(node, parent):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                
                if neighbor in visited:
                    return False
                
                if not dfs(neighbor, node):
                    return False
            
            return True
        return dfs(0,-1) and len(visited) == n



        