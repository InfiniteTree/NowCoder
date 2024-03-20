'''
题目描述：
给定一组数字，表示扑克牌的牌面数字，忽略扑克牌的花色，请按如下规则对这一组扑克牌进
行整理：
步骤1、对扑克牌进行分组，形成组合牌，规则如下：
当牌面数字相同张数大于等于4 时，组合牌为“炸弹”；
3 张相同牌面数字+ 2 张相同牌面数字，且3 张牌与2 张牌不相同时，组合牌为“葫芦”；
3 张相同牌面数字，组合牌为“三张”；
2 张相同牌面数字，组合牌为“对子”；
剩余没有相同的牌，则为“单张”；
步骤2、对上述组合牌进行由大到小排列，规则如下：
不同类型组合牌之间由大到小排列规则：“炸弹” > "葫芦" > "三张" > "对子" > “单张”；
相同类型组合牌之间，除“葫芦”外，按组合牌全部牌面数字加总由大到小排列；
“葫芦”则先按3 张相同牌面数字加总由大到小排列，3 张相同牌面数字加总相同时，再按另
外2 张牌面数字加总由大到小排列；
由于“葫芦”>“三张”，因此如果能形成更大的组合牌，也可以将“三张”拆分为2 张和1
张，其中的2 张可以和其它“三张”重新组合成“葫芦”，剩下的1 张为“单张”
步骤3、当存在多个可能组合方案时，按如下规则排序取最大的一个组合方案：
依次对组合方案中的组合牌进行大小比较，规则同上；
当组合方案A 中的第n 个组合牌大于组合方案B 中的第n 个组合牌时，组合方案A 大于组合方
案B；
输入描述：
第一行为空格分隔的N 个正整数，每个整数取值范围[1,13]，N 的取值范围[1,1000]
输出描述：
经重新排列后的扑克牌数字列表，每个数字以空格分隔
'''
import sys

class solution():
    def problem(self, listN):
        hashmap = [0] * 13
        for poke in listN:
            hashmap[poke-1] += 1

        res = []
        gound = []
        bomb = []
        triple = []
        double = []
        single = []
        for i in range(len(hashmap)):
            while hashmap[i] >= 4:
                bomb.append(i)
                hashmap[i] -= 4
            if  hashmap[i] == 3:
                triple.append(i)
                hashmap[i] -= 3
            elif  hashmap[i] == 2:
                double.append(i)
                hashmap[i] -= 2
            elif hashmap[i] == 1:
                single.append(i)
                hashmap[i] -= 1
        
        # sorting not reverse for easy poping
        bomb.sort()
        triple.sort()
        double.sort()
        
        # build up gound
        while triple and double:
            gound.append([triple[-1],double[-1]])
            triple.pop()
            double.pop()
        while len(triple) >= 2:
            gound.append([triple[-1],triple[-2]])
            triple.pop()
            triple.pop()
            single.append(triple[-1])
        
        single.sort()

        # build up the return list
        for i in range(len(bomb)-1, -1,- 1):
            for _ in range(4):
                res.append(bomb[i]+1)
        
        for i in range(len(gound)): # not reverse due to the procedure of build it
            for _ in range(3):
                res.append(gound[i][0]+1)
            for _ in range(2):
                res.append(gound[i][1]+1)
        
        for i in range(len(triple)-1, -1,- 1):
            for _ in range(3):
                res.append(triple[i]+1)
        
        for i in range(len(double)-1, -1,- 1):
            for _ in range(2):
                res.append(double[i]+1)
        
        for i in range(len(single)-1, -1,- 1):
            res.append(single[i]+1)
        
        print(res)
        return res


case = solution()
for line in sys.stdin:
    input = list((line.split()))
    N = [int(x) for x in input]
    #print(N)
    break
#N = [9, 9, 9, 8, 8, 8, 7, 9, 8, 8, 8, 8, 8, 8, 7, 2, 13, 12, 11, 6, 6, 6, 7, 5, 4, 7, 6, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
case.problem(N)
