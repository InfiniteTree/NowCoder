import sys

case_flag = 0
numCase = 0
numOrig = 0 # Original empty bottle number
for line in sys.stdin:
    # For the first input line, record the num of original cases
    if case_flag == 0: 
        numCase = line.split()[0]
        case_flag = 1 
   
    a = line.split()
    numOrig = int(a[0])
    # For the last input line: finish
    if numOrig == 0:
        break
    ans = 0
    while numOrig >= 3:
        exchange = numOrig // 3
        remain = numOrig % 3
        ans += exchange
        numOrig = exchange + remain
    if numOrig == 2:
        ans += 1
    print(ans)
    #print(a)