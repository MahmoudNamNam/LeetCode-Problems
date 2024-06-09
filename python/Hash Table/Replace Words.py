from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        
        words = sentence.split()
        
        for i in range(len(words)):
            for root in dictionary:
                if words[i].startswith(root):
                    words[i] = root
                    break
        
        return ' '.join(words)


sol=Solution()
# Example usage
dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(sol.replaceWords(dictionary, sentence))  # Output: "the cat was rat by the bat"

dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"
print(sol.replaceWords(dictionary, sentence))  # Output: "a a b c"