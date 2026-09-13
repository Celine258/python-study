#现在有n个地点可供选择，并且在一条线上，小明想在这些地方开餐馆用m[1]到m[n]表示餐馆的位置
#由于餐馆之间的距离和利润有关系，为了避免竞争，餐馆之间的距离必须大于k，用p来表示餐馆的利润

class Solution:
    def setRestraunt(self, n:int, m:list[int], p:list[int]):
        f = [0] * (n+1)#f[i]表示从1到i的最大利润
        #如果距离不对
        #f[i] = max(p[i], f[i-1])
        #如果距离对了
        #f[i] = f[i-1] + p[i]
        for i in range(1, n+1):
            f[i] = max(p[i], f[i-1])#但是首先得比较是否可以舍弃自身
            for j in range(1, i):
                if (m[i] - m[j]) >= k:
                    f[i] = max(f[j] + p[i], f[i])
        return max(f)




t = int(input("请输入要测试数据的组数(1 <= t <= 1000): "))
solution = Solution()
j = 1
while(t):
    n = int(input("请输入地点总数(1 < n < 100): ")) 
    k = int(input("请输入餐馆之间的距离限制(0 < k < 1000): "))
    m = [0] * (n + 1)
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        print("输入地点位置")
        m[i] = int(input(f"输入第{i}个餐馆位置(顺序排列): "))
    for i in range(1, n + 1):
        print("输入地点利润")
        p[i] = int(input(f"输入第{i}个餐馆利润: "))
    res = solution.setRestraunt(n, m, p)
    print(f"第{j}组数据的最大利润是:{res}RMB")
    j += 1
    t -= 1
    