"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    lst.insert(index, value)
    return lst


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    if not isinstance(index, int) or index < 0 or index >= len(lst):
        # Index is invalid -- out of range or wrong type so avoid the crash and signal failure
        return None
    return lst.pop(index) 
 # pop() removes the item AND returns its value

def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    for i in range(len(lst)): # scan sequentially, index by index
        if lst[i] == value:
            return i  # found it -- return position immediately
    return -1 #no match found -- return -1 to indicate failure


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.
    numbers = [10, 20, 30, 40, 50]
    print("\n=== INSERTION TESTS ===")
    print("Original list:", numbers)

    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning:", numbers)

    # Insert in the middle -- roughly half the list shifts right.
    middle_index = len(numbers) // 2
    insert_at(numbers, middle_index, 25)
    print(f"After inserting 25 at the middle (index {middle_index}):", numbers)

    # Insert at the end
    insert_at(numbers, len(numbers), 60)
    print("After inserting 60 at the end:", numbers)

 

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("Current list:", numbers)

    # Delete from the beginning -- remaining elements shift left.
    removed_first = delete_at(numbers, 0)
    print(f"Removed value at index 0: {removed_first} -> List now:", numbers)
 
    # Delete from the middle.
    mid = len(numbers) // 2
    removed_mid = delete_at(numbers, mid)
    print(f"Removed value at index {mid}: {removed_mid} -> List now:", numbers)

    # Delete from the end -- no shifting needed.
    last_index = len(numbers) - 1
    removed_last = delete_at(numbers, last_index)
    print(f"Removed value at index {last_index}: {removed_last} -> List now:", numbers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("Current list:", numbers)
 
    existing_value = numbers[1] if len(numbers) > 1 else numbers[0]
    result_found = search_value(numbers, existing_value)
    print(f"Searching for existing value {existing_value}: found at index {result_found}")
 
    missing_value = 9999
    result_missing = search_value(numbers, missing_value)
    print(f"Searching for missing value {missing_value}: result = {result_missing} (not found)")
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
   # Edge case 1: Deleting with an invalid (out-of-range) index.
    invalid_delete = delete_at(numbers, 999)
    print(f"Attempting to delete index 999 (invalid): returned {invalid_delete} "
          f"-- list unchanged: {numbers}")
 
    # Edge case 2: Searching an empty list.
    empty_list = []
    empty_search = search_value(empty_list, 10)
    print(f"Searching for 10 in an empty list: returned {empty_search} (correctly not found)")
 
    # Edge case 3: Inserting into an empty list.
    insert_at(empty_list, 0, 100)
    print(f"Inserting 100 into an empty list at index 0: {empty_list}")
 
    # Edge case 4: Deleting from an empty list.
    empty_delete = delete_at([], 0)
    print(f"Attempting to delete index 0 from an empty list: returned {empty_delete}")
 
# Scenario: A simple task queue for a customer support ticketing
    # system. Tickets are stored in the order they should be handled.
    # - New URGENT tickets get inserted at the FRONT of the queue.
    # - New NORMAL tickets get inserted at the END of the queue.
    # - Completed tickets are DELETED once resolved.
    # - Support staff SEARCH the queue by ticket ID to check status.

    print("\n=== REAL-WORLD SCENARIO: Support Ticket Queue ===")
 
    ticket_queue = ["TICKET-101", "TICKET-102", "TICKET-103"]
    print("Initial ticket queue:", ticket_queue)
 
    # An urgent ticket arrives and jumps to the front of the line.
    insert_at(ticket_queue, 0, "TICKET-URGENT-999")
    print("Urgent ticket added to front:", ticket_queue)
 
    # A normal ticket arrives and goes to the back of the line.
    insert_at(ticket_queue, len(ticket_queue), "TICKET-104")
    print("Normal ticket added to end:", ticket_queue)
 
    # Staff resolve the urgent ticket, so it's removed from the queue.
    resolved = delete_at(ticket_queue, 0)
    print(f"Resolved and removed: {resolved} -> Queue now:", ticket_queue)
 
    # Staff look up whether a specific ticket is still pending.
    lookup_id = "TICKET-103"
    position = search_value(ticket_queue, lookup_id)
    if position != -1:
        print(f"{lookup_id} is still pending at queue position {position}.")
    else:
        print(f"{lookup_id} was not found -- it may already be resolved.")


if __name__ == "__main__":
    main()