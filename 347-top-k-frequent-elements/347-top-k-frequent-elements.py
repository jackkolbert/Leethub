class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_dict = {}
        
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        
        my_list = []
        i = 0
        while i < k:
            max_count = 0
            winner = ""
            for l in my_dict:
                if my_dict[l] > max_count:
                    max_count = my_dict[l]
                    winner = l
                
            i += 1
            my_dict[winner] = 0
            my_list.append(winner)
        return my_list
        