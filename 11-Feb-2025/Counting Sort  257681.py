# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    m = max(arr)
    result = [0]* 100
    for num in arr:
        result[num] +=1
    return result
