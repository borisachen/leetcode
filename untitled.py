
def deep_copy(head):
	if not head: return head
	iter = head
	d = {}
	while iter:
		d[iter] = RandomListNode(iter.val)
		iter = iter.next
	iter = head
	while iter:
		d[iter].next = iter.next
		d[iter].random = iter.random
		iter = iter.next
	return d[head]