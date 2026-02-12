class Solution:

    def __init__(self):
        self.ans = []

    def get_subsequence(self, nums, index, result):
        if index == len(nums):
            return [result.copy()]
        result.append(nums[index])
        left = self.get_subsequence(nums, index + 1, result)
        result.remove(nums[index])
        right = self.get_subsequence(nums, index + 1, result)
        return left + right


if __name__ == '__main__':
    nums = [3, 1, 2]
    sol = Solution()
    print(sol.get_subsequence(nums, 0, []))
