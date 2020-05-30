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


def perform(fun, **args):
    fun(**args)

def action1(args):
    print('a1')

def action2(args):
    print('a2')

perform(action1, {'a':1, 'b':2})
