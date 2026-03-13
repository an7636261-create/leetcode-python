def preorderTraversal(root):
    result = []
    if root:
        result.append(root.val)
        result += self.preorderTraversal(root.left)
        result += self.preorderTraversal(root.right)
    return result

