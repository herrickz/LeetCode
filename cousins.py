
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isCousins(x, y, root):

    if root.value == x or root.value == y:
        return False

    node_queue = []
    
    if root.left != None:
        if root.left.value == x or root.left.value == y:
            return False
        else:
            node_queue.append(root.left)

    if root.right != None:
        if root.right.value == x or root.right.value == y:
            return False
        else:
            node_queue.append(root.right)

    while(node_queue):

        found_x = False
        found_y = False

        for i in range(len(node_queue)):    
            current_node = node_queue.pop(0)
            is_parent = False

            if current_node.left != None:
                if not found_x and current_node.left.value == x:
                    is_parent = True
                    found_x = True

                elif not found_y and current_node.left.value == y:
                    is_parent = True
                    found_y = True
            
                else:
                    node_queue.append(current_node.left)

            if current_node.right != None:
                if not found_x and current_node.right.value == x:
                    found_x = True

                    if found_y and is_parent:
                        return False
                    
                elif not found_y and current_node.right.value == y:
                    found_y = True

                    if found_x and is_parent:
                        return False
                else:
                    node_queue.append(current_node.right)
            
            if found_x and found_y:
                return True

        if found_x or found_y:
            return False


    return False


#           1
#          / \
#        2     3
#       / \   / \
#      4   5 6   7

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

print(isCousins(2, 3, root))