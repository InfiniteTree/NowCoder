'''
题目描述：
小明每周上班都会拿到自己的工作清单，工作清单内包含n 项工作，每项工作都有对应的耗时
时长（单位h）和报酬，工作的总报酬为所有已完成工作的报酬之和。那么请你帮小明安排一
下工作，保证小明在指定的工作时间内工作收入最大化。
输入描述：
输入的第一行为两个正整数T，n。T 代表工作时长（单位h，0 < T < 100000），n 代表工作
数量(1 < n ≤ 3000)。
接下来是n 行，每行包含两个整数t，w。t 代表该项工作消耗的时长（单位h，t > 0），w 代
表该项工作的报酬。
输出描述：
输出小明指定工作时长内工作可获得的最大报酬。
'''
import sys

case_flag = 0
t, w = [], []
i = 0
for line in sys.stdin:
    # For the first input line, record the num of original cases
    if case_flag == 0: 
        T, n = int(line.split()[0]), int(line.split()[1])
        case_flag = 1
        continue
    t.append(int(line.split()[0]))
    w.append(float(line.split()[1]))
    i+=1
    if i == n: #input done
        break

dp = [0] * (T+1)
for i in range(len(t)):
    for j in range(T, t[i], -1):
        dp[j] = max(dp[j], dp[j-t[i]]+w[i])

print("Max income is", dp[-1])





    
    
















    