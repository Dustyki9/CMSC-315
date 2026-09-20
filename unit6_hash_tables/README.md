# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

This assignment deepened my understanding of how Python dictionaries work as hash tables. I learned that keys are run through a hash function to determine which internal bucket stores their value, which is why lookups, insertions, and deletions average O(1) time instead of requiring a full scan like a list would. Writing the insert, lookup, update, and delete operations helped me see that updating a key doesn't create a new entry, it overwrites the value at the existing hashed location.

The main challenge was handling edge cases safely. Directly accessing a missing key with square brackets raises a KeyError, so I had to use .get() and .pop() with default values to avoid crashing the program. This taught me the difference between "unsafe" direct access and defensive lookup methods.

A collision occurs when two different keys hash to the same bucket. Python resolves this internally using open addressing, so we rarely notice it, but collisions explain why hash table performance is described as average O(1) rather than guaranteed — in rare worst-case scenarios with many collisions, performance can degrade toward O(n).
