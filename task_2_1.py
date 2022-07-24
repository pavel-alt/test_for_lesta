class Item:
    def __init__(self, value, nextElement, previousElement):
        self.value = value
        self.previousElement = previousElement if previousElement else self
        self.nextElement = nextElement if nextElement else self


class CycleBuffer:
    def __init__(self, size):
        self.size = size
        self.firstElement = None
        self.lastElement = None
        self.count = 0

    def add(self, value):
        """ Adding an element to the buffer. """
        if self.count == self.size:
            self.__delete()
        newElement = Item(value=value, nextElement=self.lastElement, previousElement=self.firstElement)
        if self.lastElement:
            self.lastElement.previousElement = newElement
        if not self.firstElement:
            self.firstElement = newElement
        self.lastElement = newElement
        self.count += 1

    def __delete(self):
        self.firstElement = self.firstElement.previousElement
        self.firstElement.nextElement = self.lastElement
        self.count -= 1

    def useElement(self):
        """ Removes an element and returns its value. """
        value = self.firstElement.value
        self.__delete()
        return value
