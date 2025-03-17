# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

n,t,c = map(int,(input().split()))
arr = list(map(int,input().split()))
temp_count = 0
total_count = 0
for i in arr:
    if i <= t :
        temp_count +=1
    elif i > t:
        temp_count = 0
    if temp_count >= c:
        total_count +=1
print(total_count)