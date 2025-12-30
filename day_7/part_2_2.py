import fileinput

count = 0

def travel(b_index, l_index, lines):
    if l_index >= len(lines) - 1:
        
        global count
        count += 1
        print(f"current count: {count}")
        #print(f"b-index: {b_index}")
        return

    if lines[l_index][b_index] == "^":
        travel(b_index - 1, l_index + 1, lines)
        travel(b_index + 1, l_index + 1, lines)
    else:
        travel(b_index, l_index + 1, lines)


def main():
    lines = list(fileinput.input())
    b_index = lines[0].find("S")

    travel(b_index, 0, lines)
    print(count)


if __name__ == "__main__":
    count = 0
    main()
