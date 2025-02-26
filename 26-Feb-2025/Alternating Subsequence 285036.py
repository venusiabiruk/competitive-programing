# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    ans = 0
    while i < n:
        same_sign_max = arr[i]
        while i < n and (arr[i] >0) == (same_sign_max >0):
            same_sign_max = max(same_sign_max, arr[i])
            i += 1
        ans += same_sign_max
    print(ans)


 
