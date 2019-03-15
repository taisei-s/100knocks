# coding:utf-8
"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存

各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

import sys

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def swing12():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        fileLines = f.readlines()

    write_file("col1.txt", fileLines[0])
    write_file("col2.txt", fileLines[1])


if __name__ == "__main__":
    swing12()