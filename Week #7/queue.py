#!/usr/bin/env python3

class Queue:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def size(self):
        return len(self.data)

    def empty(self):
        return self.size() == 0
    
    def remove(self):
        if len(self.data) == 0:
            return None
        else:
            return self.data.pop(0)

    def __str__(self):
        return "Queue: " + str(self.data).replace(",", "")

def main():
    s = Queue()
    print(s)
    print("Empty: ", s.empty())
    s.append(1)
    s.append(4)
    s.append(5)
    print(s)
    print("Size: ", s.size())
    print("Empty: ", s.empty())
    x = s.remove()
    print("Removed: ", x)
    print(s)
    x = s.remove()
    print("Removed: ", x)
    x = s.remove()
    print("Removed: ", x)
    x = s.remove()
    print("Removed: ", x)
 
if __name__ == "__main__":
    main()