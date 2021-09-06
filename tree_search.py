
class Node:
    """Class to represent a node in our search tree."""
    
    def __init__(self, value=0, name=None, parent=None):
        """Declare our node values."""
        self.value = value
        self.left = None
        self.right = None
        self.children = []
        self.name = name
        self.parent = parent

    def insert(self, value, name, parent):
        """Insert a node into our tree."""
        
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value, name, parent)
                else: 
                    self.left.insert(value, name, parent)

            elif value > self.value:
                if self.right is None:
                    self.right = Node(value, name, parent)
                else:
                    self.right.insert(value, name, parent)
                    
        else:
            self.value = value

    def print_tree(self):
        """Print the values in our node."""
        print(f"{self.parent}->{self.name} {self.value}")
        if self.left:
            self.left.print_tree()
        # print(self.value)
        if self.right:
            self.right.print_tree()

    def inorderTraversal(self, root):
        """ Left -> Root -> Right"""
        res = []
        if root:
            # print(f"before recursive {root.value}")
            res = self.inorderTraversal(root.left)
            res.append(root.value)
            # print(root.value)
            res = res + self.inorderTraversal(root.right)

        print(f"res = {res}")

        return res

def readintotree(fileName):
    """Read from a file and insert into a tree."""
    with open(fileName, "r") as file:
        first_line = False
        root = Node(1, 'A')
        for line in file:
            try:
                (startingNode, endingNode, cost) = line.split()
            except ValueError:
                break
            # paths = [key:val]

            node_int = int(cost)
            if first_line:
                root = Node(node_int)
                # print(node_int)
                first_line = False
            else:
                root.insert(node_int, endingNode, startingNode)
        
    return root

        
       
test = "test.txt"
root = readintotree(test)
root.print_tree()

# print(root.inorderTraversal(root))


