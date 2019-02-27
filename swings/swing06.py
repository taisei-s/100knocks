# coding:utf-8

def ngram(str, n):
    ngram = []
    for i in range(n, len(str)+1):
        ngram.append(str[i-n:i])

    return ngram


def swing06(str1, str2):
    X = set(ngram(str1, 2))
    Y = set(ngram(str2, 2))
    Z = set(['se'])

    answer_list = [X|Y,  X&Y, X-Y, Z<=X, Z<=Y]

    return answer_list




if __name__ == "__main__":
    str1 = "paraparaparadise"
    str2 = "paragraph"
    print(swing06(str1, str2))