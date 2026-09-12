class Solution:
    def FindMS(self, nums: list[int]):
        #数组f为第1个数到第i个数的MS
        f = [0] * len(nums)
        n = len(nums)
        for i in range(0, n):
            f[i] = nums[i]
            f[i] = max(f[i], f[i] + f[i-1])
        return max(f)

nums = [-2, 10, 8, -4, 7, 5, -29, 10]
s = Solution()
n = s.FindMS(nums)
print(n)