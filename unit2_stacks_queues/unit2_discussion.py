"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []  # Using a list to store stack items

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            print("Queue is empty. Cannot dequeue. :( ")
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Returns the front value WITHOUT removing it.
        if self.is_empty():
            print("Queue is empty. Cannot view front.")
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")
 
    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO (LIFO: Last In, First Out) ===")
    stack = Stack()
 
    print("\n-- Pushing 4 values onto the stack --")
    for value in ["Plate 1", "Plate 2", "Plate 3", "Plate 4"]:
        stack.push(value)
        print(f"Pushed: {value} | Stack now: {stack.items}")
 
    print("\n-- Peeking at the top of the stack --")
    print(f"Top of stack (peek): {stack.peek()}")
 
    print("\n-- Popping all values to demonstrate LIFO behavior --")
    while not stack.is_empty():
        popped = stack.pop()
        print(f"Popped: {popped} | Stack now: {stack.items}")
    print("Notice the order: Plate 4, 3, 2, 1 — the LAST plate pushed")
    print("was the FIRST one popped. That is LIFO behavior.")
 
    print("\n-- EDGE CASE: Popping from an empty stack --")
    result = stack.pop()
    print(f"Result of pop() on empty stack: {result}")
 
    print("\n-- EDGE CASE: Peeking at an empty stack --")
    result = stack.peek()
    print(f"Result of peek() on empty stack: {result}")
 
    print("\n-- EDGE CASE: Single-item stack becomes empty after removal --")
    single_stack = Stack()
    single_stack.push("Only Item")
    print(f"Stack after one push: {single_stack.items}")
    single_stack.pop()
    print(f"Stack after popping the only item: {single_stack.items}")
    print(f"is_empty() check: {single_stack.is_empty()}")
 
    print("\n-- REAL-WORLD SCENARIO: Browser 'Back' Button History --")
    browser_history = Stack()
    pages = ["home.com", "products.com", "cart.com", "checkout.com"]
    for page in pages:
        browser_history.push(page)
        print(f"Visited: {page}")
    print("\nUser clicks 'Back' repeatedly:")
    while not browser_history.is_empty():
        page = browser_history.pop()
        print(f"Going back from: {page}")
    print("This mirrors LIFO: the most recently visited page is always")
    print("the first one you return to when clicking 'Back'.")
 

    
# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

    print("\n\n=== QUEUE DEMO (FIFO: First In, First Out) ===")
    queue = Queue()
 
    print("\n-- Enqueuing 4 values onto the queue --")
    for value in ["Customer 1", "Customer 2", "Customer 3", "Customer 4"]:
        queue.enqueue(value)
        print(f"Enqueued: {value} | Queue now: {list(queue.items)}")
 
    print("\n-- Checking the front of the queue --")
    print(f"Front of queue: {queue.front()}")
 
    print("\n-- Dequeuing all values to demonstrate FIFO behavior --")
    while not queue.is_empty():
        served = queue.dequeue()
        print(f"Served: {served} | Queue now: {list(queue.items)}")
    print("Notice the order: Customer 1, 2, 3, 4 — the FIRST customer")
    print("in line was the FIRST one served. That is FIFO behavior.")
 
    print("\n-- EDGE CASE: Dequeuing from an empty queue --")
    result = queue.dequeue()
    print(f"Result of dequeue() on empty queue: {result}")
 
    print("\n-- EDGE CASE: Checking front of an empty queue --")
    result = queue.front()
    print(f"Result of front() on empty queue: {result}")
 
    print("\n-- EDGE CASE: Single-item queue becomes empty after removal --")
    single_queue = Queue()
    single_queue.enqueue("Only Customer")
    print(f"Queue after one enqueue: {list(single_queue.items)}")
    single_queue.dequeue()
    print(f"Queue after dequeuing the only item: {list(single_queue.items)}")
    print(f"is_empty() check: {single_queue.is_empty()}")
 
    print("\n-- REAL-WORLD SCENARIO: Printer Job Queue --")
    printer_queue = Queue()
    jobs = ["Resume.pdf", "Report.docx", "Invoice.xlsx", "Flyer.png"]
    for job in jobs:
        printer_queue.enqueue(job)
        print(f"Job submitted to printer: {job}")
    print("\nPrinter processes jobs in the order received:")
    while not printer_queue.is_empty():
        job = printer_queue.dequeue()
        print(f"Now printing: {job}")
    print("This mirrors FIFO: the first document submitted is the")
    print("first one printed, keeping the process fair and predictable.")
 
 
if __name__ == "__main__":
    main()