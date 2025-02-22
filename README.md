Problem Description: Circular Queue Implementation
The task is to implement a Circular Queue data structure using class-based programming in Python. A circular queue is a type of queue in which the last element is connected back to the first element, creating a circular arrangement. This structure helps efficiently utilize memory space by allowing the reuse of vacated spots when elements are dequeued.

Problem Requirements:
Queue Operations:

Enqueue: Add an element to the end (rear) of the queue.
Dequeue: Remove an element from the front of the queue.
Peek: Retrieve (but not remove) the front or rear element of the queue.
Display: Print all the elements in the queue from front to rear.
Check Full: Verify if the queue has reached its maximum capacity.
Check Empty: Verify if the queue is empty.
Current Size: Determine how many elements are currently in the queue.
Queue Properties:

The queue operates in a circular manner, where the rear pointer wraps around to the beginning of the queue when the end is reached.
The queue should have a fixed capacity set at the time of its creation.
The front and rear pointers must be managed such that when elements are dequeued, space is freed up and can be reused when new elements are enqueued.
Class-based Implementation:

The implementation should be object-oriented, with a class CircularQueue containing methods to handle the queue operations. The methods should properly manage the queue’s front and rear pointers and ensure circular behavior when adding/removing elements.
User Interaction:

The program should allow the user to interact with the circular queue, providing a menu-driven interface to enqueue, dequeue, peek, display the queue, and check the queue's status.
The user should be able to specify the maximum capacity of the queue and then perform various operations based on the menu choices.
Edge Case Handling:

Ensure that the queue gracefully handles cases like trying to dequeue from an empty queue or trying to enqueue into a full queue.
Proper error messages should be displayed when invalid operations are attempted.
