# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

 
t = int(input())
size = ["S","M","L"]
for _ in range(t):
    a, b =  input().split()
    if a == b:
        print("=")
    elif size.index(a[-1]) > size.index(b[-1]):
        print(">")
    elif size.index(a[-1]) < size.index(b[-1]):
        print("<")
    elif a[-1] == b[-1]:
        if a[-1] == size[0]:
            if len(a) > len(b):
                print("<")
            else:
                print(">")
        else:
            if len(a) > len(b):
                print(">")
            else:
                print("<")