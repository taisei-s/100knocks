# coding:utf-8

def swing02(str1, str2):
    """
    assume str1 and str2 is string coding utf-8, len(str1) == len(str2) is true
    return string alternately connected to str1 and str2 from the beginning
    """
    return ''.join(c1 + c2 for c1, c2 in zip(str1, str2))


if __name__ == "__main__":
    str1 = u'パトカー'
    str2 = u'タクシー'
    print(swing02(str1, str2))