class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        dct = {
            '(':')',
            '[':']',
            '{':'}',
        }
        
        for i in range(len(s)):
            if len(lst)>=1 and lst[-1] in dct.keys():
                if s[i]==dct[lst[-1]]:
                    lst.pop()
                else:
                    lst.append(s[i])
            else:
                lst.append(s[i])
        
        return lst==[]