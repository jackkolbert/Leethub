class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxLeft = height[0]
        maxRight = height[-1]
        water = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            
            if maxLeft <= maxRight:
                l += 1
                water += max(min(maxLeft, maxRight) - height[l], 0)
                print(water)
                maxLeft = max(height[l], maxLeft)
            else:
                r -= 1
                water += max(min(maxLeft, maxRight) - height[r], 0)
                print(water)
                maxRight = max(height[r], maxRight)
        
        return water
            
            
        
            
        