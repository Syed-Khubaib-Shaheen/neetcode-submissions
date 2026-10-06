class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def dfs(row,col,visited):
            visited.add((row,col))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
            
                if (0 <= nr < len(heights) and
                    0 <= nc < len(heights[0]) and 
                    (nr,nc) not in visited and 
                    heights[nr][nc] >= heights[row][col]):

                    dfs(nr,nc,visited)
        
        for col in range(len(heights[0])):
            dfs(0,col,pacific)
        
        for row in range(len(heights)):
            dfs(row,0,pacific)
        
        for col in range(len(heights[0])):
            dfs(len(heights)-1, col, atlantic)
        
        for row in range(len(heights)):
            dfs(row,len(heights[0])-1, atlantic)
        
        answer = []

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) in pacific and (row, col) in atlantic:
                    answer.append([row,col])
        
        return answer

