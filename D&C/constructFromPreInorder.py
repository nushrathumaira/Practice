class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # not a binary search tree
        if inorder:
            root_ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[root_ind])
            root.left = self.buildTree(preorder,inorder[0:root_ind])
            #preorder is a mutable object (list) and since you are building the left-subtree first, it will just extract out it's elements first, as well as root before the right subtree recursive call uses it.
            root.right = self.buildTree(preorder,inorder[root_ind+1:])
            return root