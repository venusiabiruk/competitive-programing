# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5 = 0
        count_10 = 0
        for i in bills:
            if i == 5:
                count_5 +=1
            elif i == 10:
                if count_5 >=1:
                    count_5 -=1
                    count_10 +=1
                else:
                    return False
            elif i ==20:
                if count_10 >= 1 and count_5 >= 1:
                    count_5 -= 1
                    count_10 -=1
                elif count_5 >=3:
                    count_5 -=3
                    
                else:
                    return False
        
        return True
       

        