def linearSearch(lst, searchValue):
    for i in range(0, len(lst)):
        if lst[i] == searchValue:
            return i
    return None
def main():
    lst = eval(input('Enter a list : '))
    searchVal = eval(input('Enter a value to be searched :'))
    searchResult = linearSearch(lst,searchVal)
    print(searchVal, 'found at index ', searchResult)

if __name__ == '__main__':
    main()
