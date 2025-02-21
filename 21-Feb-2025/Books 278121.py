# Problem: Books - https://codeforces.com/contest/279/problem/B

n,t = map(int,input().split())
li = list(map(int,input().split()))
l = 0
s = 0
count = 0
max_count = 0
for r in range(n):
    s += li[r]
    count +=1
    while s > t:
        count -=1
        s -= li[l]
        l+=1
    max_count = max(count,max_count)
print(max_count)
    
