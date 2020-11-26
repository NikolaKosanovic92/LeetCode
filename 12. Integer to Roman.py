class Solution:
    def intToRoman(self, num: int) -> str:
        
        ls1 = ['I','X','C','M']
        ls5 = ['V','L','D']
        res=''
        numlst = []


        while num>0:
            n = num%10
            numlst.append(n)
            num = num//10

        for i,v in enumerate(numlst):
            if v in [1,2,3]:
                res = res+(ls1[i]*v)
            elif v in [5,6,7,8]:
                res = res+(ls1[i]*(v-5))+ls5[i]
            elif v in [4]:
                res = res+ls5[i]+ls1[i]
            elif v in [9]:
                res = res+ls1[i+1]+ls1[i]
            else:
                pass

        return (res[::-1])



