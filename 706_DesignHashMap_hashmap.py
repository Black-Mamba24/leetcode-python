class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 10000
        self.array = [None] * 10000

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key % self.length
        if self.array[index] is None:
            l = [Item(key, value)]
            self.array.insert(index, l)
        else:
            for item in self.array[index]:
               if item.key == key:
                    item.value = value
                    break
            self.array[index].append(Item(key, value))


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.length
        if self.array[index] is None:
            return -1
        else:
            for item in self.array[index]:
                if item.key == key:
                    return item.value
            return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.length
        list = self.array[index]
        if list:
            for i, item in enumerate(list):
                if item.key == key:
                    list.pop(i)
                    self.array[index] = list

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

hashmap = MyHashMap()
hashmap.put(2,2)
hashmap.put(2,1)
hashmap.remove(2)
print(hashmap.get(2))