class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col=len(grid),len(grid[0])
        queue=deque()
        count=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for rows in range(row):
            for cols in range(col):
                if grid[rows][cols]=='1':
                    count+=1
                    grid[rows][cols]='0'
                    queue.append((rows,cols))
                    while queue:
                        curr,curc=queue.popleft()
                        for dr,dc in directions:
                            newr,newc=curr+dr,curc+dc
                            if 0<=newr<row and 0<=newc<col:
                                if grid[newr][newc]=='1':
                                    queue.append((newr,newc))
                                    grid[newr][newc]='0'
        return count
        