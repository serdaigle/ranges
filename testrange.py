import unittest
from range import Ranges, Node

class TestRange(unittest.TestCase):

	###################
	# ADD tests
	def test_add(self):
		#Adding invalid range to an empty tree	
		ranges = Ranges()
		ranges.add(6,6)
		self.assertEqual(ranges.tree, None)
		ranges.add(10,6)
		self.assertEqual(ranges.tree, None)
		
		#Adding valid range to an empty tree	
		ranges.add(4,6)
		self.assertEqual(ranges.tree.range, (4,6))
		ranges.add(1,3)
		self.assertEqual(ranges.tree.left.range, (1,3))
		ranges.add(10,15)
		self.assertEqual(ranges.tree.right.range, (10,15))
		
		
	def test_add_examples(self):
		ranges = Ranges()
		ranges.add(1,2)
		ranges.add(3,5)
		result = ranges.get(0,10)
		self.assertEqual(result, [(1,2), (3,5)])
		
		ranges = Ranges()
		ranges.add(1,6)
		ranges.add(3,5)
		result = ranges.get(0,10)
		self.assertEqual(result, [(1,6)])
		
		ranges = Ranges()
		ranges.add(1,4)
		ranges.add(3,5)
		result = ranges.get(0,10)
		self.assertEqual(result, [(1,5)])
		
	def test_leftmerge(self):
		ranges = Ranges()
		ranges.add(5,6)
		ranges.add(1,2)
		ranges.add(-1,0)
		ranges.add(3,4)
		ranges.add(10,15)
		ranges.add(8,9)
		result = ranges.get(-100,100)
		self.assertEqual(result, [(-1,0), (1,2), (3,4), (5,6),(8,9), (10,15)])
		
		ranges.add(3,6)
		result = ranges.get(-100,100)
		self.assertEqual(result, [(-1,0), (1,2), (3,6),(8,9), (10,15)])

	def test_rightmerge(self):
		ranges = Ranges()
		ranges.add(5,6)
		ranges.add(1,2)
		ranges.add(-1,0)
		ranges.add(3,4)
		ranges.add(10,15)
		ranges.add(7,9)
		result = ranges.get(-100,100)
		self.assertEqual(result, [(-1,0), (1,2), (3,4), (5,6),(7,9), (10,15)])
		
		ranges.add(1,4)
		result = ranges.get(-100,100)
		self.assertEqual(result, [(-1,0), (1,4),(5,6),(7,9), (10,15)])

	
	
	###################
	# Delete tests
	def test_delete(self):
		#Adding invalid range to an empty tree	
		ranges = Ranges()
		ranges.add(4,6)
		ranges.add(10,20)
		ranges.add(7,9)
		ranges.add(25,30)
		ranges.add(21,24)
		ranges.add(1,3)
		ranges.delete(1,3)
		self.assertEqual(ranges.tree.left, None)
		
		ranges.add(1,3)
		ranges.add(-10,-5)
		ranges.delete(15,22)
		self.assertEqual(ranges.tree.right.range, (10, 15))
		self.assertEqual(ranges.tree.right.right.left.range, (22, 24))
		
	def test_delete_examples(self):
		#Adding invalid range to an empty tree	
		ranges = Ranges()
		ranges.add(1,6)
		ranges.delete(-3,-1)
		results = ranges.get(-100,100)
		self.assertEqual(results, [(1,6)])

		ranges.delete(-1,10)
		results = ranges.get(-100,100)
		self.assertEqual(results, [])
		
		ranges.add(1,6)
		ranges.delete(4,10)
		results = ranges.get(-100,100)
		self.assertEqual(results, [(1,4)])
	
	###################
	# Get API tests
	def test_get(self):
		ranges = Ranges()
		ranges.add(5,6)
		ranges.add(1,2)
		ranges.add(-1,0)
		ranges.add(3,4)
		ranges.add(10,15)
		ranges.add(7,9)
		result = ranges.get(1,6)
		self.assertEqual(result, [(1,2), (3,4),(5,6)])
		
	def test_get_examples(self):
		ranges = Ranges()
		ranges.add(1,3)
		ranges.add(5,7)
		result = ranges.get(4,5)
		self.assertEqual(result, [])
		
		ranges = Ranges()
		ranges.add(1,3)
		ranges.add(5,6)
		result = ranges.get(4,6)
		self.assertEqual(result, [(5,6)])

		result = ranges.get(2,9)
		self.assertEqual(result, [(1,3),(5,6)])
		
	
if __name__ == '__main__':
    unittest.main()