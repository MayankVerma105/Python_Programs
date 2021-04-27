def bubbleSort(lst):
    n = len(lst) - 1
    for i in range(0, n):
        for j in range(0, i, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]

def main():
    lst = eval(input('Enter the list : '))
    print('Sorted list')
    lst.sort()
    print(lst)

if __name__=='__main__':
    main()
