# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = 100002
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum
                elif sum > target:
                    k-=1
                else:
                    j+=1
                closest = closest if abs(closest-target) < abs(sum - target) else sum
        return closest