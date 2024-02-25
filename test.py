def calculate_expression():
    def get_expression():
        return input().strip()

    def findParenthesis(expression):
        start = 0
        end = 0
        i = 0
        for character in expression:
            if character == '(':
                start = i
            elif character == ')':
                end = i
            if start != 0 and end != 0:
                if start < end:
                    return expression[start:end+1]
                else:
                    raise Exception("Invalid expression")
            i += 1

        return -1
    def findNumber(expression):
        i = 0
        number = 0
        for character in expression:
            if '0' <= character <= '9':
                number += int(character)
                i += 1
            else:
                return number, expression[i:].strip()
    def findToken(expression):
        i = 0
        for character in expression:
            if character > '9' or character in ",." or character < '(':
                raise Exception("Invalid character")
            elif character == '(':
                return '(', expression[i:].strip()
            elif character == ')':
                return ')', expression[i:].strip()
            elif character == '+':
                return '+', expression[i:].strip()
            elif character == '-':
                return '-', expression[i:].strip()
            elif character == '*':
                return '*', expression[i:].strip()
            elif character == '/':
                return '/', expression[i:].strip()
            elif '0' <= character <= '9':
                return findNumber(expression[i:])
            i += 1

    def findExpression(expression):
        token, expression = findToken(expression)
        if token == '(':
            number, expression = findExpression(expression)
            if expression[0] != ')':
                raise Exception("Invalid expression")
            return number, expression[1:]
        else:
            number, expression = findNumber(expression)
            return number, expression

    line = get_expression()
    eval()

    try:
        print(findToken(line))
    except:
        print("ERROR")


def main():
    number_of_evaluations = int (input().strip())
    for _ in range(number_of_evaluations):
        calculate_expression()


if __name__ == "__main__":
    main()