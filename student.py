class Student:
    def __init__(self, rollno, name, marks ):
        self.rollno = rollno
        self.name = name
        self.marks = marks

    def display(self):
        return 'Roll no :\n' +str(self.rollno)+ ',Name: \n' +str(self.name)+ 'marks: \n ' + str(self.marks) +'\n'
#Driver class
s1=Student(1,'Sourabh',56)
s2=Student(2,'Mayank',67)
print(s1.display())
print(s2.display())
