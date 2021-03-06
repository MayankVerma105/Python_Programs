def selectionSort(lst):
    for i in range(0, len(lst)-1):
        minIndex = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[minIndex]:
                minIndex = j
        if minIndex != i:
            lst[minIndex], lst[i] = lst[i], lst[minIndex]

def main():
    lst = eval(input('Enter a list : '))
    print('Sorted List')
    selectionSort(lst)
    print(lst)

if __name__ == '__main__':
    main()
