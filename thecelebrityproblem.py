N = 8

Matrix = [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0]]

def knows(a, b):

    return Matrix[a][b]

def findCelebrity(n):
    s = []
    for i in range(n):
        s.append(i)

    A = s.pop()
    B = s.pop()

    while (len(s)> 1):
        if (knows(A,B)):
            A = s.pop()
        else:
            B = s.pop()

    if (len(s) == 0):
        return -1

    C = s.pop()

    if (knows(C, B)):
        C = B
         
    if (knows(C, A)):
        C = A

    for i in range(n):
        if ((i != C) and (knows(C,i) or not knows(i, C))):
            return -1
    return C

#Driver Code
if __name__ == '__main__':
    n = 4
    id_ = findCelebrity(n)
     
    if id_ == -1:
        print("No celebrity")
    else:
      print("Celebrity ID ", id_)
