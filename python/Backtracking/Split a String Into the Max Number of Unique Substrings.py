class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n=len(s)
        def backtrack(start, seen):
            if start == n:
                return len(seen)  

            max_splits = 0
            for end in range(start + 1, n + 1):
                substring = s[start:end]
                if substring not in seen:  # Only consider the substring if it's unique
                    seen.add(substring)
                    # Recurse with the remaining part of the string
                    max_splits = max(max_splits, backtrack(end, seen))
                    # Backtrack by removing the substring
                    seen.remove(substring)

            return max_splits
        
        return backtrack(0, set())

    
sol =Solution()

print(sol.maxUniqueSplit( "ababccc"))
print(sol.maxUniqueSplit("aba"))
print(sol.maxUniqueSplit("aa"))
print(sol.maxUniqueSplit("llkcegedae"))