def main():
    n = int(input('Enter Number of Subjects : '))
    totalMarks = 0
    print('Enter Marks : ')
    for i in range(1, n + 1):
        marks = float(input('Subject' + str(i) + ':'))
        assert marks >= 0 and marks <= 100
        totalMarks += marks
        percentage = totalMarks / n
        print(percentage)

if __name__ == '__main__':
    main() 
