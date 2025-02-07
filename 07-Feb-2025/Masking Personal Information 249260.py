# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.split('@')
            for i in range(2):
               s[i] = s[i].lower()
            list1_name = list(s[0])
            s[0] = list1_name[0] + "*"*5 + list1_name[-1]
            result = "@".join(s)
            return result
        else:
            Separation_characters = "+-(), " 
            num =[]
            mask = ""
            for i in s:
                if i in Separation_characters:
                    continue
                num.append(i)
            if len(num) == 10:
                mask = "***-***-"
            elif len(num) == 11:
                mask = "+*-***-***-"
            elif len(num) == 12:
                mask = "+**-***-***-"
            elif len(num) == 13:
                mask = "+***-***-***-"
            num = num[-4:]
            num = "".join(num)
            mask = mask + num
            return mask
            















