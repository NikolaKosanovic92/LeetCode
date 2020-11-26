class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxlen = 0
        self.start = 0
        
        for i in range(len(s)):
            self.expandFromCenter(s,i,i)
            self.expandFromCenter(s,i,i+1)
            
        return s[self.start:self.start+self.maxlen]
     
    def expandFromCenter(self, s, left, right):
        while left>-1 and right<len(s) and s[left]==s[right]:
            left = left-1
            right = right+1
            
        if self.maxlen < right-left-1:
            self.maxlen = right-left-1
            self.start = left+1