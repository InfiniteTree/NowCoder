import sys

case_flag = 0
ret = []
for line in sys.stdin:
    # For the first input line, record the num of original cases
    if case_flag == 0: 
        #numInt = line.split()[0]
        case_flag = 1
        continue
    item = int(line.split()[0])
    if item not in ret:
        ret.append(item)
ret.sort()
#print(ret)
for i in range(len(ret)):
    print(ret[i])