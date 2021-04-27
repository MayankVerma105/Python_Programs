def insertionSort(lst):
    for i in range(0, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > temp:
            lst[j + 1] = lst[j]
            j = j - 1
            lst[j + 1] = temp

def main():
    lst = eval(input('Enter the list: '))
    print('Sorted List')
    insertionSort(lst)
    print(lst)

if __name__ == '__main__':
    main()
