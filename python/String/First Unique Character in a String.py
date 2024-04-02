def firstUniqChar(s: str):
    arr = [0] * 26
    for i in range(len(s)):
        index = ord(s[i].lower()) - 97
        if arr[index] == 0:
            arr[index] = 1
        else:
            arr[index] += 1
    for i in range(len(s)):
        index = ord(s[i].lower()) - 97
        if arr[index] == 1:
            return i
    
    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))


# another sol


def firstUniqChar(s: str) -> int:
    key = 'abcdefghijklmnopqrstuvwxyz'
    idx = 10**5
    for i in key:
        x = s.find(i)
        if x != -1 and x == s.rfind(i):
            idx = min(idx,x)
    return idx if idx != 10**5 else -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))