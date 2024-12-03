# trida pro kazdy bod, kdy se robot musi rozhodnout (uzel)
class BinaryTreeNode:
    def __init__(self, rozhodnuti, uzel=None):
        self.rozhodnuti = rozhodnuti  # rozhodnuti kam pujde dal
        self.uzel = uzel  # reference k
        self.levy = None  # levy potomek
        self.pravy = None  # pravy potomek


# trida pro vytvoreni celeho binarniho stromu
class BinaryTree:
    def __init__(self):
        self.root = None  # koren celeho stromu
        self.uzel = None  # aktualni uzel

    def rozhodni_se(self, decision):
        """
        Adds a decision to the binary tree.
        """
        new_node = BinaryTreeNode(decision, parent=self.uzel)
        if not self.root:
            self.root = new_node
        else:
            if not self.current.left:
                self.current.left = new_node
            elif not self.current.right:
                self.current.right = new_node
            else:
                raise ValueError("Both children are already assigned. Cannot add a new decision.")
        self.current = new_node

    def backtrack(self):
        """
        Moves back to the parent node to explore other paths.
        """
        if self.current and self.current.parent:
            self.current = self.current.parent
        else:
            raise ValueError("Cannot backtrack further.")
