# coding:utf-8

def ngram(str, n):
    ngram = []
    for i in range(n, len(str)+1):
        ngram.append(str[i-n:i])

    return ngram

def word_ngram(str, n):
    word_list = [c.strip(',.') for c in str.split()]
    word_ngram = ngram(word_list, n)

    return word_ngram

def swing05(str):
    word_bigram = word_ngram(str, 2)
    character_bigram = ngram(str, 2)

    return word_bigram, character_bigram




if __name__ == "__main__":
    str = "I am an NLPer"
    word_bigram, character_bigram = swing05(str)

    print(word_bigram)
    print(character_bigram)