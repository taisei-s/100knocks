# coding:utf-8

def swing01(str):
    """
    assume str is string coding utf-8
    return string on 1,3,5,7 of str
    """
    return str[:7:2]


if __name__ == "__main__":
    str = u'パタトクカシーー'
    print(swing01(str))