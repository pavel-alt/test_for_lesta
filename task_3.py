from random import shuffle, choice
from time import clock


def timeManager(func):
    """ Decorator that calculates the running time of a function """
    def timer(*args, **kwargs):
        start = clock()
        result = func(*args, **kwargs)
        end = clock()
        print end - start
        return result

    return timer


def quickSort(lst_obj):
    """
    1. Select an element from an array. Let's call it base.
    2. Splitting: rearranging the elements in an array so that elements less than the pivot are placed before it,
       and those greater than or equal to it are placed after it.
    3. Recursively apply the first two steps to the two subarrays to the left and right of the pivot. Recursion
       does not apply to an array that has only one element or no elements.
    """
    if len(lst_obj) <= 1:
        return lst_obj
    else:
        q = choice(lst_obj)
        L = []
        M = []
        R = []
        for elem in lst_obj:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return quickSort(L) + M + quickSort(R)


@timeManager
def main(func, array):
    func(array)


if __name__ == "__main__":
    originalList1 = range(10000)
    shuffle(originalList1)
    originalList2 = range(1000000)
    shuffle(originalList2)
    originalList3 = range(2000000)
    shuffle(originalList3)
    originalList4 = range(2000000)

    print "Unsorted lists:"
    main(quickSort, originalList1)
    main(quickSort, originalList2)
    main(quickSort, originalList3)
    print "Sorted list:"
    main(quickSort, originalList4)
