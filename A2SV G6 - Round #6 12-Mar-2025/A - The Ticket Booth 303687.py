# Problem: A - The Ticket Booth - https://codeforces.com/gym/594077/problem/A

from math import ceil
import math
n,s = map(int,input().split())
ans = math.ceil(s/n)

print(ans)