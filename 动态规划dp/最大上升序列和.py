class Solution:
    def FindMSIS(self, nums: list[int]):
        if not nums:
            return 0
        #跟LIS类似
        f = [0] * len(nums)
        n = len(nums)
        for i in range(0, n):
            f[i] = nums[i]
            #sum = [] 这个list可以通过max函数来省略掉
            for j in range(0, i):
            #     if nums[j] < nums[i]:
            #         sum.append(f[j])
            # if not sum:
            #     continue
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j] + nums[i])
            # f[i] += max(sum)
        return max(f)

nums = [1, 7, 3, 5, 9, 4, 8]
solution = Solution()
n = solution.FindMSIS(nums)
print(n)