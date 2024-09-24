In this assignment we are not creating and working with a class for an entire tree but just for a
node, as shown here by this snippet of code from bst.py:

class Node():

def __init__(self,
key = None,
leftchild = None,
rightchild = None):

self.key = key

self.leftchild = leftchild

self.rightchild = rightchild

A tree will simply consist of a collection of node instances with their children set correctly. We will
reference a tree simply by referencing the instance of its root node.

Thus we can start building a tree via a command such as:

root = Node(key=100)

Then we can add a left child to this via:
root.leftchild = Node(key=50)

And we could delete this same child via:
root.leftchild = None

Example 6.1. For example consider the following tracefile:

insert,5

insert,10

insert,2

insert,3

insert,4

delete,3

insert,1

dump


The lines would be processed in the order given where the final line then dumps the tree to stringified
JSON. The result would look like this:

{"k": 5, "l": {"k": 2, "l": {"k": 1, "l": null, "r": null},
"r": {"k": 4, "l": null, "r": null}}, "r": {"k": 10, "l": null, "r": null}}
