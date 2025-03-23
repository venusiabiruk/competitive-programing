# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(n)]
    d1 = {}  
    d2 = {}  
    for i in range(n):
        for j in range(k):
            if (i - j) not in d1:
                d1[i - j] = 0
            if (i + j) not in d2:
                d2[i + j] = 0
            d1[i - j] += m[i][j]
            d2[i + j] += m[i][j]
    maxx = 0
    for i in range(n):
        for j in range(k):
            total_sum = d1[i - j] + d2[i + j] - m[i][j]
            maxx = max(maxx, total_sum)
    print(maxx)
