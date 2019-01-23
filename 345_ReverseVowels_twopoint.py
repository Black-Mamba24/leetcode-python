class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l, r = 0, len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u'}
        array = list(s)
        while l < r:
            while l < r and array[l].lower() not in vowels:
                l += 1
            while l < r and array[r].lower() not in vowels:
                r -= 1
            if l < r:
                array[l], array[r] = array[r], array[l]
                l += 1
                r -= 1
        return ''.join(array)


s = Solution()
print(s.reverseVowels("aA"))
