class Range:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def in_range(self, num):
        return num >= self.lower and num <= self.upper

    def __lt__(self, other):
        return self.lower < other.lower

    def __eq__(self, other):
        return self.lower == other.lower and self.upper == other.upper

    def __repr__(self):
        return f"Range: {self.lower}-{self.upper}"
    
class Ranges:
    def __init__(self):
        self.ranges = []
        self.index = 0
        self.value = None
        
    def sort(self):
        self.ranges.sort()
        for r in self.ranges:
            print(r)

    def merge(self, lower, upper):
        result = False
        self.sort()
        for r in self.ranges:
            if r == Range(lower, upper):
                result = True
                break
            
            elif r.lower <= lower and r.upper > lower:
                result = True
                if r.upper < upper:
                    r.upper = upper
                break
        return result

    def fix(self):
        index = 0
        while index < len(self.ranges) - 1:
            one = self.ranges[index]
            two = self.ranges[index + 1]

            if one.upper > two.lower:
                self.ranges.pop(index+1)
                print(f"started_again for '{one}' and '{two}'")
                self.add_range(two.lower, two.upper)
                index = 0
            elif one.lower == two.lower:
                if one.upper <= two.upper:
                    print(f"Removing {one}  because it is in {two}")
                    self.ranges.pop(index)
                    index = 0
            elif one.upper == two.lower:
                print(f"Merges {one} with {two}")
                one.upper = two.upper
                self.ranges.pop(index + 1)
                index = 0
            else:
                index += 1
    
    def add_range(self, lower, upper): 
        if not self.merge(lower, upper):
            self.ranges.append(Range(lower, upper))
            self.ranges.sort()
        
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
        ranges.fix()

    for data in ranges.ranges:
        print(data)
        count += data.upper - data.lower + 1  # to be inclusive
        print(f"count => {count}")

