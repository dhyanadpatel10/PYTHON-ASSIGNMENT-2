MOD = 1000000007

def max_path(matrix):
    n, m = len(matrix), len(matrix[0])
    dp = [[-10**9]*m for _ in range(n)]
    ways = [[0]*m for _ in range(n)]

    if matrix[0][0] != "X":
        dp[0][0] = int(matrix[0][0])
        ways[0][0] = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "X": continue
            val = int(matrix[i][j])
            for di,dj in [(0,-1),(-1,0),(-1,-1)]:
                ni,nj = i+di,j+dj
                if 0<=ni<n and 0<=nj<m and dp[ni][nj]!=-10**9:
                    score = dp[ni][nj]+val
                    if score>dp[i][j]:
                        dp[i][j]=score
                        ways[i][j]=ways[ni][nj]
                    elif score==dp[i][j]:
                        ways[i][j]=(ways[i][j]+ways[ni][nj])%MOD
    if dp[n-1][m-1]==-10**9:
        print("IMPOSSIBLE")
    else:
        print(dp[n-1][m-1], ways[n-1][m-1])

# ---------------- SAMPLE INPUT ----------------
matrix = [
    ["1","2","3"],
    ["4","X","6"],
    ["7","8","9"]
]
max_path(matrix)
