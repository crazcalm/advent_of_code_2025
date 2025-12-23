def starts_with_0(data):
    if data.startswith("0"):
        return True
    else:
        return False

def repeat_twice(num):
    data = str(num)
    half = len(data) // 2
    return data[:half] == data[half:]
    
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

if __name__ == "__main__":
    import fileinput

    count = 0
    for line in fileinput.input():
        if line == "\n":
            break
        
        for ranges in line.split(","):
            start, stop = ranges.split("-")

            for ids in InvalidIds(int(start), int(stop), checks=[repeat_twice]):
                print(ids)
                count += ids

    print(count)
    
