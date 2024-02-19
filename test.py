def calculate_expresion():
    def getExpresion():
        return input().strip()


    def evaluateExpresion(expresion):
        for character in expresion:
            if character > '9' or character in ",." or character < '(':
                raise Exception("Invalid character")

    line = getExpresion()

    try:
        print(eval(input().strip()))
    except:
        print("ERROR")


def main():
    number_of_evaluations = int (input().strip())
    for _ in range(number_of_evaluations):
        calculate_expresion()


if __name__ == "__main__":
    main()