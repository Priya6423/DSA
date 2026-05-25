class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        maxi=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    queue=deque([(r,c)])
                    count=1
                    grid[r][c]=0
                    directions=[(-1,0),(1,0),(0,-1),(0,1)]
                    while queue:
                        cur_r,cur_c=queue.popleft()
                        for dr,dc in directions:
                            newr,newc=cur_r+dr,cur_c+dc
                            if 0<=newr<row and 0<=newc<col:
                                if grid[newr][newc]==1:
                                    count+=1
                                    grid[newr][newc]=0
                                    queue.append((newr,newc))
                    maxi=max(count,maxi)
        return maxi


        