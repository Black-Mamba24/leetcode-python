def bubble(array):
    """
    :param array: 整型数组
    :return: 排序数组
    """
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                tmp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = tmp
    return array

if __name__ == '__main__':
    res = bubble([3,4,12,6,7,-2,1,4,3,1,0,431,32])
    print(res)