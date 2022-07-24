import pytest

from task_3 import quickSort


@pytest.mark.parametrize("unsortList, sortList", (([1, 7, 2, 8, 3, 9, 6, 4, 5, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                                                 ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))
def testquickSort(unsortList, sortList):
    actualList = quickSort(unsortList)
    assert actualList == sortList, "Not correct sorted list. Expected {}, actual {}".format(sortList, actualList)
