# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int,input().split())
buildings = list(map(int,input().split()))
p_d = [0] * n
s_d = [0] * n
for i in range(1,n):
    p_d[i] = p_d[i-1] + max(0,buildings[i-1]- buildings[i])
for i in range(n-2,-1,-1):
    s_d[i] = s_d[i+1] + max(0,buildings[i+1]- buildings[i])
for _ in range(m):
    a, b = map(int,input().split())
    if a > b:
        print(s_d[b-1] - s_d[a-1])
    elif b >a:
         print(p_d[b-1] - p_d[a-1])




