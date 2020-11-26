class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        i = 0
        ch = {}
        for j in range(n):
            if s[j] in ch:
                i = max(i, ch[s[j]])
            ans = max(ans, j-i+1)    
            ch[s[j]]=j+1    
        return ans