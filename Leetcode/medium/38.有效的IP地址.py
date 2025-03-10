# -*- coding: utf-8 -*-

"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
"""


def restoreIpAddresses(s):
    res = []
    n = len(s)

    def backtrack(i, tmp, flag):
        if i == n and flag == 0:
            res.append(tmp[:-1])
            return
        if flag < 0:
            return
        for j in range(i, i + 3):
            if j < n:
                if i == j and s[j] == "0":
                    backtrack(j + 1, tmp + s[j] + ".", flag - 1)
                    break
                if 0 < int(s[i:j + 1]) <= 255:
                    backtrack(j + 1, tmp + s[i:j + 1] + ".", flag - 1)

    backtrack(0, "", 4)
    return res


# s = "25525511135"
# print(restoreIpAddresses(s))

def square_root_1(c):
    g = c/2
    while abs(g**3 - c) > 0.00000000001:
        g = (2*g)/3 + c/(3*(g**2))  #此为开三次方根的公式
    return round(g)


print(square_root_1(27))

