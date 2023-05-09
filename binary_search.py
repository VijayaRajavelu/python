#Binary Search
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

#nums = [1, 3, 5, 7, 9]
#target = 5
result = Solution()
#print(result.search(nums, target))

print(result.search([-1,0,3,5,9,12],9))
