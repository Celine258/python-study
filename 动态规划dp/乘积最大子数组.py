class Solution:
    def FindMPS(self, nums: list[int]):#Maximum Product Subarray
        f = [0] * len(nums)#f[i]为从nums[0]到nums[i]连续子序列的乘积最大值
        d = [0] * len(nums)#d[i]为从nums[0]到nums[i]连续子序列的乘积最小值
        n = len(nums)
        f[0] = nums[0]
        d[0] = nums[0]
        for i in range(1, n):
            f[i] = nums[i]
            d[i] = nums[i]
            f[i] = max(max(nums[i], f[i-1]*nums[i]), d[i-1]*nums[i])
            d[i] = min(min(nums[i], f[i-1]*nums[i]), d[i-1]*nums[i])

        return max(f)

nums = [2, 3, 3, -8, -3]
solution = Solution()
n = solution.FindMPS(nums)
print(n)

#最大的问题是怎么解决负数的问题
        