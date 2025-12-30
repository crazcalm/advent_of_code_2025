import fileinput
from pprint import pprint

class Node:
    def __init__(self, row, index, parent=None):
        self.row = row
        self.index = index
        self.right = None
        self.left = None
        self.parent = parent

    def __repr__(self):
        return f"Node(row={self.row}, index={self.index})"
        
def visit(node, path):
    if node.left:
        visit(node.left, path)
    if node.right:
        visit(node.right, path)

    if not node.right and not node.left:
        current = node
        print(current)
        tempt = [current]
        while current.parent:
            print(current.parent, ",")
            tempt.append(current.parent)
            current = current.parent

        #path.append(tempt)
        path.append(1)
    
def main2():
    head = Node(0, 5)
    left = Node(1,4, head)
    right = Node(1, 6, head)
    head.right = right
    head.left = left

    left_left = Node(2,3, left)
    left_right = Node(2, 5, left)

    head.left.left = left_left
    head.left.right = left_right
    
    paths = [head]
    print(visit(head, paths))
    pprint(paths)


def main():
    lines = list(fileinput.input())
    head = Node(row=0, index=lines[0].find("S"))
    current_nodes = [head]
    
    for row, line in enumerate(lines[1:], start=1):
        print(f"num of beams -- {len(current_nodes)}")
        print(f"row: {row}")
        for node in current_nodes:
            if line[node.index] == "^":
                import pdb
                #pdb.set_trace()
                left = Node(row=row, index=node.index - 1, parent=node)
                right = Node(row=row, index=node.index + 1, parent=node)
                node.left = left
                node.right = right

                current_nodes.append(left)
                current_nodes.append(right)

        current_nodes = [node for node in current_nodes if node.left is None]

    print("finished tree")
        
    paths = []
    visit(head, paths)
    pprint(paths)
    print(len(paths))

    
if __name__ == "__main__":
    main()
