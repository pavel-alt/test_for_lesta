import pytest

from task_2_1 import CycleBuffer

testCycleBuffer = CycleBuffer(5)


@pytest.mark.parametrize("newElement", ("first", "second", "third", "fourth", "fifth", "sixth"))
def testLastElement(newElement):
    testCycleBuffer.add(newElement)
    assert testCycleBuffer.lastElement.value == newElement, \
        "Not correct last element value. Expected {}, actual {}".format(newElement, testCycleBuffer.lastElement.value)


@pytest.mark.parametrize("expectedValue", ("second", "third", "fourth", "fifth", "sixth"))
def testUseElement(expectedValue):
    actualValue = testCycleBuffer.useElement()
    assert actualValue == expectedValue, \
        "Not correct used element value. Expected {}, actual {}".format(expectedValue, actualValue)
