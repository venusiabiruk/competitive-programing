# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque
n, k = map(int, input().split())
arr = list(map(int, input().split()))
chat = deque()
seen = set()
for i in arr:
    if i not in seen:
        if len(chat) == k:  
            removed = chat.pop()
            seen.remove(removed)  
        chat.appendleft(i) 
        seen.add(i)
print(len(chat))
print(*chat)
 