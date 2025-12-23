class Range:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.range_set = set(range(lower,upper + 1))

    def in_range(self, num):
        return num >= self.lower and num <= self.upper

class Ranges:
    def __init__(self):
        self.ranges = []
        self.ranges_set = set()

    def add_range(self, lower, upper):
        self.ranges.append(Range(lower, upper))
        self.ranges_set.update(self.ranges[-1].range_set)
        
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

    print(len(ranges.ranges_set))
