import sys
from itertools import count, islice


def sequence():
    """Generate Recaman's sequence"""
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


def write_sequence(num):
    """Write Recaman's sequence to a text file"""
    filename = "recaman.txt"
    with open(filename, mode="wt", encoding="utf-8") as f:
        f.writelines(f"{r}\n" for r in islice(sequence(), num))


def main():
    write_sequence(num=int(sys.argv[1]))


if __name__ == '__main__':
    write_sequence(num=int(sys.argv[1]))
