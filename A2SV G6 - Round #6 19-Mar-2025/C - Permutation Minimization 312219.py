# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

from collections import deque
t = int(input())
for _ in range(t):
    result = deque()
    n = int(input())
    arr = list(map(int,input().split()))
    for i in arr:
        if not result or i < result[0]:
            result.appendleft(i)
        else:
            result.append(i)
    print(*result)