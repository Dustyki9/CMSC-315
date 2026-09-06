"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None
 # Both children start as None because a brand-new node

class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        #empty tree
         self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
         self.root = self._insert_recursive(self.root, value)
 

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
       # Base case: we've walked off the tree (found an empty spot),
        # so this is where the new node belongs.
        if node is None:
            return Node(value)
              # The BST property says every node's left subtree holds
        # smaller values and its right subtree holds larger values.
        # So we compare 'value' to the current node's value to decide
        # which direction to keep searching for an empty spot.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # else: value == node.value -> duplicate, we simply don't
        # insert it again (this BST ignores duplicates).
 
        # Return the (possibly unchanged) node so the parent call
        # can relink it correctly.
        return node
            
    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
          # O(log n) average performance instead of O(n).
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
          # Base case 1: we hit an empty branch, so the value isn't here.
        if node is None:
            return False
 
        # Base case 2: found it.
        if value == node.value:
            return True
 
        # Recursive case: use the BST property to only search the
        # half of the tree that could possibly contain the value.
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)
 
 


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
     tree = BST()
    # Chosen so some values land in the left subtree of the root (50)
    # and some land in the right subtree, demonstrating both branches.
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
 
    for v in values_to_insert:
        tree.insert(v)
        # Each insertion starts at the root and compares against it:
        # values less than 50 branch left, values greater branch right.
        # That single comparison at the root immediately cuts the
        # remaining search space in half, and the same halving repeats
        # at every level as the value travels down the tree.
        print(f"Inserted {v}")
 
    print(f"Values inserted: {values_to_insert}")
 
    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================
    print("\n=== IN-ORDER TRAVERSAL ===")
    result = tree.inorder()
    print(f"In-order traversal result: {result}")
    print(
        "Explanation: The traversal visits left subtree -> node -> right "
        "subtree at every step. Since left children are always smaller "
        "and right children are always larger than their parent, this "
        "ordering naturally produces the values in sorted (ascending) order."
    )
     #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
      existing_values = [40, 80]
    missing_values = [25, 100]
 
    for v in existing_values:
        found = tree.search(v)
        print(f"Searching for {v} (exists): found = {found}")
 
    for v in missing_values:
        found = tree.search(v)
        print(f"Searching for {v} (does not exist): found = {found}")
 
    print(
        "Explanation: Existing values return True because the search "
        "follows the same left/right comparisons used during insertion "
        "and eventually lands on the matching node. Missing values return "
        "False because the search reaches an empty (None) branch before "
        "finding a match, proving the value was never inserted."
    )
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    # Edge case 1: searching/traversing an empty tree.
    empty_tree = BST()
    print(f"Empty tree in-order traversal: {empty_tree.inorder()}")
    print(f"Searching for 10 in an empty tree: {empty_tree.search(10)}")
    print(
        "Explanation: With no root node, the recursive helpers hit their "
        "base case (node is None) immediately, so traversal returns an "
        "empty list and search safely returns False instead of crashing."
    )
 
    # Edge case 2: inserting a duplicate value.
    tree.insert(50)  # 50 already exists in the tree
    print(f"After inserting duplicate 50, in-order traversal: {tree.inorder()}")
    print(
        "Explanation: Because _insert_recursive only recurses left or "
        "right (never both) and does nothing when value == node.value, "
        "the duplicate 50 is silently ignored and the tree structure "
        "stays unchanged."
    )
 
    # Edge case 3: a tree with only one node.
    single_node_tree = BST()
    single_node_tree.insert(99)
    print(f"Single-node tree in-order traversal: {single_node_tree.inorder()}")
    print(f"Searching for 99 in single-node tree: {single_node_tree.search(99)}")
    print(
        "Explanation: With only a root and no children, both left and "
        "right subtrees are None, so traversal simply visits the root, "
        "and searching for the root's own value returns True immediately."
    )


if __name__ == "__main__":
    main()
