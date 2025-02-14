# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        i = 0
        while i < len(nums):
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    answer.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    j+=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                else:
                    k-=1
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            i+=1
        return answer