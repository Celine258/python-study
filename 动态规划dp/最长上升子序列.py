class Solution:
    def FindLIS(self, nums: list[int]):
        #找出状态:f[i]表示以i为结束的nums[i]数组中最长上升子序列的长度
        #状态表达:f[i],找1到i-1之间比nums[i]小的数，然后对他们的LIS+1
        f = [1] * len(nums)

        n = len(nums)
        for i in range(0, n-1):
            a = []
            for j in range(0, i):
                if nums[j] < nums[i]:
                    a.append(f[j])
            if not a:
                continue
            f[i] += max(a)
        return max(f)


nums = [2, 5, 3, 4, 1, 7, 6]
solution = Solution()
n = solution.FindLIS(nums)
print(n)