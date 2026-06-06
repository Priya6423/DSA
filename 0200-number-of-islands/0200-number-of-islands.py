class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        queue=deque()
        count=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1':
                    count+=1
                    grid[row][col]='0'
                    queue.append((row,col))
                    directions=[(-1,0),(1,0),(0,-1),(0,1)]
                    while queue:
                        curr,curc=queue.pop()
                        for dr,dc in directions:
                            newr,newc=curr+dr,curc+dc
                            if 0<=newr<rows and 0<=newc<cols:
                                if grid[newr][newc]=='1':
                                    queue.append((newr,newc))
                                    grid[newr][newc]='0'
        return count





        