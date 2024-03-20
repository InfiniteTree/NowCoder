'''
机考真题1
给你一个整数M 和数组N, N 中的元素为连续整数
要求根据N 中的元素组装成新的数组R
组装规则
1.R 中元素总和加起来等于M
2.R 中的元素可以从N 中重复选取
3.R 中的元素最多只能有1 个不在N 中
且比N 中的数字都要小（不能为负数）
请输出 数组R 一共有多少组装办法
输入描述 第一行输入是连续数组N 采用空格分隔 第二行输入数字M
输出描述 输出的是组装办法数量 int 类型
补充说明 1 <= N.length <= 30 1 <= N.length <= 1000
'''
class solution:
    def sol(self, N, M):
        N.sort()
        N_min = N[0]
        
        def backtrack(count, arrayN, target, index):
            # Base case
            if target < 0:
                return
            if target == 0 or 0<target<N_min:
                count[0] += 1
                return
            # Recursion
            for i in range(index, len(arrayN)):
                backtrack(count, arrayN, target-arrayN[i], i)
                
        count = [0]  
        backtrack(count, N, M, 0)
        print(count[0])
        return

# Test
case = solution()
N = [3,7,4,10,8]
M = 10
case.sol(N, M)


