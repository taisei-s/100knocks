# coding:utf-8
"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存

各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

command:
$cut -f 1 hightemp.txt
$cut -f 2 hightemp.txt
"""

import sys

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def swing12():
    filename = sys.argv[1]
    col1 = ''
    col2 = ''
    with open(filename, 'r') as f:
        for line in f.readlines():
            col1 += line.split('\t')[0] + '\n'
            col2 += line.split('\t')[1] + '\n'

    write_file("col1.txt", col1)
    write_file("col2.txt", col2)


if __name__ == "__main__":
    swing12()