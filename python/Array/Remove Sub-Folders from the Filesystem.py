from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  
        result = []
        
        for sub in folder:
            # Only add the folder if it's not a subfolder of the last added one
            if not result or not sub.startswith(result[-1] + '/'):
                result.append(sub)
                
        return result


sol = Solution()
print(sol.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(sol.removeSubfolders(["/a","/a/b/c","/a/b/d"]))
print(sol.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))
