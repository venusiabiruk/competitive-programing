# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    summ = 0
    max_sum = 0
    left = Counter()
    right = Counter(s)
    for i in s:
        left[i] += 1
        right[i] -=1
        if right[i] == 0:
            del right[i]
        summ = len(left) + len(right)
        max_sum = max(summ,max_sum)


    print(max_sum)
