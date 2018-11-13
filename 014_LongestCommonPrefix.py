class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for index, c in enumerate(shortest):
            for str in strs:
                if str[index] != c:
                    return shortest[:index]
        return shortest

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["ggaaa", "ggggg"]))