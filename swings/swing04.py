# coding:utf-8
"""
04. 元素記号

"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

def swing04(str):
    word_list = [c.strip(',.') for c in str.split()]
    single = [0, 4, 5, 6, 7, 8, 14, 15, 18]
    element_dict ={}
    for i in range(len(word_list)):
        p = 1 if i in single else 2
        element_dict[word_list[i][:p]] = i + 1

    return element_dict


if __name__ == "__main__":
    str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    element_dict = swing04(str)
    for k, v in sorted(element_dict.items(), key=lambda x: x[1]):
        print(k, v)