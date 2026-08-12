from typing import List


class TreeNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:

    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if self.root is None:
            self.root = TreeNode(key, val)
            return

        curr = self.root
        parent = None

        while curr:
            parent = curr

            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                curr.val = val
                return

        newNode = TreeNode(key, val)

        if key < parent.key:
            parent.left = newNode
        else:
            parent.right = newNode

    def get(self, key: int) -> int:
        curr = self.root

        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val

        return -1

    def getMin(self) -> int:
        if self.root is None:
            return -1

        curr = self.root

        while curr.left:
            curr = curr.left

        return curr.val

    def getMax(self) -> int:
        if self.root is None:
            return -1

        curr = self.root

        while curr.right:
            curr = curr.right

        return curr.val

    def findMin(self, node):
        while node and node.left:
            node = node.left

        return node

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, curr, key):
        if curr is None:
            return None

        if key < curr.key:
            curr.left = self.removeHelper(curr.left, key)

        elif key > curr.key:
            curr.right = self.removeHelper(curr.right, key)

        else:
            # No left child
            if curr.left is None:
                return curr.right

            # No right child
            if curr.right is None:
                return curr.left

            # Two children:
            # Find inorder successor
            minNode = self.findMin(curr.right)

            curr.key = minNode.key
            curr.val = minNode.val

            curr.right = self.removeHelper(curr.right, minNode.key)

        return curr

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root, result) -> None:
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)