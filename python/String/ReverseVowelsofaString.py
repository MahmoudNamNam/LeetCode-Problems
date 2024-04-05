class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j = len(s)-1
        vowel = {'a', 'e', 'i', 'o', 'u','A','E','I','O','U'}
        res = list(s)
        
        while i < j:
            if res[i] not in vowel:
                i += 1
            elif res[j] not in vowel:
                j -= 1
            else:
                # Swap the characters
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
                
        return "".join(res)