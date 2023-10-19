class my_islice_iterator():
    # Constructor
    def __init__(self, iterable, start, stop):
        self.iterable = iterable
        self.start = start
        self.stop = stop
        self.index = start
    # Iterator method
    def __iter__(self):
        return self
    # Next method
    def __next__(self):
        # Check if index exceeds range
        if (self.index >= self.stop or self.index >= len(self.iterable)):
            raise StopIteration
        # Update index 
        ans = self.index
        self.index += 1
        return self.iterable[ans]

def my_islice_generator(iterable, start, stop):
    # Checking length of iterable to the stopping value
    if stop <= len(iterable):
        # Returing value at index
        for i in range(start,stop):
            yield iterable[i]