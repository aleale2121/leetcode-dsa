class Solution:
    def merge(self,left_list, right_list):
        left_cursor = right_cursor = 0
        ans = []
        while left_cursor < len(left_list) and right_cursor < len(right_list):
            if left_list[left_cursor] < right_list[right_cursor]:
                ans.append(left_list[left_cursor])
                left_cursor += 1
            else:
                ans.append(right_list[right_cursor])
                right_cursor += 1

        ans.extend(left_list[left_cursor:])
        ans.extend(right_list[right_cursor:])

        return ans

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = int(len(nums) / 2)
        left = self.sortArray(nums[0:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)