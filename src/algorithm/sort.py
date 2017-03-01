# coding=utf-8


def insertion_sort(seq):
    """ 插入排序 """
    for j in range(1, len(seq)):
        key = seq[j]
        i = j - 1
        while i >= 0 and seq[i] > key:
            seq[i + 1] = seq[i]
            i -= 1

        seq[i + 1] = key

    return seq
