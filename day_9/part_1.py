import fileinput


def main():
    largest = 0
    lines = list(fileinput.input())
    for index1, item1 in enumerate(lines):
        for index2, item2 in enumerate(lines):
            if index1 == index2:
                continue
            x1, y1 = item1.split(",")
            x2, y2 = item2.split(",")
            distance = (abs(int(x1) - int(x2)) +1) * (abs(int(y1) - int(y2)) + 1)
            if distance > largest:
                largest = distance

    print(largest)
    return largest
                

if __name__ == "__main__":
    main()
