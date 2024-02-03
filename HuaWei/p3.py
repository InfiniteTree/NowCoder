import sys

def transform(str_to_int):
    if str_to_int == "A":
        ret = 10
    elif str_to_int == "B":
        ret = 11
    elif str_to_int == "C":
        ret = 12
    elif str_to_int == "D":
        ret = 13
    elif str_to_int == "E":
        ret = 14
    elif str_to_int == "F":
        ret = 15
    else:
        ret = int(str_to_int)
    return ret

number = ''
for line in sys.stdin:
    number = line.split()[0]

ret = 0
for i in range(2, len(number)):
    # Switch case
    digit = transform(number[i])
    ret += digit * 16 ** (len(number)-i-1)
print(ret)