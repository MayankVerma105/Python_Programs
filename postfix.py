from stack import Stack
def postfix(exp):
    precedence = {'+':1, '-':2, '*':3, '/':4}
    operand = '0123456789'

    result = ''
    stk = Stack()
    for symbol in exp:
        if symbol == '(':
            stk.push(symbol)
        elif symbol == ')':
            val = stk.pop()
            while val != '(':
                result += val
                val = stk.pop()
        elif symbol in operand:
            result += symbol
        elif symbol in precedence:
            if not(stk.isEmpty()):
                stkTop = stk.top()
            while not(stk.isEmpty()) and stkTop != '(' \
                  and precedence [stkTop] >= precedence[symbol]:
                result += stk.pop()
            return result
def main():
    exp = input('Enter the expression in infix notation: ')
    exp = postfix(exp)
    print(exp)

if __name__ == '__main__':
    main()
