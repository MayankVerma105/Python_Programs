from stack import Stack
def main():
    while 1:
        print('Choose an opition \n')
        print('1. Create Stack')
        print('2. Delete Stack')
        print('3. Push')
        print('4. Pop')
        print('5. Print Stack Data ')
        print('6. Top element')
        print('7. No. of element ')
        choice = int(input('Enter Choice : '))
        if choice == 1:
            stk = Stack()
            print('Stack Created')
        elif choice == 2:
            del stk
            print('Stack Deleted')
        elif choice == 3:
            element = int(input('Enter element to be inserted : '))
            stk.push(element)
        elif choice == 4:
            print('Element poped ',stk.pop())
        elif choice == 5:
            print(stk)
        elif choice == 6:
            print('Top element',stk.top())
        elif choice == 7:
            print('No. of elements', stk.size())
        proceed = input('Enter y if you wish to continue ')
        if proceed != 'y' and proceed != 'Y':
            break

if __name__ == '__main__':
    main()
