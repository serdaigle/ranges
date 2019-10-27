from typing import List

class Node: 
	def __init__(self,data): 
		self.left = None
		self.right = None
		self.range = data 

class Ranges(object):

	def __init__(self):
		self.tree = None
	
	def _rangeCheck(self, start:int, end:int) -> bool:
		"""
		Check if a given range is valid. It is a assumed that a valid range will have 
		an initial value that is smaller than the end value. If both values are equal, 
		it is not considered a valid range.
		:param start: Start of the range (inclusive)
		:param end: End of the range (exclusive)
		:return True if the range is valid False otherwise
		"""
		return start < end
			
	
	def display(self):
		"""
		Debugging function, displays the tree structure containing the stored ranges.
		"""
		def displayTree(node:Node):
			if node:
				displayTree(node.left)
				print(node.range)
				displayTree(node.right)
		print("Displaying tree:")
		displayTree(self.tree)
		
	def _findIntersect(self, node:Node, start:int, end:int) -> (Node, Node, bool):
		parent = None
		isLeft = False
		while node:
			if end <= node.range[0]:
				parent = node
				node = node.left
				isLeft = True
			elif start >= node.range[1]:
				parent = node
				node = node.right
				isLeft = False
			else:
				return (node, parent, isLeft)
		if not node:
			return None
			
			
###########################################################################	
		
		
	def get(self, start:int, end:int) -> List:
		"""
		Returns a list of ranges contained in the data that intersect with
		'start' and 'end'. Complexity O(log n), could be O(n) in the worst case.
		:param start: Start of the range (inclusive)
		:param end: End of the range (exclusive)
		:return List of ranges that intersect
		"""
		results = []
		def searchTree(node) -> List:
			if not node:
				return None
			if end <= node.range[0]:
				searchTree(node.left)
			elif start >= node.range[1]:
				searchTree(node.right)
			else:
				if start < node.range[0]:
					searchTree(node.left)
				results.append(node.range) 
				if end > node.range[1]:
					searchTree(node.right)
					
		if self._rangeCheck(start, end) and self.tree :
			x = self._findIntersect(self.tree, start, end)
			if x:
				(node, parent, isLeft) = x
				searchTree(node)	
		return results		

	
###########################################################################	

	def add(self, start:int, end:int):
		"""
		Adds a new range into the data structure from 'start' to 'end'. 
		Internally, it calls the inner function _addToTree.
		:param start: Start of the range (inclusive)
		:param end: End of the range (exclusive)
		"""
		if not self._rangeCheck(start, end):
			return
		if not self.tree:
			self.tree = Node((start,end)) 
		else :
			self._addToTree(self.tree, start, end)
	
	def _addToTree(self, node:Node, start:int, end:int):
		"""
		This function searches through the tree until it finds a range that 
		intersects with the new range we want to add. Upon finding it, it 
		calls upon _leftMerge and/or _rightMerge to update the current node, 
		as well as it's children and exits.
		:param node: Node containing the range we are evaluating.
		:param start: Start of the range (inclusive)
		:param end: End of the range (exclusive)
		"""
		done = False
		merge = False
		while not done:
			# Check if new range is smaller than current range
			if end <= node.range[0] :
				if node.left:
					node = node.left
				else:
					node.left = Node((start,end))
					done = True
			# Check if new range is larger than current range
			elif start >= node.range[1]:
				if node.right:
					node = node.right
				else:
					node.right = Node((start,end))
					done = True
			# New range intersects with current range
			else:
				merge = True
				done = True
		if merge:
			if start < node.range[0]:
				self._leftMerge(node, start, end)
			if end > node.range[1]:
				self._rightMerge(node, start, end)
				
	
	
	def _leftMerge(self, node:Node, start:int, end:int):
		"""
		This function updates the starting point of the range, and evaluates 
		the left side of the tree starting from 'node'.  Average time complexity 
		is O(log n). Can be to O(n) in case the tree degenerates into a list.
		:param node: Node containing the range we are evaluating.
		:param start: Start of the range (inclusive)
		:param end: End of the range (exclusive)
		"""
		min = start 
		prev = node
		tmp = node.left
		isLeftChild = True 
		while tmp :
			if min >= tmp.range[1]:
				prev = tmp
				tmp = tmp.right
				isLeftChild = False
			else:
				if min > tmp.range[0]:
					min = tmp.range[0]
				tmp = tmp.left
				if isLeftChild:
					prev.left = tmp
				else:
					prev.right = tmp
		node.range = (min,node.range[1])
		
		
	def _rightMerge(self, node: Node, start:int, end:int):
		"""
		This function updates the end point of the range, and evaluates the 
		right side of the tree starting from "node". Complexity O(log n), 
		could be O(n) in the worst case. 
		:param node: Node containing the range we are evaluating.
		:param start: Start of the range (inclusive)
		:param end: End of the range (exclusive)
		"""
		max = end 
		prev = node
		tmp = node.right
		isRightChild  = True
		while tmp:
			if max <= tmp.range[0]:
				prev = tmp
				tmp = tmp.left
				isRightChild = False
			else:
				if max < tmp.range[1]:
					max = tmp.range[1]
				tmp = tmp.right
				if isRightChild:
					prev.right = tmp
				else:
					prev.left = tmp
		node.range = (node.range[0], max)



###########################################################################		
	def delete(self, start:int, end:int):
		"""
		Deletes the range from 'start' to 'end' from the data structure. Internally, 
		it calls upon the inner function 'delete' which has an average time complexity
		O(log n); it could be O(n) in the worst case. 
		:param start: Start of the range (inclusive)
		:param end: End of the range (exclusive)
		"""
		def deleteFromTree(parent:Node, node:Node, isLeft:bool, start:int, end:int):
			if not node:
				return
			if end <= node.range[0] :
				deleteFromTree(node, node.left, True, start, end)
			elif start >= node.range[1]:
				deleteFromTree(node, node.right,False, start, end)
			# Intersects with deletion range
			else:
				newLeft = None
				newRight = None
				
				if start > node.range[0]: 
					newLeft = Node((node.range[0], start))
					newLeft.left = node.left
				else:
					newLeft = node.left
					
				if end < node.range[1]: 
					newRight = Node((end, node.range[1]))
					newRight.right = node.right
				else:
					newRight = node.right
					
				if newLeft:
					tmp = newLeft
					while tmp.right:
						tmp = tmp.right
					tmp.right = newRight
				else:
					newLeft = newRight
				
				# We are dealing with root (no parent)
				if not parent:
					self.tree = newLeft
				# Parent is not root
				else:
					if isLeft:
						parent.left = newLeft
					else:
						parent.right = newLeft
				deleteFromTree(parent, newLeft, isLeft, start, end)

	
		if self._rangeCheck(start, end) and self.tree:			
			x = self._findIntersect(self.tree, start, end)
			if x:
				(node, parent, isLeft) = x
				deleteFromTree(parent, node, isLeft, start, end)	

		

		
	