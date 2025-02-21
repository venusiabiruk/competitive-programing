# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

    testcase = int(input())
for _ in range(testcase):
    n,diff = map(int,input().split())
    nums = list(map(int,input().split()))
    nums.sort()
    n = len(nums)//2
    l = (len(nums)//2) - 1 #2
    r = len(nums) - 1
    is_True = True
    for i in range(n): # 0 1 2 
        if nums[r] - nums[l] < diff:
            is_True = False
            break
        l -= 1
        r -= 1

    if is_True:
        print("YES")
    else:
        print("NO")