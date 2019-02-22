# coding:utf-8

import random

def shuffle_inside(word):
    if len(word) <= 4:
        return word

    inside = list(word[1:-1])
    random.shuffle(inside)
    new_word = word[0] + ''.join(inside) + word[-1]

    return new_word



def swing09(str):
    word_list = str.split()
    shuffled = ' '.join([shuffle_inside(word) for word in word_list])

    return shuffled


if __name__ == "__main__":
    str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(swing09(str))