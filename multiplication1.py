def printTable(num,nMultiple)
    for multiple in range(1, nMultiple + 1):
        for num in range(1, nTables + 1):
            print('{0: >2}'.format(num),'*',\
                  '{0: >2}'.format(multiple),'=',\
                  '{0: >3}'.format(num * multiple),'\t',end = '')
                  
        print()
        
def main():
    nTables = int(input('Enter number of multiplication tables : '))
    printTables(nTables)
    
if __name__ == '__main__':
    main()
