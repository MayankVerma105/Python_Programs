class Person:
    count = 0
    def __init__(self, name, DOB, address):
        self.name = name
        self.DOB = DOB
        self.address = address

    def getName(self):
        return self.name
    def getDOB(self):
        return self.DOB
    def getaddress(self):
        return self.address
    def setName(self, name):
        self.name = name
    def setDOB(self, DOB):
        self.DOB = DOB
    def setaddress(self, address):
        self.address = address
    def getCount(self):
        return Person.count
    def __str__(self):
        return 'Name :'+self.name+'\nDOB :'+str(self.DOB)+'\nAddress:'+self.address

    def __del__(self):
        print('Deleted!!')
        Person.count -= 1
    
