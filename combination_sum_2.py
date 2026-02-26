class Solution:
    def get_combination(self, nums, target):
        nums.sort()
        result = []

        def get_backtrack(index, remaining, path):

            if remaining == 0:
                result.append(path.copy())
                return

            if index == len(nums) or remaining < 0:
                return

            path.append(nums[index])
            get_backtrack(index + 1, remaining - nums[index], path)
            path.pop()

            next_index = index + 1

            while next_index < len(nums) and nums[next_index] == nums[index]:
                next_index += 1

            get_backtrack(next_index, remaining, path)

        get_backtrack(0, target, [])
        return result

    def get_combination_using_for_loop_backtrack(self,nums,remaining):
        nums.sort()
        result = []

        def get_backtrack(start, remaining, path):

            if remaining == 0:
                result.append(path.copy())
                return

            if start == len(nums) or remaining < 0:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    continue
                path.append(nums[i])
                get_backtrack(i+1, remaining - nums[i], path)
                path.pop()

        get_backtrack(0, remaining, [])
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    #
    # nums = [1, 2]
    # target = 50

    print(solution.get_combination_using_for_loop_backtrack(nums, target))
