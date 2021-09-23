
from BinaryTree import BinaryTree, Tree # NOTE this!!!
# NOTE this!!!# NOTE this!!!# NOTE this!!!# NOTE this!!!# NOTE this!!!


def main():
    tree1 = BinaryTree('aaa')
    # print(tree1)
    tree1.insert_left('bbb')
    # print(tree1)
    tree1.insert_right('ccc')
    # print(tree1.left_child.left_child.left_child)

    # # # 

    a = BinaryTree('aaa')
    a.insert_left('bbb')
    a.insert_right('ccc')

    b = a.left_child
    b.insert_right('ddd')

    c = a.right_child
    c.insert_left('e')
    c.insert_right('f')

    d = b.right_child
    e = c.left_child
    f = c.right_child

    # a.DFS_pre_order()
    # a.DFS_in_order()
    a.DFS_post_order()
    

# TODO :
# data structure, root, left/right
# methods.. basic __str__ printout
# three basic traversals...
# print pretty tree out!

