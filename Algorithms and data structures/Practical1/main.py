
with open("tests.bat", "r", encoding="utf-8", errors="ignore") as f:
    for i, line in enumerate(f):
        print(line.strip())
        if i > 20:  # only print first ~20 lines
            break


def read_dat(dat):
    pass

def find_min_spanning_tree(V, E, starting_v):
    pass

