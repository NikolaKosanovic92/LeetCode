class Solution:
    def reverse(self, x):

        s = str(abs(x))            
        reversed = int(s[::-1])
        
        if reversed > 2147483647:
            return 0
        
        if x > 0:
            return reversed 
        else:
            return (reversed * -1)
        