class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []

        nums.sort()

        for i1 in range(len(nums)):
            for i2 in range(i1+1,len(nums)):
                l = i2+1
                r = len(nums)-1
                while  l<r:
                    summ = nums[i1] + nums[i2] + nums[l] + nums[r]
                    if summ>target:
                        r = r-1
                    elif summ<target:
                        l=l+1
                    else:
                        out.append([nums[i1],nums[i2],nums[l],nums[r]])
                        l=l+1
        new_out = []
        for elem in out:
            if elem not in new_out:
                new_out.append(elem)
        out = new_out
        return out
        
        

