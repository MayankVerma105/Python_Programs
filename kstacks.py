class KStacks:
      
    def __init__(self, k, n):
        self.k = k
        self.n = n
        
        self.arr = [0] * self.n
  
        self.top = [-1] * self.k

        self.free = 0
  
        self.next = [i + 1 for i in range(self.n)]
        self.next[self.n - 1] = -1

    def isEmpty(self, sn):
        return self.top[sn] == -1
  
    def isFull(self):
        return self.free == -1

    def push(self, item, sn):
        if self.isFull():
            print("Stack Overflow")
            return
  
        insert_at = self.free
  
        self.free = self.next[self.free]
  
        self.arr[insert_at] = item
  
        self.next[insert_at] = self.top[sn]

        self.top[sn] = insert_at

    def pop(self, sn):
        if self.isEmpty(sn):
            return None
  
        top_of_stack = self.top[sn]
  
        self.top[sn] = self.next[self.top[sn]]
  
        self.next[top_of_stack] = self.free
        self.free = top_of_stack
  
        return self.arr[top_of_stack]
  
    def printstack(self, sn):
        top_index = self.top[sn]
        while (top_index != -1):
            print(self.arr[top_index])
            top_index = self.next[top_index]
  
# Driver Code
if __name__ == "__main__":
      
    # Create 3 stacks using an 
    # array of size 10.
    kstacks = KStacks(3, 10)
  
    # Push some items onto stack number 2.
    kstacks.push(15, 2)
    kstacks.push(45, 2)
  
    # Push some items onto stack number 1.
    kstacks.push(17, 1)
    kstacks.push(49, 1)
    kstacks.push(39, 1)
  
    # Push some items onto stack number 0.
    kstacks.push(11, 0)
    kstacks.push(9, 0)
    kstacks.push(7, 0)
  
    print("Popped element from stack 2 is " + 
                         str(kstacks.pop(2)))
    print("Popped element from stack 1 is " + 
                         str(kstacks.pop(1)))
    print("Popped element from stack 0 is " + 
                         str(kstacks.pop(0)))
  
    kstacks.printstack(0)
