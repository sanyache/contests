def exist(board, word) -> bool:
    n = len(board)
    m = len(board[0])
    w = len(word)
    def dfs(row, col, prefix, vis):
        print(word[:prefix+1])
        for r in vis:
            print(*r)
        if prefix == w-1:
            if board[row][col] == word[-1]:
                return  True
            else:
                return False
        r1 = r2 = r3 = r4 = False
        if row + 1 < n and not vis[row+1][col] and board[row+1][col] == word[prefix+1]:
            vis[row+1][col] = True
            r1 = dfs(row+1, col, prefix+1, vis)
        if row - 1 >= 0 and not vis[row-1][col] and board[row-1][col] == word[prefix+1]:
            vis[row-1][col] = True
            r2 = dfs(row-1, col, prefix+1, vis)
        if col + 1 < m and not vis[row][col+1] and board[row][col+1] == word[prefix+1]:
            vis[row][col+1] = True
            r3 = dfs(row, col+1, prefix+1, vis)
        if col - 1 >= 0 and not vis[row][col-1] and board[row][col-1] == word[prefix+1]:
            vis[row][col-1] = True
            print("-1")
            print(word[:prefix+1] + board[col-1][row])
            r4 = dfs(row, col-1, prefix+1, vis)
        vis[row][col] = False
        return r1 or r2 or r3 or r4

    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0]:
                visited = [[False] * m for _ in range(n)]
                visited[i][j] = True
                if dfs(i, j, 0, visited):
                    return True
    return False

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"
print(exist(board, word))

