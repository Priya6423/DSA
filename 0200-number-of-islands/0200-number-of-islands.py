class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    count+=1
                    grid[r][c]='0'
                    queue=deque([(r,c)])
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    while queue:
                        cur_r,cur_c=queue.popleft()
                        for dr, dc in directions:
                            new_r, new_c = cur_r + dr, cur_c + dc
                            if 0<=new_r<rows and 0<=new_c<cols:
                                if grid[new_r][new_c]=='1':
                                    grid[new_r][new_c]='0'
                                    queue.append((new_r,new_c))
        return count
        

    
