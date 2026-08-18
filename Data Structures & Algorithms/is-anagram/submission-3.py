class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = {}
        chars_t = {}

        if (len(s) != len(t)):
            return False
        
        for (char_s, char_t) in zip(s, t):
            if (char_s not in chars_s):
                chars_s[char_s] = 1
            else:
                chars_s[char_s] += 1
            
            if (char_t not in chars_t):
                chars_t[char_t] = 1
            else:
                chars_t[char_t] += 1

        return chars_s == chars_t


        