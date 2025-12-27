class InvalidIds:
    def __init__(self, start, end, checks=None):
        self.start = start
        self.current = start - 1
        self.end = end
        self.checks = checks if checks else []

    def invalid(self, value):
        result = False
        for check in self.checks:
            if check(value):
                result = True
                break
        return result
        
    def __iter__(self):
        return self

    def __next__(self):
        result = None
        while result is None:
            self.current += 1

            if self.current > self.end:
                raise StopIteration

            if self.invalid(self.current):
                result = self.current
            
        return self.current
