# coding=utf-8
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for word in s.split(" "):
            res += word[::-1] #start:end:step，翻转一个字符串
            res += ""
        return res[:-1]

        # 最优解，先全部翻转，再分割，word顺序再反转，并用join拼接为字符串
        # return " ".join(s[::-1].split(" ")[::-1])