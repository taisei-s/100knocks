# coding:utf-8

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