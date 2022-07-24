class CycleStorage:
    def __init__(self, size):
        self.size = size
        self.storage = []

    def add(self, value):
        """ Adding an element to the buffer. """
        if len(self.storage) == self.size:
            self.__delete()

        self.storage.append(value)

    def __delete(self, quantity=1):
        for _ in range(quantity):
            self.storage.pop(0)

    def useElement(self):
        """ Removes an element and returns its value. """
        value = self.storage[0]
        self.__delete()
        return value
