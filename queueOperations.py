from myQueue import Queue
def main():
    while 1:
        print('Choose an option \n')
        print('1. Create Queue')
        print('2. Delete Queue')
        print('3. Enqueue')
        print('4. Dequeue')
        print('5. Print Queue Data ')
        print('6. Front Element ')
        print('7. No of elements')
        choice = int(input('Enter Choice : '))
        if choice == 1:
            q = Queue()
            print('Queue Created ')
        elif choice == 2:
            del q
            print('Queue Deleted ')
        elif choice == 3:
            element = int(input('Enter element to be inserted : '))
            q.enqueue(element)
        elif choice == 4:
            print('Element deleted',q.dequeue())
        elif choice == 5:
            print(q)
        elif choice == 6:
            print('Front element',q.front())
        elif choice == 7:
            print('No. of elements : ',q.size())
        proceed = input('Enter y if you wish want to continue :')
        if proceed != 'y' and proceed != 'Y':
            break

if __name__ == '__main__':
    main()
