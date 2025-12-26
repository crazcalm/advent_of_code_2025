import fileinput
from collections import Counter

def get_num_of_parts(data):
    counter = Counter(data)
    values = list(counter.items())
    sorted_values = sorted(values, key=lambda value: value[1])
    num_of_parts = sorted_values[0][1]
    if num_of_parts == 1:
        return len(data)
    return num_of_parts
    

class StringParts:
    def __init__(self, data, num_of_parts):
        self.data = data
        self.index = -1
        self.num_of_parts = num_of_parts
        self.seq = len(data) // num_of_parts

    def __iter__(self):
        return self

    def __next__(self):
        result= ""
        for _ in range(self.seq):
            self.index += 1
            if result and self.index >= len(self.data):
                return result
            elif self.index>= len(self.data):
                raise StopIteration
            else:
                result += self.data[self.index]
        return result

def has_repeats(data, parts):
    result = True
    data_iter = StringParts(data, parts)

    part_1 = next(data_iter)

    # single digits
    if part_1 == data:
        return False
    
    for part in data_iter:
        if part_1 != part:
            result = False
            break
    return result

def invalid_id3(raw_data):
    data = str(raw_data)
    for parts in range(get_num_of_parts(data), 1, -1):
        if len(data) // parts == len(data) / parts:
            #print(f"Factor -- {parts}")
            result = has_repeats(data, parts)
            if result == True:
                return True
    return False

    
def invalid_id2(raw_data):
    data = str(raw_data)
    for parts in range(len(data), 1, -1):
        if len(data) // parts == len(data) / parts:
            #print(f"Factor -- {parts}")
            result = has_repeats(data, parts)
            if result == True:
                return True
    return False

def invalid_id(raw_data):
    """
    This fails for cases like 33773377 and 10011001 because the number of parts returned is 4, but that would
    give us 33,77,33,77 which would be false. We need this broken into 2 parts instead.
    """
    data = str(raw_data)
    parts = get_num_of_parts(data)

    result = True
    data_iter = StringParts(data, parts)

    part_1 = next(data_iter)

    # single digits
    if part_1 == data:
        return False
    
    for part in data_iter:
        if part_1 != part:
            result = False
            break
    return result

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

def main(check_func):
    count = 0
    for line in fileinput.input():
        if line == "\n":
            break
        
        for ranges in line.split(","):
            start, stop = ranges.split("-")

            for ids in InvalidIds(int(start), int(stop), checks=[check_func]):
                #print(ids)
                count += ids

    print(count)
    

    
if __name__ == "__main__":
    main(invalid_id2)
    
