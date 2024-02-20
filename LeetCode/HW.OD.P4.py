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
t_w = [] # t/w represent the average income rate of each job
i = 0
for line in sys.stdin:
    # For the first input line, record the num of original cases
    if case_flag == 0: 
        T, n = int(line.split()[0]), int(line.split()[1])
        case_flag = 1
        continue
    t_w.append((float(line.split()[1])/float(line.split()[0]), float(line.split()[0]),float(line.split()[1]), i))
    i+=1
    if i == n: #input done
        break
    
t_w.sort(key=lambda x:(x[0],x[1]), reverse=True)
print(t_w)

# Calculate the max income
worked = 0
income = 0
idx = 0
while(idx<n):
    if worked+t_w[idx][1] < T:
        worked+=t_w[idx][1]
        income+=t_w[idx][2]
    idx+=1
print(income)

    
    
















    