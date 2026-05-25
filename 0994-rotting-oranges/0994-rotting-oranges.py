class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        queue=deque()
        count=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c]==1:
                    count+=1
        if count==0:return 0
        directions=[(-1,0),(0,-1),(1,0),(0,1)]
        count1=0
        while queue:
            level=len(queue)
            for i in range(level):
                curr,curc=queue.popleft()
                for dr,dc in directions:
                    newr,newc=curr+dr,curc+dc
                    if 0<=newr<rows and 0<=newc<cols:
                        if grid[newr][newc]==1:
                            queue.append((newr,newc))
                            grid[newr][newc]=2
                            count-=1
            count1+=1
        return count1-1 if count==0 else -1
        
                    


        

        