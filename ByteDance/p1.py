import sys 
points = []
ret = []
num = 0

for line in sys.stdin:
    a = line.split()
    if len(a) == 1:
        num = int(a[0])
    else:
        points.append((int(a[0]),int(a[1])))
#print(points)

points.sort(key=lambda x:x[1])
max_x = 0

for i in range(num - 1, -1, -1):
    if points[i][0] >= max_x:
        #ret.append((points[i][0], points[i][1]))
        print(f"{points[i][0]} {points[i][1]}")
        max_x = points[i][0]
        '''
        if points[i][0] - points[k][0] < 0 and points[i][1] - points[k][1] < 0:
            break
        '''
'''
ret.sort(key=lambda x:x[0])
#print(ret)
for i in ret:
    print(f"{i[0]} {i[1]}")
'''
        