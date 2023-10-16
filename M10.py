class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
        return root

def traverse_inorder(root):
    if root:
        traverse_inorder(root.right)
        print(root.value, end=" ")
        traverse_inorder(root.right)

def traverse_preorder(root):
    if root:
        print(root.value, end=" ")
        traverse_preorder(root.left)
        traverse_preorder(root.right)

def traverse_postorder(root):
    if root:
        traverse_postorder(root.left)
        traverse_postorder(root.right)
        print(root.value, end=" ")

def traverse_levelorder(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while(len(queue) > 0):
        print(queue[0].value, end=" ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

def findmin(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def delete(root, value):
    if root is None:
        return root

    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = findmin(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)

    return root

def clone(node):
    if node is None:
        return None

    new_node = TreeNode(node.value)
    new_node.left = clone(node.left)
    new_node.right = clone(node.right)

    return new_node

def main():
    root = None
    while True:
        try:
            value = int(input("Enter the value (-1 to exit): "))
            if value == -1:
                break
            root = insert(root, value)
        except ValueError:
            print("Invalid input! Please enter an integer value.")

    print("\nThe Pre-Order Traversal: ")
    traverse_preorder(root)
    print("\nThe In-Order Traversal: ")
    traverse_inorder(root)
    print("\nThe Post-Order Traversal: ")
    traverse_postorder(root)
    print("\nThe Level-Order Traversal: ")
    traverse_levelorder(root)

    delete_val = int(input("\nEnter the value to be deleted: "))
    root = delete(root, delete_val)
    print("\nThe Pre-Order Traversal: ")
    traverse_preorder(root)
    print("\nThe In-Order Traversal: ")
    traverse_inorder(root)
    print("\nThe Post-Order Traversal: ")
    traverse_postorder(root)
    print("\nThe Level-Order Traversal: ")
    traverse_levelorder(root)

    groot = clone(root)
    print("\nThe cloned Tree: ")
    traverse_inorder(groot)
    print()

if __name__ == "__main__":
    main()
