# coding:utf-8
"""
07. テンプレートによる文生成

引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""

def swing07(x, y, z):
    return unicode(x) + u"時の" + unicode(y) + u"は" + unicode(z)


if __name__ == "__main__":
    x = 12
    y = u"気温"
    z = 22.4
    print(swing07(x, y, z))