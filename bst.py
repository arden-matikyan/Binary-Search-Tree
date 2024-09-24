import json
import queue 

# DO NOT MODIFY THIS CLASS!
class Node():
    def  __init__(self, 
                  key        = None, 
                  leftchild  = None,
                  rightchild = None):
        self.key        = key
        self.leftchild  = leftchild
        self.rightchild = rightchild

# DO NOT MODIFY THIS FUNCTION!
# For the tree rooted at root, dump the tree to stringified JSON object and return.
# NOTE: in future projects you'll need to write the dump code yourself,
# but here it's given to you.
def dump(root: Node) -> str:
    def _to_dict(node) -> dict:    
        return {
            "k": node.key,
            "l": (_to_dict(node.leftchild) if node.leftchild is not None else None),
            "r": (_to_dict(node.rightchild) if node.rightchild is not None else None)
        }
    if root == None:
        dict_repr = {}
    else:
        dict_repr = _to_dict(root)
    return json.dumps(dict_repr)

#---------------------------------------------------------------------------------------------------

# For the tree rooted at root, insert the given key and return the root node.
# The key is guaranteed to not be in the tree.
def insert(root: Node, key: int) -> Node:
    
    if root is None: 
        root = Node(key, None, None) 
    else:
        current = root 
        while current is not None: 
            if key < current.key: 
                if current.leftchild is None: 
                    current.leftchild = Node(key, None, None)
                    return root 
                else: 
                    current = current.leftchild
            elif key > current.key:
                if current.rightchild is None: 
                    current.rightchild = Node(key, None, None)
                    return root 
                else: 
                    current = current.rightchild

    return root

# For the tree rooted at root, delete the given key and return the root node.
# The key is guaranteed to be in the tree.
# When replacement is necessary use the inorder successor.
def delete(root: Node, key: int) -> Node:
    
    if root is None: 
        return None 
    
    # traverse until key is found 
    if key < root.key: 
        # replace key when deleted 
        root.leftchild = delete(root.leftchild, key)
    elif key > root.key:
        root.rightchild = delete(root.rightchild, key)
    else: # key is found (node to be deleted) 
        if root.leftchild is None:
            repl = root.rightchild
            root = None 
            return repl 
        elif root.rightchild is None:  
            repl = root.leftchild
            root = None
            return repl 
        else: 
            repl = findnext(root)
            root.key = repl.key 

            # delete the in order successor (search by old key)
            root.rightchild = delete(root.rightchild, repl.key)

    return root 

def findnext(root: Node) -> Node: 

    current = root 
    parent = root 
    if root.rightchild is None: 
        return None 
    else:
        parent = current 
        current = current.rightchild
        while current.leftchild is not None:
            current = current.leftchild 

    return current 


# For the tree rooted at root, calculate the list of keys on the path from the root to the search key.
# Return the json stringified list.
# The key is guaranteed to be in the tree.
def search(root: Node, search_key: int) -> str:
    toRet = []

    current = root 
    toRet.append(current.key)

    while current.key != search_key: 
        if current.key < search_key: 
            current = current.rightchild
        else: 
            current = current.leftchild

        
        toRet.append(current.key)

    # Then tweak the next line so it uses your list rather than None.
    return(json.dumps(toRet))

# For the tree rooted at root, dump the preorder traversal to a stringified JSON list and return.
def preorder(root: Node) -> str:


    def pre(current: Node): 

        toRet.append(current.key)

        if current.leftchild is not None:
            pre(current.leftchild)

        if current.rightchild is not None:
            pre(current.rightchild)



    toRet = [] 
    pre(root)


    return(json.dumps(toRet))

# For the tree rooted at root, dump the inorder traversal to a stringified JSON list and return.
def inorder(root: Node) -> str:
    
    def pre(current: Node): 

        if current.leftchild is not None:
            pre(current.leftchild)

        toRet.append(current.key)
        
        if current.rightchild is not None:
            pre(current.rightchild)

    toRet = [] 
    pre(root)

    return(json.dumps(toRet))

# For the tree rooted at root, dump the postorder traversal to a stringified JSON list and return.
def postorder(root: Node) -> str:

    def pre(current: Node): 

        if current.leftchild is not None:
            pre(current.leftchild)

        if current.rightchild is not None:
            pre(current.rightchild)

        toRet.append(current.key)
        
    toRet = [] 
    pre(root)

    return(json.dumps(toRet))

# For the tree rooted at root, dump the BFT traversal to a stringified JSON list and return.
# The DFT should traverse left-to-right.
def bft(root: Node) -> str:
    
    toRet = [] 
    q = queue.Queue()
    q.put(root) 
    current = root 

    while(q.empty() is False): 
        current = q.get()     
        toRet.append(current.key)

        if current.leftchild is not None: 
            q.put(current.leftchild)
        if current.rightchild is not None: 
            q.put(current.rightchild)
        
    # Then tweak the next line so it uses your list rather than None.
    return json.dumps(toRet)    