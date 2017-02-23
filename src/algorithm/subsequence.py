# coding=utf-8


def find_all(seq):
    """ 查找子序列. """
    res = []
    seq_len = len(seq)
    for i in range(seq_len):
        sub_seq_len = i + 1
        for j in range(seq_len - sub_seq_len + 1):
            res.append(seq[j:j + sub_seq_len])

    return res
