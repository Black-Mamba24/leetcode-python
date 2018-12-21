def intersrction(s1, s2):
    """交集"""
    print(s1.intersection(s2))
    print(s1 & s2)


def union(s1, s2):
    """并集"""
    print(s1.union(s2))
    print(s1 | s2)


def difference(s1, s2):
    """差集"""
    print(s1.difference(s2))
    print(s1 - s2)


def symmetric_difference(s1, s2):
    """补集"""
    print(s1.symmetric_difference(s2))
    print(s1 ^ s2)


s1, s2 = {1, 2, 3}, {2, 3, 4}
intersrction(s1, s2)
union(s1, s2)
difference(s1, s2)
difference(s2, s1)
symmetric_difference(s1, s2)