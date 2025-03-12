# Problem: B - Nafargi's Binary Reduction Game - https://codeforces.com/gym/594077/problem/B

n = int(input())
arr = list(map(int,input()))
s = []
for i in arr:
    if s and s[-1]!= i:
        s.pop()
    else:
        s.append(i)
print(len(s))
        