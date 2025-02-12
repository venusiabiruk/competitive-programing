# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        m = 0 
        for l in range(len(seats)):
            if seats[l] > students[l]:
                m += seats[l] - students[l]
            elif seats[l] < students[l]:
                m += students[l]-seats[l]
            elif seats[l] == students[l]:
                continue
        return m
               
        




        