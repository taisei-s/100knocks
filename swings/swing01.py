# coding:utf-8
"""
01. 「パタトクカシーー」

「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""

def swing01(str):
    return str[:7:2]


if __name__ == "__main__":
    str = u'パタトクカシーー'
    print(swing01(str))