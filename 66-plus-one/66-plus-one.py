class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        found = False
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
                continue
            else:
                digits[i] += 1
                found = True
                break
                
        if found is False:
            return [1] + digits
        else:
            return digits
            