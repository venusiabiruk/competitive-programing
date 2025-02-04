# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

testcase = int(input())

for i in range(testcase): # 0 1 2 3 4
    count = 0
    s = input()

    for i, j in zip("codeforces" , s):
        if i != j:
            count +=1
    print(count)