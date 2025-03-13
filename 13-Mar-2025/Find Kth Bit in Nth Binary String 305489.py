# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def find_bit(n):
            arr = []
            # reversed_arr
            result = ""
            if n == 1:
                return "0"
            else:
                prev = find_bit(n-1)
            # prev = 0 
            for bit in prev:
                if bit == "0":
                    arr.append("1")
                else:
                    arr.append("0")
            arr.reverse()
            reversed_arr = "".join(arr)
            result = prev + "1" + reversed_arr
            return result
        ans = find_bit(n)   
        return ans[k-1]
        
             
        







        