import sys


def __doc__():
    return "自定义的 分页脚本"


def more(lines, limit):
    # print(type(lines), lines)
    while True:
        cur = lines[:limit]
        lines = lines[limit:]
        for line in cur:
            print(line.strip())
        if not lines or input('More?') not in ['y', 'Y']:
            break


more(open(sys.argv[1]).readlines(), int(sys.argv[2]))
