# coding:utf-8

def swing02(str1, str2):
    return ''.join(c1 + c2 for c1, c2 in zip(str1, str2))


if __name__ == "__main__":
    str1 = u'パトカー'
    str2 = u'タクシー'
    print(swing02(str1, str2))