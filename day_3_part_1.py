def batteries(data):
    tens = 0
    ones = 0
    largest = 0
    for index, digit_str in enumerate(data, start=1):
        digit = int(digit_str)
        if digit > tens and index != len(data):
            
            largest = int(f"{tens}{digit}")
            tens = digit
            ones = None
        elif ones is None or digit > ones:
            ones = digit
        else:
            pass
    if tens and ones and int(f"{tens}{ones}") > largest:
        largest = int(f"{tens}{ones}")
    return largest 

if __name__ == "__main__":
    import fileinput

    count = 0
    for line in fileinput.input():
        line = line.strip()
        if not line:
            break
        result = batteries(line)
        print(f"{line} -- batteries -> {result}")
        #print(f"{result}")
        count += result

    print(count)
