'''
题目描述：
某公司目前推出了AI 开发者套件、AI 加速卡、AI 加速模块、AI 服务器、智能边缘多种硬件产
品，每种产品包含若干个型号。现某合作厂商要采购金额为amount 元的硬件产品搭建自己的
AI 基座。假设当前库存有N 种产品，每种产品的库存量充足，给定每种产品的价格，记为price
（不存在价格相同的产品型号）。请为合作厂商列出所有可能的产品组合。
输入描述：
输入包含采购金额amount 和产品价格列表price。第一行为amount，第二行为price。例如：
500
[100, 200, 300, 500]
输出描述：
输出为组合列表。例如：
[[500], [200, 300], [100, 200, 200], [100, 100, 300], [100, 100, 100, 200], [100, 100,
100, 100, 100]]
补充说明：
1. 对于给定输入，产品组合少于150 种。输出的组合为一个数组，数组的每个元素也是一个
数组，表示一种组合方案。如果给定产品无法组合金额为amount 元的方案，那么返回空列表。
2. 两种组合方案，只要存在一种产品的数量不同，那么方案认为是不同的。
3. 每种产品型号价格不相同
4. 1 <= 产品类型数量<= 30
5. 100 <= 产品价格<= 20000
6. 100 <= 采购金额<= 50000
'''
import sys
comb = []
flag = 0
# input
for line in sys.stdin:
    if flag == 0:
        amount = float(line.split()[0])
        flag = 1
        continue
    price_str = line.split("\n")[0].strip("[]").split(",")
    break

# processing
price = list(map(int, price_str))
price.sort()

def dfs(amount, price, idx, sum, path, comb):
    if sum>=amount:
        if sum == amount:
            comb.append(path[:])
        return
    for i in range(idx, len(price)):
        path.append(price[i])
        dfs(amount, price, i, sum+price[i], path, comb)
        path.pop()


dfs(amount, price, 0, 0, [], comb)
print(comb)


    
