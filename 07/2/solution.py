
from collections import namedtuple

class Node:
	def __init__(self, name, weight, children):
		self.name = name
		self.weight = weight
		self.children = children
		if not len(children):
			self.child_weights = []
		else:
			self.child_weights = [0] * len(children)
		self.parent = None

	def set_parent(self, parent):
		self.parent = parent

	def get_subtree_weight(self):
		return self.weight + sum(self.child_weights)


def set_child_weights(nodes, node):
	node = nodes.get(node)
	if len(node.children) == 0:
		return node.weight

	for i,c in enumerate(node.children):
		node.child_weights[i] = set_child_weights(nodes, c)

	return node.weight + sum(node.child_weights)


def is_tree_balanced(nodes, node):
	node = nodes.get(node)
	if len(node.children) == 0:
		return True
	if max(node.child_weights) != min(node.child_weights):
		return False
	return all([is_tree_balanced(nodes, c) for c in node.children])


def find_imbalance(nodes, node):
	node = nodes.get(node)
	child_balances = [is_tree_balanced(nodes, c) for c in node.children]
	# if all the children are balanced, the fault is in one of the 
	# child's weight
	if all(child_balances):
		assert len(node.children) != 2, "ambigious case"

		counts = {}
		for c in node.children:
			cn = nodes.get(c)
			total = cn.get_subtree_weight()
			if not counts.get(total):
				counts[total] = [c]
			else:
				counts[total].append(c)
		assert len(counts.keys()) == 2, "more than 2 different subtree weights"
		good_weight = 0
		bad_weight = 0
		for weight, lst in counts.items():
			if len(lst) == 1:
				assert bad_weight == 0, "bad weight already set"
				bad_weight = weight
			else:
				assert good_weight == 0 or good_weight == weight, "good weight something else"
				good_weight = weight
		to_add = good_weight - bad_weight 
		target_weight = nodes.get(counts[bad_weight][0]).weight + to_add
		return target_weight
	# otherwise, recurse down the unbalanced tree
	else:
		assert child_balances.count(False) == 1, "can't have more than one unbalanced subtree"
		idx = child_balances.index(False)
		return find_imbalance(nodes, node.children[idx])


def run(lines):
	nodes = {}
	for l in lines:
		l = l.strip()
		node_def = l
		children = []
		if " -> " in l:
			parts = l.split(" -> ")
			node_def = parts[0]
			children = parts[1].strip().split(", ")
		name = node_def.split(' (')[0]
		weight = int(node_def.split(' (')[1][:-1])
		nodes[name] = Node(name, weight, children)

	for name in nodes.keys():
		n = nodes[name]
		for c in n.children:
			nodes[c].set_parent(name)

	root = None
	for name,node in nodes.items():
		if node.parent is None:
			assert root is None
			root = name

	set_child_weights(nodes, root)


	return find_imbalance(nodes, root)
	
	

if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)

