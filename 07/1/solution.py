
from collections import namedtuple

class Node:
	def __init__(self, name, weight, children):
		self.name = name
		self.weight = weight
		self.children = children
		self.parent = None

	def set_parent(self, parent):
		self.parent = parent


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

	return root
	

if __name__ == "__main__":
	with open("input.txt") as f:
		lines = f.readlines()
		print run(lines)

