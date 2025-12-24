class Range:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def in_range(self, num):
        return num >= self.lower and num <= self.upper

    def __lt__(self, other):
        return self.lower < other.lower
    
class Ranges:
    def __init__(self):
        self.ranges = []
        self.index = 0
        self.value = None

    def __iter__(self):
        self.sort()
        return self

    def __next__(self):
        if self.value == None:
            self.value = self.ranges[self.index].lower
            return self.value
        
        while True:
            if self.index >= len(self.ranges):
                raise StopIteration

            self.value += 1


            if self.value < self.ranges[self.index].lower:
                self.value = self.ranges[self.index].lower
                break

            elif self.value > self.ranges[self.index].upper:
                print(f"last upper --> {self.ranges[self.index].upper}")
                self.index += 1
                self.value -= 1  # to counter balance the extra add one
                continue
            else:
                # returning the value
                break

        return self.value
        
    def sort(self):
        self.ranges.sort()
        
    def add_range(self, lower, upper):
        self.ranges.append(Range(lower, upper))
        
    def in_range(self, num):
        result = False
        for range_ in self.ranges:
            if range_.in_range(num):
                result = True
                break
        return result


if __name__ == "__main__":
    import fileinput

    ranges = Ranges()
    count = 0

    for line in fileinput.input():
        line = line.strip()

        if not line:
            break

        lower, upper = line.split("-")
        ranges.add_range(int(lower), int(upper))

    for num in ranges:
        #print(num)
        count += 1

    print(f"count is -> {count}")
