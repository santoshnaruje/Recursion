class Solution:

    def merge_sort_returning_array(self, nums, left, right):

        def merge(left_sorted, right_sorted):

            merged_nums = []

            left = 0
            right = 0

            while left < len(left_sorted) and right < len(right_sorted):
                if left_sorted[left] < right_sorted[right]:
                    merged_nums.append(left_sorted[left])
                    left += 1
                else:
                    merged_nums.append(right_sorted[right])
                    right += 1

            while left < len(left_sorted):
                merged_nums.append(left_sorted[left])
                left += 1

            while right < len(right_sorted):
                merged_nums.append(right_sorted[right])
                right += 1
            return merged_nums

        if left > right:
            return []

        if left == right:
            return [nums[left]]

        mid = (left + right) // 2
        left_sorted = self.merge_sort(nums, left, mid)
        right_sorted = self.merge_sort(nums, mid + 1, right)
        merged = merge(left_sorted, right_sorted)
        return merged

    def merge_sort_in_place(self, nums, left, right):

        def merge(nums, left, mid, right):

            result = []
            low = left
            high = mid+1

            while low <= mid and high <= right:
                if nums[low] < nums[high]:
                    result.append(nums[low])
                    low+=1
                else:
                    result.append(nums[high])
                    high+=1

            while low <= mid:
                result.append(nums[low])
                low+=1

            while high <= right:
                result.append(nums[high])
                high+=1

            for i in range(len(result)):
                nums[left+i] = result[i]

        if left >=right:
            return

        mid = left + (right - left) // 2
        self.merge_sort_in_place(nums, left, mid)
        self.merge_sort_in_place(nums, mid + 1, right)
        merge(nums,left,mid,right)

if __name__ == "__main__":
    nums = [4, 1, 3, 9, 7]
    sol = Solution()
    left = 0
    right = len(nums) - 1
    print(sol.merge_sort_in_place(nums, left, right))
    print(nums)
