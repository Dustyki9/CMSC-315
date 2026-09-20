"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")
 
    # ===============================
    # CREATE A HASH TABLE
    # ===============================
    #
    # A Python dictionary IS a hash table under the hood.
    # When you add a key, Python runs the key through a hash
    # function (hash()) which converts it into an integer.
    # That integer determines which internal "bucket" (slot in
    # the underlying array) the key-value pair is stored in.
    # This is why dictionary lookups are, on average, O(1) --
    # instead of scanning every item like a list, Python jumps
    # almost directly to the bucket where the value lives.
 
    student_grades = {}  # start with an empty dictionary (empty hash table)
 
    # Insert 5 key-value pairs. Each key is hashed to decide
    # where it is stored internally.
    student_grades["Alice"] = 92
    student_grades["Ben"] = 85
    student_grades["Carla"] = 78
    student_grades["Derek"] = 90
    student_grades["Elena"] = 88
 
    print("\n=== INSERT OPERATIONS ===")
    print("Dictionary after inserting 5 key-value pairs:")
    print(student_grades)
 
    # ===============================
    # LOOKUP OPERATIONS
    # ===============================
    #
    # Looking up a value by key does NOT search through every
    # item. Python hashes the key again, jumps to the matching
    # bucket, and returns the value. This is what makes
    # dictionary lookups fast regardless of how large the
    # dictionary grows.
 
    print("\n=== LOOKUP OPERATIONS ===")
    print(f"Alice's grade: {student_grades['Alice']}")
    print(f"Derek's grade: {student_grades['Derek']}")
 
    # Using .get() is a safer lookup method because it returns
    # None (or a default) instead of raising an error if the
    # key does not exist.
    print(f"Using .get() for 'Ben': {student_grades.get('Ben')}")
 
    # ===============================
    # UPDATE OPERATIONS
    # ===============================
    #
    # Assigning a new value to an EXISTING key does not create
    # a new entry. Python hashes the key, finds the existing
    # bucket, and overwrites the value stored there.
 
    print("\n=== UPDATE OPERATIONS ===")
    print(f"Before update: Carla = {student_grades['Carla']}")
    student_grades["Carla"] = 81  # Carla retook a quiz
    print(f"After update:  Carla = {student_grades['Carla']}")
    print("Full dictionary after update:")
    print(student_grades)
 
    # ===============================
    # DELETE OPERATIONS
    # ===============================
    #
    # Deleting a key removes its entry from the underlying
    # hash table entirely. The key must be re-hashed and
    # inserted again later if you want it back.
 
    print("\n=== DELETE OPERATIONS ===")
    print("Before deletion:")
    print(student_grades)
    del student_grades["Ben"]  # Ben dropped the course
    print("After deleting 'Ben':")
    print(student_grades)
 
    # ===============================
    # EDGE CASES
    # ===============================
 
    print("\n=== EDGE CASES ===")
 
    # Edge case 1: Looking up a key that does not exist.
    # Using [] directly raises a KeyError, so we handle it safely.
    try:
        print(student_grades["Ben"])
    except KeyError:
        print("Edge Case 1: Looking up 'Ben' (already deleted) "
              "raises a KeyError -- the key no longer exists in "
              "the hash table.")
 
    # Safer alternative using .get(), which returns None instead
    # of crashing the program.
    result = student_grades.get("Ben")
    print(f"Edge Case 1b: Using .get('Ben') instead returns: {result}")
 
    # Edge case 2: Deleting a key that does not exist.
    # del would raise a KeyError, so .pop() with a default is safer.
    removed = student_grades.pop("Frank", "Key not found")
    print(f"Edge Case 2: Attempting to delete 'Frank' (never existed) "
          f"safely returns: {removed}")
 
    # Edge case 3: Updating/inserting into an empty dictionary.
    empty_dict = {}
    empty_dict["NewKey"] = "NewValue"
    print(f"Edge Case 3: Adding to an empty dictionary works fine: {empty_dict}")
 
    # Edge case 4: Two different keys can (in theory) hash to the
    # same bucket -- this is called a COLLISION. Python resolves
    # collisions internally (using open addressing), so as the
    # programmer you never see broken data, but it is worth noting
    # that hash collisions are why worst-case dictionary operations
    # can degrade from O(1) to O(n) in rare cases.
    print("Edge Case 4: Collisions are handled internally by Python; "
          "as users we never manually resolve them, but they explain "
          "why hash table performance is *average* O(1), not guaranteed.")
 
    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================
    #
    # A simple contact book / phone directory. Names (keys) map
    # to phone numbers (values). This mirrors how hash tables are
    # used in real applications: fast lookup of a value by a
    # unique identifier.
 
    print("\n=== REAL-WORLD SCENARIO: Contact Book ===")
    contact_book = {
        "Mom": "555-0101",
        "Work": "555-0192",
        "Pizza Place": "555-0147",
    }
    print("Initial contact book:", contact_book)
 
    # Insert a new contact
    contact_book["Dentist"] = "555-0133"
    print("After adding 'Dentist':", contact_book)
 
    # Lookup a contact
    print(f"Looking up 'Mom': {contact_book.get('Mom')}")
 
    # Update a contact's number
    contact_book["Work"] = "555-0199"
    print("After updating 'Work':", contact_book)
 
    # Delete a contact
    del contact_book["Pizza Place"]
    print("After removing 'Pizza Place':", contact_book)
 
    # Edge case: looking up a contact that was never saved
    print(f"Looking up 'Unknown': {contact_book.get('Unknown', 'No such contact')}")
 
 
if __name__ == "__main__":
    main()
 
