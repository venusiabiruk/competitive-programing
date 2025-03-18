# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

t = int(input())
for _ in range(t):
    s = list(input().strip())
    team1, team2 = 0, 0
    rem1, rem2 = 5, 5
    min_kicks1 = 10  
    for i in range(10):
        if i % 2 == 0: 
            if s[i] == '1' or s[i] == '?':
                team1 += 1
            rem1 -= 1
        else:  
            if s[i] == '1':
                team2 += 1
            rem2 -= 1
        if team1 > team2 + rem2 or team2 > team1 + rem1:
            min_kicks1 = i + 1
            break
    team1, team2 = 0, 0
    rem1, rem2 = 5, 5
    min_kicks2 = 10  

    for i in range(10):
        if i % 2 == 0: 
            if s[i] == '1':
                team1 += 1
            rem1 -= 1
        else: 
            if s[i] == '1' or s[i] == '?':
                team2 += 1
            rem2 -= 1

        if team1 > team2 + rem2 or team2 > team1 + rem1:
            min_kicks2 = i + 1
            break

    print(min(min_kicks1, min_kicks2))


