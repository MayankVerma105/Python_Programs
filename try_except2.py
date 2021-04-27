import sys
def main():
    try:
        f = open('Temporary_File','r')
    except IOError as err:
        print('Problem with Input Output',err)
        print(sys.exc_info())
    print('Program continues smoothly beyond try-except block')

if __name__ == '__main__':
    main()
