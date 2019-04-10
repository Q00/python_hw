class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if not self.head:
            return True

        return False

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("잘못된 Pop연산.\n")
            return None

        ret_data = self.head.data
        self.head = self.head.next

        return ret_data

    def print_stack(self):
        if self.is_empty():
            print("No data\n")
            return
        
        temp = self.head
        while True :
            data = temp.data
            print(f'  {data}', end='')
            temp = temp.next
            if temp == None:
                break
        print() 


def low_power(under, upper):
    result = 1.0
    if upper < 0:
        for i in range(0, upper*-1):
            result = result * float(under)

        return result
    elif upper == 0:
        return 1.0
    else:
        for i in range(0, upper):
            result = result * float(under)
        return result

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.print_stack()
    s.push(low_power(2,3))
    s.push(5)
    s.push(low_power(3,3))
    s.print_stack()
    s.pop()
    s.print_stack()
    s.push(1)
    s.push(low_power(2,8))
    s.print_stack()
    s.pop()
    s.print_stack()
    s.pop()
    s.print_stack()

