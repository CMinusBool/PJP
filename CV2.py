def check_for_token(string):
    if string.isspace():
        return
    if string[0] == '-':
        print("OP:-")
        if len(string) > 1:
            check_for_token(string[1:])
    elif string[0] == '(':
        print("LPAR")
        if len(string) > 1:
            check_for_token(string[1:])
    elif string[0] == '+':
        print("OP:+")
    elif string[0] == '*':
        print("OP:*")
    elif string[0] == '/':
        print("OP:/")


file = open("input.txt", "r")
file = file.read()

raw_tokens = file.split(" ")

print(raw_tokens)

for raw_token in raw_tokens:
    print(raw_token)
    check_for_token(raw_token)