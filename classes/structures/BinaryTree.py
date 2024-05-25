import string
from typing import Union

class Node:
    id:str
    value:Union[int,float]
    left:object
    right:object

    def __init__(self, value) -> None:
        self.id = None
        self.value = value
        self.left = None
        self.right = None

def insert(root:Node, value:Union[int, float], id=None) -> Node:
    if root is None:
        new_node = Node(value)
        new_node.id = id
        return new_node
    else:
        if root.value == value:
            return root
        elif (root.value < value):
            root.right = insert(root.right, value, id)
        else: 
            root.left = insert(root.left, value, id)
    return root

def create_tree(root:Node, terminals:list) -> object:
    for i in range(len(terminals)):
        insert(root, terminals[i], id=string.ascii_uppercase[i+1])

def inorder(root:Node):
    if root:
        inorder(root.left)
        print(root.id, end=" ")
        inorder(root.right)

@property
def get_root(self):
    return self.root.value

if __name__ == '__main__':
    r = Node(5); r.id = 'A'
    insert(r, 8, 'B')
    insert(r, 3, 'C')
    insert(r, 10, 'D')
    insert(r, 7, 'E')
    inorder(r)

    s = Node(5); s.id = 'A'
    create_tree(s, [3, 1, 4, 1, 5, 9, 2, 6])
    inorder(s)