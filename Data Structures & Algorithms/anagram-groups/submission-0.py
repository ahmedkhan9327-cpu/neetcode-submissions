class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        prev = {}

        for str in strs:
            key = "".join(sorted(str))

            if key not in prev:
                prev[key] = []
            
            prev[key].append(str)
            
        return list(prev.values())

