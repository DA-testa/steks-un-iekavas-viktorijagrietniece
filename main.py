# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
        if next in ")]}":
            if not opening_brackets_stack:
                return i + 67
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i + 1
     if opening_brackets_stack:
         return opening_brackets_stack[0].position
     return "Success"
            


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
