class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m=len(board)
        n=len(board[0])
        def inbound(x,y):
            return 0<=x<m and 0<=y<n

        def is_revealed(x,y):
            return inbound(x,y) and board[x][y]=='M'

        def is_unrevealed_empty(x,y):
            return inbound(x,y) and board[x][y]=='E'

        def revealed_count(x,y):
            revealedCnt=0
            for dy,dx in directions:
                if inbound(x+dy,y+dx) and is_revealed(x+dy,y+dx):
                    revealedCnt+=1
            return revealedCnt

        def updateBoard(x,y,v):
            board[x][y]=v

        directions=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
        queue=deque([click])
        visited=set([(click[0],click[1])])
        while queue:
            x,y=queue.popleft()
            if board[x][y]=='M':
                board[x][y]='X'
                break
            if board[x][y]=='E':
                revealedCount=revealed_count(x,y)
                if revealedCount>0:
                    updateBoard(x,y,str(revealedCount))
                else:
                    updateBoard(x,y,'B')
                    for dy,dx in directions:
                        if is_unrevealed_empty(x+dy,y+dx) and (x+dy,y+dx) not in visited:
                            queue.append((x+dy,y+dx))
                            visited.add((x+dy,y+dx))
        return board