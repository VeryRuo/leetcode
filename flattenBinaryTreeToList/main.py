# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        def _flatten(r):
            head = r
            tail = r
            h1 = h2 = t1 = t2 = None
            if r.left != None:
                h1, t1 = _flatten(r.left)
                # print h1.val, t1.val
            if r.right != None: 
                # print r.val, r.right.val
                h2, t2 = _flatten(r.right)

            head.left = None
            if h1 != None:
                head.right = h1
                tail = t1
            if h2 != None:
                tail.right = h2
                tail = t2
            return head, tail


        if root == None:
            return
        _flatten(root)

def makeTree(A, i):
    if i >= len(A):
        return None
    node = TreeNode(A[i])
    # print node.val, 
    node.left = makeTree(A, i * 2 + 1)
    node.right = makeTree(A, i * 2 + 2)
    return node

def preOrder(root):
    if root != None:
        print root.val, 
        preOrder(root.left) 
        preOrder(root.right)

if __name__ == '__main__':
    t = [1, 2, 5, 3, 4, 0, 6]
    root = makeTree(t, 0)
    # preOrder(root)
    s = Solution()
    s.flatten(root)
    while root.right != None:
        print root.val, 
        root = root.right
    print root.val
