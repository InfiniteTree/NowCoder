'''
小明有 n 块木板，第 i ( 1 ≤ i ≤ n ) 块木板长度为 ai。
小明买了一块长度为 m 的木料，这块木料可以切割成任意块，
拼接到已有的木板上，用来加长木板。
小明想让最短的木板尽量长。
请问小明加长木板后，最短木板的长度可以为多少？
输入描述:
输入的第一行包含两个正整数，n(1≤n≤10^3),m(1≤m≤10^6)
n表示木板数，m表示木板长度。输入的第二行包含n个正整数，a1,a2,...an(1≤ai≤10^6)。
输出描述
输出的唯一一行包含一个正整数，表示加长木板后，最短木板的长度最大可以为多少？
'''
import sys
flag = 0
for line in sys.stdin:
    if flag == 0 :
        n = int(line.split()[0])
        m = int(line.split()[1])
    woods = line.split()
    break
