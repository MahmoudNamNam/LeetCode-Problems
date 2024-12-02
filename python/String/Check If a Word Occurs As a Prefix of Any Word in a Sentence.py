class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        idx=1
        for word in words:
            if word.startswith(searchWord):
                return idx
            idx+=1
        return -1
    
sol = Solution()
print(sol.isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg"))
print(sol.isPrefixOfWord(sentence = "this problem is an easy problem", searchWord = "pro"))
print(sol.isPrefixOfWord(sentence = "i am tired", searchWord = "you"))

