# coding:utf-8

def swing03(str):
    """
    assume str is string.
    return list with number of word's characters
    """
    return [len(word.strip(".,")) for word in str.split()]


if __name__ == "__main__":
    pass