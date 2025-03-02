# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

t = int(input())
for _ in range(t):
    s = input()
    if len(s)%2 != 0:
        print("NO")
    else:
        if s[len(s)//2:len(s)] == s[0:len(s)//2]:
            print("YES")
        else:
            print("NO")