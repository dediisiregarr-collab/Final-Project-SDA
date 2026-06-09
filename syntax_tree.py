from stack import Stack
from collections import deque


class TreeNode:
    def __init__(self, tag):
        self.tag = tag
        self.children = []

    # Menambahkan child ke node saat ini
    def add_child(self, child):
        self.children.append(child)


# Menampilkan struktur tree
def print_tree(node, level=0):

    if node is None:
        return

    print("    " * level + node.tag)

    for child in node.children:
        print_tree(child, level + 1)


# Traversal Preorder
# Root -> Children
def preorder(node):

    if node is None:
        return

    print(node.tag, end=" ")

    for child in node.children:
        preorder(child)


# Traversal Postorder
# Children -> Root
def postorder(node):

    if node is None:
        return

    for child in node.children:
        postorder(child)

    print(node.tag, end=" ")
    
def level_order(root):

    if root is None:
        return []

    result = []

    queue = deque()

    queue.append(root)

    while queue:

        current = queue.popleft()

        result.append(current.tag)

        for child in current.children:
            queue.append(child)

    return result


# Menghitung jumlah seluruh node
def count_nodes(node):

    if node is None:
        return 0

    total = 1

    for child in node.children:
        total += count_nodes(child)

    return total


# Menghitung jumlah leaf node
def count_leaf_nodes(node):

    if node is None:
        return 0

    # Jika tidak punya child berarti leaf
    if len(node.children) == 0:
        return 1

    total = 0

    for child in node.children:
        total += count_leaf_nodes(child)

    return total


# Menghitung kedalaman tree
def tree_depth(node):

    if node is None:
        return -1

    if len(node.children) == 0:
        return 0

    max_depth = 0

    for child in node.children:

        depth = tree_depth(child)

        if depth > max_depth:
            max_depth = depth

    return max_depth + 1


# Membangun Syntax Tree dari token HTML
def build_tree(tokens):

    root = None
    stack = Stack()

    for token in tokens:

        # Tag pembuka
        if token.startswith("<") and not token.startswith("</"):

            tag = token[1:-1]

            node = TreeNode(tag)

            if root is None:
                root = node

            else:
                parent = stack.peek()

                if parent is not None:
                    parent.add_child(node)

            stack.push(node)

        # Tag penutup
        elif token.startswith("</"):

            if not stack.is_empty():
                stack.pop()

    return root


# Testing
if __name__ == "__main__":

    tokens = [
        "<html>",
        "<body>",
        "<div>",
        "<p>",
        "</p>",
        "</div>",
        "</body>",
        "</html>"
    ]

    root = build_tree(tokens)

    print("=== Syntax Tree ===")
    print_tree(root)

    print("\n=== Preorder ===")
    preorder(root)

    print("\n\n=== Postorder ===")
    postorder(root)

    print("\n\n=== Statistik ===")
    print("Jumlah Node :", count_nodes(root))
    print("Jumlah Leaf :", count_leaf_nodes(root))
    print("Kedalaman Tree :", tree_depth(root))