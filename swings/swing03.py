# coding:utf-8

def swing03(str):
    return [len(word.strip(".,")) for word in str.split()]


if __name__ == "__main__":
    pass