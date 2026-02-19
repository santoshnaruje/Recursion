class Solution:
    def quick_sort(self, nums, left, right):
        if left < right:
            partition_index = self.get_partition(nums, left, right)
            self.quick_sort(nums, left, partition_index - 1)
            self.quick_sort(nums, partition_index + 1, right)

    def get_partition(self, nums, left, right):
        pivot = nums[left]
        low = left + 1

        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1

        # place pivot in correct position
        nums[left], nums[low - 1] = nums[low - 1], nums[left]

        return low - 1


if __name__ == '__main__':
    nums = [10, 7, 8, 9, 1, 5]
    solution = Solution()
    solution.quick_sort(nums, 0, len(nums) - 1)
    print(nums)