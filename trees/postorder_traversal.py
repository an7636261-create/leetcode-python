def postorderTraversal(root):
    result = []
    if root:
        result += postorderTraversal(root.left)
        result += postorderTraversal(root.right)
        result.append(root.val)
    return result