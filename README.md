# ranges
A data structure that stores ranges. A range where the start and end value are equal to be invalid, seeing as it would be a range of 0 indexes. Any ranges where the start value is larger than the end value will be ignored. 

When ranges overlap, they will be merged upon adding.

# range.py
This file contains the data structure which helps us keep track and manipulate ranges.I decided to use a binary tree to store the ranges. This makes search time and updating go to an average of O(log n), though we could hit O(n) time complexity if the tree degenerates into a list.

## Add method
The add method calls upon the _addToTree() method which walks through the tree until it finds the correct placement of the new range. If this new placement is an empty list, it simply adds the new range. Otherwise, it must update the current range and evaluate its children. I divided this evaluation into right and left child analysis. _addToTree() contains a while
loop that has, on average, O(log n) time complexity. When it finishes, it can call upon _leftMerge() and/or _rightMerge(), both of which are also O(logn) on average. 

## Delete method
The delete method calls upon the inner function deleteFromTree() which has a time complexity O(log n), but that could be O(n) in worst cases, for example when all nodes are within the range that must be deleted.

## Get method
The get method calls upon the recursive inner function searchTree() which can have a time complexity O(log n) if there is only one range that matches the search, but that could be O(n) if all nodes match the requested range and must be evaluated.

# testrange.py
In order to test my data structure, I used unit tests to verify the outputs of each of the methods.
