# coding:utf-8
"""
11. タブをスペースに置換

タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

commnad:
$sed -e s/'\t'/' '/g hightemp.txt
$cat hightemp.txt | tr '\t' ' '
$expand -t 1 hightemp.txt
"""

import sys

def swing11():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        file = f.read()

    print(file.replace('\t', ' '))


if __name__ == "__main__":
    swing11()