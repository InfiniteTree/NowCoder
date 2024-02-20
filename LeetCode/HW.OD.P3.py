'''
题目描述：
现需要实现一种算法，能将一组压缩字符串还原成原始字符串，还原规则如下：
1、字符后面加数字N，表示重复字符N 次。例如：压缩内容为A3，表示原始字符串为AAA。
2、花括号中的字符串加数字N，表示花括号中的字符串重复N 次。例如：压缩内容为{AB}3，
表示原始字符串为ABABAB。
3、字符加N 和花括号后面加N，支持任意的嵌套，包括互相嵌套。例如：压缩内容可以
{A3B1{C}3}3。
输入描述：
输入一行压缩后的字符串
输出描述：
输出压缩前的字符串
补充说明：
输入保证，数字不会为0，花括号中的内容不会为空，保证输入的都是合法有效的压缩字符串
输入输出字符串区分大小写
输入的字符串长度为范围[1, 10000]
输出的字符串长度为范围[1, 100000]
数字N 范围[1, 10000]
'''
class Solution:
    def findEncodedString(self, string_t):
        #ret = ""
        str_stack = []
        digit_stack = []
        idxs = [] # record the location of "{" stored in str_stack
        string_t += " "
        for i in range(len(string_t)):
            char = string_t[i]
            if char.isdigit():
                digit_stack.append(char)
                continue # to store the next digit of num

            if digit_stack: # Judge whether the digit stack is empty
                num = int("".join(digit_stack)) 
                digit_stack = [] # make the digit stack empty
                top = str_stack.pop()

                if top == "}": # need to find the previous "{"
                    start = idxs.pop()
                    seq = "".join(str_stack[start+1:]) # a serious of sequences by chars
                    str_stack = str_stack[:start]
                    str_stack.append(seq * num)
                else:
                    str_stack.append(top * num)

            if char == "{":
                idxs.append(len(str_stack))
            
            str_stack.append(char) # add alpha char or "{","}"to ths string stack

        ret = "".join(str_stack).strip()
        print(ret)
        
        return ret


case = Solution()
s = "{A3B1{AC}3}3"
case.findEncodedString(s)
