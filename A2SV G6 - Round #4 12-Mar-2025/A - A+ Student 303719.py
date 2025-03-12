# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    max_num = max(a,b,c)
    if a == max_num and a!=b and a!= c:
        A = 0
    else:
        A = (max_num-a)+1
    if b == max_num and b!=a and b!= c:
        B = 0
    else:
        B = (max_num-b)+1
    if c == max_num and c!=b and c!= a:
        C = 0
    else:
        C = (max_num-c)+1
    
    print(A,B,C)
