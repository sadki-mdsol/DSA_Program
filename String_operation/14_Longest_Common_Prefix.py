def longestCommonPrefix(strs):
    res =""
    for i in range(len(strs[0])):
        for s in strs:
            if len(s)==i or strs[0][i] != s[i]:
                return res
        res += strs[0][i]

    # return res


str = ['flowers','flow','flight']

print(longestCommonPrefix(str))