def isSubSet(s1, s2):
    """s1是否为s2的子集"""
    return s1.issubset(s2)


def isSuperSet(s1, s2):
    """s1是否为s2的超集"""
    return s1.issuperset(s2)


s1 = {1, 2, 3}
s2 = {1, 2, 3, 4}
print(isSubSet(s1, s2))
print(isSuperSet(s1, s2))
