from algorithm.subsequence import find_subsequence

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print 'ori-sequence:', a, 'len:', len(a)
    print 'sub-sequence:', find_subsequence(a), 'len:', len(find_subsequence(a))
