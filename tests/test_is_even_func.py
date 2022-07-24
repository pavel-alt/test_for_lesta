import pytest
from task_1 import isEvenBitsAND, isEvenBitsSHIFT, isEvenExample


@pytest.mark.parametrize("testFunction, testData, expectedResult", ((isEvenBitsAND, 1, False),
                                                                    (isEvenBitsAND, 2, True),
                                                                    (isEvenBitsSHIFT, 1, False),
                                                                    (isEvenBitsSHIFT, 2, True),
                                                                    (isEvenExample, 1, False),
                                                                    (isEvenExample, 2, True)))
def testIsEvenFunction(testFunction, testData, expectedResult):
    actualResult = testFunction(testData)
    assert actualResult == expectedResult, \
        "For {} even expected: {}, actual {}".format(testData, expectedResult, actualResult)
