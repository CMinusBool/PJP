class Node:
    pass


class OperatorNode(Node):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right


class NumberNode(Node):
    def __init__(self, value):
        self.value = value


def tokenize(expression):
    # Split the expression into tokens, remove whitespace and check for invalid characters
    tokens = []
    current_token = ''
    for char in expression:
        if char in ('+', '-', '*', '/', '(', ')'):
            if current_token:
                tokens.append(current_token)
            tokens.append(char)
            current_token = ''
        elif char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ''
        elif char.isdigit():
            current_token += char
        else:
            raise ValueError("Invalid character: {}".format(char))
    if current_token:
        tokens.append(current_token)
    return tokens


def parse_expression(tokens):
    # Helper functions for parsing
    def parse_multiply_division():
        node = parse_parenthesis()
        while peek() in ('*', '/'):
            operator = consume()
            right = parse_parenthesis()
            node = OperatorNode(operator, node, right)
        return node

    def parse_addition_subtraction():
        node = parse_multiply_division()
        while peek() in ('+', '-'):
            operator = consume()
            right = parse_multiply_division()
            node = OperatorNode(operator, node, right)
        return node

    def parse_parenthesis():
        token = consume()
        if token.isdigit():
            return NumberNode(int(token))
        elif token == '(':
            node = parse_addition_subtraction()
            # if expresion is not closed
            if consume() != ')':
                raise ValueError("Expected ')'")
            return node
        else:# probably not necessary becasue of the tokenize function
            raise ValueError("Invalid token: {}".format(token))

    # Parser state
    token_index = 0

    # check next token
    def peek():
        nonlocal token_index
        if token_index < len(tokens):
            return tokens[token_index]
        else:
            return None

    # Token consumption function
    def consume():
        nonlocal token_index
        token = peek()
        token_index += 1
        return token

    # Start parsing
    return parse_addition_subtraction()


def evaluate(node):
    if isinstance(node, NumberNode):
        return node.value
    elif isinstance(node, OperatorNode):
        left_val = evaluate(node.left)
        right_val = evaluate(node.right)
        if node.operator == '+':
            return left_val + right_val
        elif node.operator == '-':
            return left_val - right_val
        elif node.operator == '*':
            return left_val * right_val
        elif node.operator == '/':
            if right_val == 0:
                raise ValueError("Division by zero")
            return left_val // right_val
    else:
        raise ValueError("Invalid node type")


number_of_evaluations = int (input().strip())

for _ in range(number_of_evaluations):
    expression = input().strip()
    try:
        tokens = tokenize(expression)
        tree = parse_expression(tokens)
        result = evaluate(tree)
        print(result)
    except:
        print("ERROR")

