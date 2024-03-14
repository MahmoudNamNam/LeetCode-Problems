def isIsomorphic(s, t):
    """Check if two strings s and t are isomorphic.

    Two strings are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving 
    the order of characters. No two characters may map to the same character but a character may 
    map to itself.

    Args:
        s (str): The first string.
        t (str): The second string.

    Returns:
        bool: True if s and t are isomorphic, False otherwise.
    """
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        if char_s not in s_to_t and char_t not in t_to_s:
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
        elif s_to_t.get(char_s) != char_t or t_to_s.get(char_t) != char_s:
            return False
    
    return True


s = "egg"
t = "add"
print(isIsomorphic(s,t))
'''
Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

'''