class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        if root.left == None and root.right == None:
            return 1
        else:
            left_h = self.maxDepth(root.left)
            right_h = self.maxDepth(root.right)
            if left_h < right_h:
                return 1 + right_h
            else:
                return 1 + left_h

