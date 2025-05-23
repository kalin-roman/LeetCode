
haystack = 'leetocode'
needle = 'leeto'

def strStr(haystack: str, needle: str) -> int:
    i = 0
    while needle[0] in haystack:
        i = haystack.index(needle[0],i)
        if haystack[i:i + len(needle)] == needle:
            return i
        i += 1
    return -1

def strStr1(haystack: str, needle: str) -> int:
    return haystack.find(needle)

print(strStr1(haystack,needle))

