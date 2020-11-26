class Solution:
    def longestCommonPrefixKole(self, strs: List[str]) -> str:
        if not strs:
            return ''
    
        pref = strs[0]
        for s in strs:
            n = min(len(s),len(pref))
            tmp = ''
            for j in range(n):
                if s[j]==pref[j]:
                    tmp = tmp + pref[j] 
                else:
                    break
                    
            if len(tmp)<len(pref):
                pref = tmp

        return pref