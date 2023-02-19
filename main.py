from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
            pass
        
        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            if not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
            pass
            
    if opening_brackets_stack:
         return opening_brackets_stack[0].position
     return "Success"
            


def main():
    input_method = input()
    if "I" in input_method :
        text = input()
        mismatch = find_mismatch(text)
        if type (mismatch) == int:
           print(mismatch)
        else:
           print("Success")
    elif input_method == 'F':
        filename = input()
        test = "./test/" + filename
        with open (testfolder, mode = 'r') as file:
            text = file.read()
            mismatch = find_mismatch(text)
            print(mismatch)
       
if __name__ == "__main__":
    main()
