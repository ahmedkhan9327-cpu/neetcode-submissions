class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        prev = {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if c1 not in prev:
                prev[c1] = 1
            else:
                prev[c1] += 1

            if c2 not in prev:
                prev[c2] = -1
            else:
                prev[c2] -= 1

        for key in prev:
            if prev[key] != 0:
                return False
        return True

        
            
        

