import algorithm.subsequence

if __name__ == '__main__':
    a = [1, 2, 3]
    print 'ori-sequence:', a, 'len:', len(a)
    print 'sub-sequence:', algorithm.subsequence.find_all(a), 'len:', len(algorithm.subsequence.find_all(a))
