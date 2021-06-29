from collections import deque
from SS import create_avl_tree, insert_avl_tree

if __name__ == '__main__':
    # LL
    # avl_tree = create_avl_tree(deque([40, 25, 60, 20, 30]))
    # avl_tree.show_BSTree_1()
    # avl_tree = insert_avl_tree(avl_tree, 15)
    # avl_tree.show_BSTree_1()

    # LR
    # avl_tree = create_avl_tree(deque([80, 40, 90, 20, 60, 85, 95, 10, 30, 50, 70]))
    # avl_tree.show_BSTree_1()
    # avl_tree = insert_avl_tree(avl_tree, 45)
    # avl_tree.show_BSTree_1()

    # RR
    # avl_tree = create_avl_tree(deque([25, 20, 40, 30, 60]))
    # avl_tree.show_BSTree_1()
    # avl_tree = insert_avl_tree(avl_tree, 70)
    # avl_tree.show_BSTree_1()

    # RL
    avl_tree = create_avl_tree(
        deque([40, 30, 456, 3, 2, 429, 4, 2222, 1, 4, 6,5,6,7,7,7,12,3,4,4443,333, 4, 20, 80, 10, 30, 60, 90, 50, 70, 85, 95]))
    avl_tree.show_BSTree_1()
    avl_tree = insert_avl_tree(avl_tree, 55)
    avl_tree.show_BSTree_1()
