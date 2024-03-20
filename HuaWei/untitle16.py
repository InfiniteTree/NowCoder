key = input()
boxes = input().split()
 
def getResult(key, boxes):
    for i in range(len(boxes)):
        box = boxes[i]
        tmp = list("".join(list(filter(lambda c: 'a' <= c <= 'z' or 'A' <= c <= 'Z', list(box)))).lower())
        tmp.sort()
 
        if key == "".join(tmp):
            return i+1
    return -1
 
print(getResult(key, boxes))