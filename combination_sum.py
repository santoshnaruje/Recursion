class Solution:
    def get_combination(self, nums, index, target, result):

        if target == 0:
            return [result.copy()]

        if target < 0 or len(nums) == index:
            return []

        result.append(nums[index])
        left = self.get_combination(nums, index , target-nums[index], result)
        result.pop()
        right = self.get_combination(nums, index + 1, target, result)

        return left + right


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 6, 7]
    target = 7
    current_sum = 0
    print(solution.get_combination(nums, 0, target,[]))
