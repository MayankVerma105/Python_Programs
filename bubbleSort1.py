def bubbleSort(lst):
    n = len(lst)-1
    for i in range(0,n):
        swap = False
        for j in range(n, i ,-1):
            if lst[j] < lst[j - 1]:
                swap = True
                lst[j], lst[j - 1] = lst [j - 1], lst[j]
        if swap == False:
            break
def main():
    lst = eval(input('Enter the list'))
    print('Sorted list')
    bubbleSort(lst)
    print(lst)

if __name__ == '__main__':
    main()
