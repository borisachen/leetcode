def dfs(root):
    stack = []
    cur = root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.apppend(cur)
        stack.append(cur.right)
