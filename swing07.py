# coding:utf-8

def swing07(x, y, z):
    return unicode(x) + u"時の" + unicode(y) + u"は" + unicode(z)


if __name__ == "__main__":
    x = 12
    y = u"気温"
    z = 22.4
    print(swing07(x, y, z))