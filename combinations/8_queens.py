board = [[0 for _ in range(8)] for _ in range(8)]
cnt = 0
all_cnt = 0
def set_queen(i, j):
    global all_cnt
    all_cnt += 1
    for x in range(8):
        board[x][j] += 1
        board[i][x] += 1
        if 0 <= i+j-x < 8:
            board[i+j-x][x] += 1
        if 0 <= i-j +x < 8:
            board[i-j+x][x] += 1
    board[i][j] = -1

def remove_queen(i, j):
    for x in range(8):
        board[x][j] -= 1
        board[i][x] -= 1
        if 0 <= i+j -x < 8:
            board[i+j-x][x] -= 1
        if 0 <= i-j +x < 8:
            board[i-j+x][x] -= 1
    board[i][j] = 0

def print_position():
    global cnt
    cnt += 1
    abc = 'abcdefgh'
    ans = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == -1:
                ans.append(abc[j] + str(i+1))
    print(', '.join(ans))

def solve(i):
    for j in range(8):
        if board[i][j] == 0:
            set_queen(i, j)
            if i == 7:
                print_position()
            else:
                solve(i+1)
            remove_queen(i, j)

solve(0)
print(cnt)
print(all_cnt)