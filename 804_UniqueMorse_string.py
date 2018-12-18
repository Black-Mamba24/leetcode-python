class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        方法一：列表法，计算偏移量
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set()
        for word in words:
            res = ""
            for w in word:
                mor = morse[ord(w) - ord("a")]
                res += mor
            s.add(res)

        return len(s)

    def uniqueMorseRepresentations2(self, words):
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        di = dict(zip("abcdefghijklmnopqrstuvwxyz", morse))
        s = set()
        for word in words:
            res = ""
            for w in word:
                res += di[w]
            s.add(res)
        return len(s)