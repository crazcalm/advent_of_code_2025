class Range:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def in_range(self, num):
        return num >= self.lower and num <= self.upper

class Ranges:
    def __init__(self):
        self.ranges = []

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
    state = "ranges"
    count = 0

    for line in fileinput.input():
        line = line.strip()

        if not line and state == "ranges":
            state = "ids"
            continue
        elif not line and state == "ids":
            break

        if state == "ranges":
            lower, upper = line.split("-")
            ranges.add_range(int(lower), int(upper))

        if state == "ids":
            if ranges.in_range(int(line)):
                count += 1

    print(count)
    
