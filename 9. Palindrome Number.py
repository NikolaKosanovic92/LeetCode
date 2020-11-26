class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        y=x
        s=0
        while y>0:
            s = s*10
            s+=y%10
            y=y//10
        return x==s