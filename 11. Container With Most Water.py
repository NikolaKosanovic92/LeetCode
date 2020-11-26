class Solution:
    def maxAreaKole(self, height: List[int]) -> int:
        volume = 0
        for i in range (len(height)-1):
            for j in range(i+1, len(height)):
                volume = max(volume, (j-i)*min(height[j],height[i]))
                
        return volume
    
    def maxArea(self, height: List[int]) -> int:
        volume = 0
        left = 0
        right = len(height) - 1

        for i in range(len(height)):

            width = abs(right - left)

            if height[left] < height[right]:   
                res = width * height[left]
                left += 1
            else:
                res = width * height[right]
                right -= 1

            volume = max(volume, res)

        return volume
            
        