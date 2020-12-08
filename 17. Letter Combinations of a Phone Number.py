class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def product(lst):
            if not lst:
                yield ''
            else:
                for i in lst[0]:
                    for j in product(lst[1:]):
                        yield i+j
                
        n = len(digits)
        out = []
        lst = []
        dct = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'}

        if digits=='':
            return out
        
        for i in digits:
            lst.append(list(dct[i]))

        out = list(product(lst))

        return out




        