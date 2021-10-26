*Binary Search Tree Properties*

1. All the key in left subtree is less or equal than the root key.

2. All the key in right subtree is larger or equal than the root key.
3. Use in-order-traverse can print the bst keys in sorted order.

4. To find minimum value: follow left child until nil.

5. To find maximum value: follow right child until nil. 

6. To find successor of a key: 
    successor: the smallest key larger than the current key. 
    - the minimum key in right subtree if right subtree exists.
    - otherwise, the lowest ancestor y of current node x where x is in the left subtree of y. 

* Binary Search Tree Operations*     
    - delete 
    - insert 
    - add

* Binary Search Tree Traversal:
    - Inorder traverse: left - root - right
    - Preorder traverse: root -left - right
    - Postorder traverse: left - right - root
