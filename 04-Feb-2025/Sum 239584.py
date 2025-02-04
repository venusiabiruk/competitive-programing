# Problem: Sum - https://codeforces.com/contest/1742/problem/A

testcase = int(input())
for i in range(testcase):
    n,r,t = map(int,(input().split()))
    m = 0

    m = max( n,r,t)
    if m ==  n+r+t - m:
        print("Yes")
    else:
        print("No")


