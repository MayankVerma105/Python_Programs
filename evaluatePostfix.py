from stack import Stack
def evaluatePostfixExp(exp):
    stk = Stack()
    operations = ['+','-','*','/']
    for symbol in exp:
        if symbol in operations:
            operand2 = stk.pop()
            operand1 = stk.pop()
            result = str(eval(operand1 + symbol + operand2 ))
            stk.push(result)
        else:
            stk.push(symbol)
    result = int(stk.pop())
    return result

def main():
    exp = input('Enter a postfix expression use single digit number only:')
    result = evaluatePostfixExp(exp)
    print(result)

if __name__ == '__main__':
    main()
