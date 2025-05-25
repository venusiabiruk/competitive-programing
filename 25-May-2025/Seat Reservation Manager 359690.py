# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.reserved = []
        self.next = 1

    def reserve(self) -> int:
        if self.reserved:
            return heapq.heappop(self.reserved)
        else:
            seat = self.next
            self.next += 1
            return seat
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.reserved, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)