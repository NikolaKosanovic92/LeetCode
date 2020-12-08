class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        out = nums[0]+nums[1]+nums[2]
        razlika = abs(out-target)

        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                summ = nums[i]+nums[l]+nums[r]
                razlika1 = summ-target
                if abs(razlika1)>=razlika:
                    if razlika1>0:
                        r = r-1
                    else:
                        l = l+1
                else:
                    out = summ
                    razlika = abs(out-target)
                    if razlika1>0:
                        r = r-1
                    else:
                        l = l+1
        return out