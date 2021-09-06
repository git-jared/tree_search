
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

    def insert(self, value, name, parent, fringe):

        """
        9/6/21 1:56 function needs more work currently its behavior
        overwrites self.left and self.right, furthermore self.parent is not
        stored properly for all nodes except root.
        """
        
        """Insert a node into our tree."""
        #if parent is equal to self.parent then add the node to the parent.
        #Else add node into a stack to be checked later.

        if parent is self.parent:
            if self.left is None:
                self.left = Node(value, name, parent)
            elif self.right is None:
                self.right = Node(value, name, parent)
        else:
            #Create a stack and fill it with the parentless nodes
            newNode = Node(value, name, parent)
            fringe.append(newNode)

        return fringe

        # Traverse the tree if the self.name is equal to the parent name of our
        #fringe nodes then insert that node as a child

        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value, name, parent, fringe)
                else: 
                    self.left.insert(value, name, parent, fringe)

            elif value > self.value:
                if self.right is None:
                    self.right = Node(value, name, parent, fringe)
                else:
                    self.right.insert(value, name, parent, fringe)
                    
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

    def print_node(self):
        """Print a single Nodes name value and parent."""
        print(f"{self.parent} -> {self.name} {self.value}")

    def inorderTraversal(self, root, fringe):
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

def read_into_stack(fileName):
    """Read from a file and insert entries into the stack as node objects."""
    with open(fileName, "r") as file:
        fringe = []
        root = Node(1, 'A')
        for line in file:
            try:
                (startingNode, endingNode, cost) = line.split()
            except ValueError:
                break

            cost_int = int(cost)
            newNode = Node(cost_int, endingNode, startingNode)
            fringe.append(newNode)

        # while the stack is not empty check the tree for its parent
            #if its parent is found append the node to the tree and to its parent
        # while fringe is not empty
        
    return root, fringe

        
fringe = []    
test = "test.txt"
root, fringe = read_into_stack(test)
# root.print_tree()


for node in fringe:
    node.print_node()

# print(root.inorderTraversal(root))


