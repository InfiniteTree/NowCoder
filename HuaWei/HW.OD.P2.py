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
class solution():
    def problem(self, listN):
        ret = []
        mark = 0
        for i in range(len(listN)-1):
            if listN[i] == listN[i+1]:        
        return ret

case = solution()
N = []
N.sort(reverse=True)
case.problem(N)