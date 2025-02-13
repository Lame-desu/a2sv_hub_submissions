# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count_array = [0] * (max(costs) + 1)

        for num in costs:
            count_array[num]+=1
        
        max_icecream = 0
        for i in range(len(count_array)):
            while count_array[i] > 0:
                coins-=i
                max_icecream+=1
                count_array[i] -= 1
                if coins < 0:
                    return max_icecream - 1
        return max_icecream
