def preorderTraversal(root):
    result = []
    if root:
        result.append(root.val)
        result += preorderTraversal(root.left)
        result += preorderTraversal(root.right)
    return result

