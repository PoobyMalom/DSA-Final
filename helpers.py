def floorpoweroftwo(x):
    x = x | (x >> 1)
    x = x | (x >> 2)
    x = x | (x >> 4)
    x = x | (x >> 8)
    x = x | (x >> 16)
    x = x | (x >> 32)
    return x - (x >> 1)


def reverse(array, range):
    temp = array[range.start:range.stop+1]
    temp.reverse()
    array[range.start:range.stop+1] = temp


def rotate(array, ammount, r):
    reverse(array, r)
    reverse(array, range(r.start, r.start + ammount))
    reverse(array, range(r.start + ammount, r.stop))


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]


def block_swap(array, A, B):
    rotate(array)
