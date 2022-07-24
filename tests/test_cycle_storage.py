import pytest

from task_2_2 import CycleStorage

testCycleStorage = CycleStorage(5)


@pytest.mark.parametrize("newElement", ("first", "second", "third", "fourth", "fifth", "sixth"))
def testLastElement(newElement):
    testCycleStorage.add(newElement)
    assert testCycleStorage.storage[-1] == newElement, \
        "Not correct last element value. Expected {}, actual {}".format(newElement, testCycleStorage.storage[-1])


@pytest.mark.parametrize("expectedValue", ("second", "third", "fourth", "fifth", "sixth"))
def testUseElement(expectedValue):
    actualValue = testCycleStorage.useElement()
    assert actualValue == expectedValue, \
        "Not correct used element value. Expected {}, actual {}".format(expectedValue, actualValue)
