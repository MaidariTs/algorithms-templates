def read_input():
    seq = str(input())
    return seq


def is_correct_bracket_seq(seq: str) -> bool:
    print(len(seq))
    # if seq[0] == '{' and seq[len(seq) - 1]  {[()]}


if __name__ == '__main__':
    seq = read_input()
    print(is_correct_bracket_seq(seq))
