def doit(preorder, inorder):
	return build(0, 0, len(inorder), preorder, inorder)

def build(prestart, instart, inend, preorder, inorder):
	if prestart >= len(prestart) or instart > inend:
		return None
	val = preorder[prestart]
	node = TreeNode(val)
	j = instart
	while True:
		if inorder[j] == val:
			break
		else:
			j += 1
	node.left = build(prestart+1, instart, j, preorder, inorder) 
	node.right = build(prestart+1, j+1, inend, preorder, inorder)
	return node