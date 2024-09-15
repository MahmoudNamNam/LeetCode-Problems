class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []

        for i in range(len(path)):
            if path[i] == "" or path[i] == ".":
                continue
            elif path[i] == "..":
                if stack:
                    stack.pop(-1)
            else:
                stack.append(path[i])
        
        path = "/".join(stack)

        return "/"+path
            

sol = Solution()
print(sol.simplifyPath("/home/"))
print(sol.simplifyPath(path = "/home/user/Documents/../Pictures"))