class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        print("Item pushed into stack!")
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print("\nStack is empty. Cannot pop from an empty stack.\n")
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)
    
    def print_stack(self):
        print("Stack elements: ", end=" ")
        print(self.items)

# Creating a list (stack):
def main():
    stac = Stack()

    while True:
        print("\n1)Push element")
        print("2)Pop element")
        print("3)Check size of stack")
        print("4)View Stack")
        print("5)Exit program\n")
        choice = int(input("Enter choice: "))

        while True:
            if choice <=5 and choice > 0:
                break
            else:
                print("Invalid choice...Enter again")

        if choice == 1:
            val = int(input("Enter the value to be pushed into the stack: "))
            stac.push(val)
        elif choice == 2:
            popele = stac.pop()
            print(f"{popele} popped from stack!")
        elif choice == 3:
            print("Stack size:", stac.size())
        elif choice == 4:
            stac.print_stack()
        elif choice == 5:
            print("Exiting program.")
            exit()

if __name__ == "__main__":
    main()
