# coding:utf-8
"""
13. col1.txtとcol2.txtをマージ

12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

command:
$paste col1.txt col2.txt
"""

import sys

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def swing13():
    #filenames = sys.argv[1:]
    filenames = ['', 'col1.txt', 'col2.txt']

    with open(filenames[1], 'r') as f:
        col1 = f.readlines()
    with open(filenames[2], 'r') as f:
        col2 = f.readlines()

    col12 = ''
    for col1_, col2_ in zip(col1, col2):
        col12 += col1_.strip() + '\t' + col2_

    write_file("col1_2.txt", col12)


if __name__ == "__main__":
    swing13()