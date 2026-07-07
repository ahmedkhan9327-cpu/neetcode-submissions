class Solution:

    def encode(self, strs: List[str]) -> str:
        sb = ""

        for s in strs:
            sb += str(len(s))
            sb += "#"
            sb += s
        
        return sb

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while (i < len(s)):
            j = i

            while (s[j] != "#"):
                j += 1

            sl = int(s[i : j])

            result.append(s[j + 1: j + 1 + sl])

            i = j + 1 + sl
        
        return result

            


