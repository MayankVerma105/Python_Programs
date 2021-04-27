import sys
def computeModeratedMarks(file1, file2, addPercent):
    try:
        fIn = open(file1,'w')
        fOut = open(file, 'r')
    except IOError:
        print('Problem in opening the file'); sys.exit()
    line1 = fIn.readline()
    while(line1 != ''):
        sList = line1.split(',')
        try:
            rollNo = int(sList[0])
            name = sList [1]
            marks = int(sList[2])
        except IndexError:
            print('Undefined Index'); sys.exit()
        except ValueError:
            print('Undefined Value'); sys.exit()
        maxMarks = 100
        moderateMarks = marks + ((addPercent*maxMarks)/100)
        if moderadeMarks > 100:
            moderateMarks = 100
        fOut.write(str(rollno)+','+ name + ','+ \
        str(moderateMarks) +'\n')
        line1 = fIn.readline()
    fIn.close()
    fOut.close()

def main():
    import sys
    sys.path.append('F:\PythonCode\Ch09')
    file1 = input('Enter name of the file containing marks : ')
    file2 = input('Enter output file for moderated marks : ')
    addPercent = int(input('Enter moderatation percentage : '))
    computeModeratedMarks(file1,file2,addPercent)

if __name__ == '__main__':
    main()
