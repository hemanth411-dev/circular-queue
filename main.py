# main.py

from circular_queue import CircularQueue 

def display_menu():
    print("\n---- Circular Queue Menu ----")
    print("1. Enqueue an element")
    print("2. Dequeue an element")
    print("3. Peek at the front element")
    print("4. Peek at the rear element")
    print("5. Display the queue")
    print("6. Show current size of the queue")
    print("7. Exit")

def main():
    try:
        capacity = int(input("Enter the maximum capacity of the queue: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for capacity.")
        return
    
    queue = CircularQueue(capacity)

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid choice! Please enter a number between 1 and 7.")
            continue
        
        if choice == 1:
            try:
                item = int(input("Enter the item to enqueue: "))
                queue.enqueue(item)
            except ValueError:
                print("Invalid item. Please enter an integer.")
        
        elif choice == 2:
            item = queue.dequeue()
            if item is not None:
                print(f"Dequeued item: {item}")
        
        elif choice == 3:
            item = queue.peek_front()
            if item is not None:
                print(f"Front item: {item}")
        
        elif choice == 4:
            item = queue.peek_rear()
            if item is not None:
                print(f"Rear item: {item}")
        
        elif choice == 5:
            print("Current Queue: ", end="")
            queue.display()
        
        elif choice == 6:
            print(f"Current size of the queue: {queue.current_size()}")
        
        elif choice == 7:
            print("Exiting the program...")
            break
        
        else:
            print("Invalid choice! Please select a valid option (1-7).")

if __name__ == "__main__":
    main()
