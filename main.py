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
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            top = opening_brackets_stack.pop()
     if opening_brackets_stack:
         return opening_brackets_stack[0].position
     return "Success"
            


def main():
    input_method = input()
    if input_method = "F":
        file_name = input()
        with open(file_name, "r") as file:
            text = file.read().strip()
    else input_method == "I"
    text = input()
    
    mismatch = find_mismatch(text)
    if mismatch == "Success":
        print("Success")
    else
        print(mismatch)
        
   


if __name__ == "__main__":
    main()
