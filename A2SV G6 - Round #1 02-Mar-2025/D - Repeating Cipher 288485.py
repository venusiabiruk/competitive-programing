# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n = int(input())
s = list(input())
ans = ""
cur = 0
for i in range(1,55):
    cur += i
    if cur - 1 < n:
        ans += s[cur-1]
    else:
        break
print(ans)





    

    
