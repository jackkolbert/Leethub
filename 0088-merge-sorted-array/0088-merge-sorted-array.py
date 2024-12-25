class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        n1_ind = m-1
        n2_ind = n-1
        placement_ind = n+m-1
        
        while n2_ind >= 0:
            
            if n1_ind >= 0 and nums2[n2_ind] < nums1[n1_ind]:
                nums1[placement_ind] = nums1[n1_ind]
                n1_ind -= 1
            else:
                nums1[placement_ind] = nums2[n2_ind]
                n2_ind -= 1
            placement_ind -= 1                