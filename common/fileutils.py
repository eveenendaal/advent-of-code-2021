def read_input(filename):
    with open(filename) as f:
        input = f.readlines()
        # trim the newline character of each line
        input = [x.strip() for x in input]
    return input
