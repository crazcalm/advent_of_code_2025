if __name__ == "__main__":
    import fileinput

    lines = list(fileinput.input())
    old_beams = set()
    new_beams = set()

    old_beams.add(lines[0].find("S"))

    count = 0
    for line in lines[1:]:
        for b_index in old_beams:
            if line[b_index] == ".":
                new_beams.add(b_index)
            elif line[b_index] == "^":
                count += 1
                new_beams.add(b_index+1)
                new_beams.add(b_index-1)
        print(f"new_beams: {new_beams}")
        old_beams = new_beams
        new_beams = set()

    print(count)
