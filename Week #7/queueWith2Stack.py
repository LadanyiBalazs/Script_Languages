#!/usr/bin/env python3

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append(self, value):
        self.stack1.append(value)

    def size(self):
        return len(self.stack1)

    def is_empty(self):
        return self.size() == 0
    
    def popleft(self):
        if len(self.stack1) == 0:
            return None
        else:
            for n in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            x = self.stack2.pop()
            for n in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
            return x
            

    def __str__(self):
        return "Queue: " + str(self.stack1).replace(",", "")

def main():
    s = MyQueue()
    print("Empty: ", s.is_empty())
    s.append(1)
    s.append(3)
    s.append(5)
    print(s)
    x = s.popleft()
    print("Removed: ", x)
    print(s)
    print("Empty: ", s.is_empty())
    s.append(9)
    print(s)
    x = s.popleft()
    print("Removed: ", x)
    print(s)
    x = s.popleft()
    print("Removed: ", x)
    print(s)
    x = s.popleft()
    print("Removed: ", x)
    print("Empty: ", s.is_empty())
 
if __name__ == "__main__":
    main()