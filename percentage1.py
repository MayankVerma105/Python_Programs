def main():
    totalMarks = 0
    nSubjects = 0
    while True:
        marks = input('Marks for Subject ' + str(nSubjects + 1) + ' : ')
        if marks == '':
            break
        marks = float(marks)
        if marks < 0 and marks > 100:
            print('INVALID MARKS')
            continue
        nSubjects = nSubjects + 1
        totalMarks += marks
        percentage = totalMarks / nSubjects
        print('Total Marks : ',int(totalMarks))
        print('Number of subjects',nSubjects)
        print('Percentage : ',round(percentage))

if __name__ == '__main__':
    main()
