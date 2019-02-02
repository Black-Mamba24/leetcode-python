class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aa = a.split("+")
        bb = b.split("+")
        aa_shi = int(aa[0])
        aa_xu = int(aa[1][:-1])
        bb_shi = int(bb[0])
        bb_xu = int(bb[1][:-1])

        shi = aa_shi * bb_shi - aa_xu * bb_xu
        xu = aa_shi * bb_xu + bb_shi * aa_xu
        return str(shi) + '+' + str(xu) + 'i'

    def complexNumberMultiply(self, a, b):
        """
        strip可以带参数
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.strip("i").split("+")
        b = b.strip("i").split("+")
        a0, a1 = int(a[0]), int(a[1])
        b0, b1 = int(b[0]), int(b[1])
        return str(a0 * b0 - a1 * b1) + '+' + str(a0 * b1 + a1 * b0) + 'i'


s = Solution()
print(s.complexNumberMultiply("1+-1i", "1+-1i"))
