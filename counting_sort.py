from collections import Counter

def counting_sort(array1):

    hist = Counter(array1)
    hist = sorted(hist.items())

    i = 0
    for key, value in hist:
        for _ in range(value):
            array1[i] = key
            i += 1

    return array1

print(counting_sort( [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1]))