import time
from colorama import init, Fore, Style

init(autoreset=True)


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(position):
            if temp is None:
                raise IndexError("Position out of bounds.")
            temp = temp.next

        if temp is None:
            self.insert_at_end(data)
            return

        new_node.next = temp
        new_node.prev = temp.prev

        if temp.prev:
            temp.prev.next = new_node

        temp.prev = new_node

    def delete_node_at_beginning(self):
        if self.head is None:
            print(Fore.RED + "List is empty.")
            return

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_node_at_end(self):
        if self.head is None:
            print(Fore.RED + "List is empty.")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    def delete_node_at_position(self, position):
        if self.head is None:
            print(Fore.RED + "List is empty.")
            return

        temp = self.head

        if position == 0:
            self.delete_node_at_beginning()
            return

        for _ in range(position):
            if temp is None:
                raise IndexError("Position out of bounds.")
            temp = temp.next

        if temp is None:
            raise IndexError("Position out of bounds.")

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    def display_list(self):
        if self.head is None:
            print(Fore.RED + "Doubly Linked List is empty.")
            return

        temp = self.head

        print(Fore.GREEN + "Doubly Linked List:")

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    def search_node(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    def length_of_list(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count


def display_menu():
    print("\n" + Style.BRIGHT + "===== Doubly Linked List Operations =====")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete at Beginning")
    print("5. Delete at End")
    print("6. Delete at Position")
    print("7. Display List")
    print("8. Search Node")
    print("9. Length of List")
    print("10. Exit")


def main():
    dll = DoublyLinkedList()

    while True:
        display_menu()

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                data = int(input("Enter data: "))
                dll.insert_at_beginning(data)
                print(Fore.GREEN + "Node inserted at beginning.")

            elif choice == 2:
                data = int(input("Enter data: "))
                dll.insert_at_end(data)
                print(Fore.GREEN + "Node inserted at end.")

            elif choice == 3:
                data = int(input("Enter data: "))
                position = int(input("Enter position (0-indexed): "))
                dll.insert_at_position(data, position)
                print(Fore.GREEN + "Node inserted successfully.")

            elif choice == 4:
                dll.delete_node_at_beginning()
                print(Fore.RED + "Node deleted from beginning.")

            elif choice == 5:
                dll.delete_node_at_end()
                print(Fore.RED + "Node deleted from end.")

            elif choice == 6:
                position = int(input("Enter position to delete: "))
                dll.delete_node_at_position(position)
                print(Fore.RED + "Node deleted successfully.")

            elif choice == 7:
                dll.display_list()

            elif choice == 8:
                data = int(input("Enter value to search: "))

                if dll.search_node(data):
                    print(Fore.GREEN + "Node Found.")
                else:
                    print(Fore.RED + "Node Not Found.")

            elif choice == 9:
                print(Fore.CYAN + f"Length of List: {dll.length_of_list()}")

            elif choice == 10:
                print("Exiting Program...")
                break

            else:
                print(Fore.YELLOW + "Invalid Choice.")

        except ValueError:
            print(Fore.RED + "Please enter a valid integer.")

        except IndexError as e:
            print(Fore.RED + str(e))

        except Exception as e:
            print(Fore.RED + str(e))

        time.sleep(1)


if __name__ == "__main__":
    main()