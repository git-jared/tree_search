

class Entry:
    """A class  to represent a single entry in our graph. """

    def __init__(self, value=0, name=None, parent=None):
        """Declare our graph values."""
        self.value = value
        self.name = name
        self.parent = parent



class Node:
    """Class to represent a node in our search tree."""
    
    def __init__(self, value=0, name=None, parent=None):
        """Declare our node values."""
        self.value = value
        self.left = None
        self.right = None
        self.name = name
        self.parent = parent

    def insert(self, graph):
        """Insert a node into our tree."""

        #Fills in the left of our tree using recursion.
        counter = 0
        for entry in graph:
            if len(graph) == 0:
                break
            print(len(graph))
            print(entry.name)
            if entry.parent is self.name:
                if self.left is None:
                    newNode = Node(entry.value, entry.name)
                    self.left = newNode
                    print(f"{self.name} now has {self.left.name} attached to the left.")
                    graph.pop(counter)
                    self.left.insert(graph)
                    
            counter+=1

        #Fills in the right of our tree using recursion.
        counter = 0
        for entry in graph:
            if len(graph) == 0:
                break
            print(len(graph))
            print(entry.name)
            if entry.parent is self.name:
                if self.right is None:
                    newNode = Node(entry.value, entry.name)
                    self.right = newNode
                    print(f"{self.name} now has {self.right.name} attached to the right.")
                    graph.pop(counter)
                    self.right.insert(graph)
         
            counter+=1

    def print_tree(self):
        """Print the values in our node."""
        # print(f"{self.name} {self.value}")
        if self.left:
            self.left.print_tree()
        print(f"{self.name}->{self.value}")
        if self.right:
            self.right.print_tree()

    def print_node(self):
        """Print a single Nodes name value and parent."""
        print(f"{self.parent} -> {self.name} {self.value}")

    def inorderTraversal(self, root):
        """ Left -> Root -> Right"""
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.name)
            # print(root.name)
            res = res + self.inorderTraversal(root.right)

        return res

def read_into_stack(fileName):
    """Read from a file and insert entries into the stack as node objects."""
    with open(fileName, "r") as file:
        graph = []
        root = Node(1, 'A')
        for line in file:
            try:
                (startingNode, endingNode, cost) = line.split()
            except ValueError:
                break

            cost_int = int(cost)
            newEntry = Entry(cost_int, endingNode, startingNode)
            graph.append(newEntry)

    """ Remove all nodes not connected to our main tree so as to 
    prevent stack overflow or infinite looping and store them in a new
    graph."""
    children = []
    index = 0
    newGraph = []
    newGraphIndex = 0
    for entry in graph:
        children.append(entry.name)
    for entry in graph.copy():
        if entry.parent not in children and entry.parent is not root.name:
            newGraph.append(graph.pop(index))
            for num in range(len(graph)):
                if  graph[num].parent is newGraph[newGraphIndex].name:
                    newGraph.append(graph.pop(num))
            newGraphIndex+=1

        index+=1

    return root, graph, newGraph
 
graph = [] 
newGraph = []   
test = "test.txt"
root, graph, newGraph = read_into_stack(test)
loops = 0

root.insert(graph)

print()
print("graph")
graphTree=root.inorderTraversal(root)
print(graphTree)

newRoot = Node(1, newGraph[0].parent)
newRoot.insert(newGraph)
print("newGraph")
newGraphTree = newRoot.inorderTraversal(newRoot)
print(newGraphTree)
print("MYGRAPH")
for entry in graph:
    print(f"{entry.parent}->{entry.name}")
print()

root.print_tree()

