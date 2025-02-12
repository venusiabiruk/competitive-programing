# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # [3,3,4,5]
        # [1,2,2,3]
        res = []
        l,r = 0,len(people)-1
        while l <=r:
            if people[r] >= limit:
                res.append(people[r])
                r-=1
            elif people[r] < limit:
                if people[l] +people[r] <= limit:
                    res.append(people[l] +people[r])
                    r-=1
                    l+=1
                else:
                    res.append(people[r])
                    r-=1


        return len(res)






        