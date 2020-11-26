class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p)==0:
            return len(s)==0
        
        if len(s)>0:
            first = p[0] in [s[0],'.']
        else:
            first = False
        
        if len(p)>= 2 and p[1]=='*':
            return self.isMatch(s, p[2:]) or (first and self.isMatch(s[1:], p))
        else:
            return first and self.isMatch(s[1:], p[1:])