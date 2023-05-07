
#Reverse a linked list in groups of given size
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	def reverse(self, head, k):		
		if head == None:
		return None
		current = head
		next = None
		prev = None
		count = 0
		while(current is not None and count < k):
			next = current.next
			current.next = prev
			prev = current
			current = next
			count += 1
		if next is not None:
			head.next = self.reverse(next, k)
		return prev
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data,end=' ')
			temp = temp.next
llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print("Given linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 3)
print ("\nReversed Linked list")
llist.printList()

#Merge a linked list into another linked list at alternate positions.
class Node(object):
	def __init__(self, data:int):
		self.data = data
		self.next = None
class LinkedList(object):
	def __init__(self):
		self.head = None
		
	def push(self, new_data:int):
		new_node = Node(new_data)
		new_node.next = self.head
		# 4. Move the head to point to new Node
		self.head = new_node
	def printList(self):
		temp = self.head
		while temp != None:
			print(temp.data)
			temp = temp.next
	def merge(self, p, q):
		p_curr = p.head
		q_curr = q.head
		while p_curr != None and q_curr != None:
			p_next = p_curr.next
			q_next = q_curr.next
			q_curr.next = p_next # change next pointer of q_curr
			p_curr.next = q_curr # change next pointer of p_curr
			p_curr = p_next
			q_curr = q_next
			q.head = q_curr
llist1 = LinkedList()
llist2 = LinkedList()
llist1.push(3)
llist1.push(2)
llist1.push(1)
llist1.push(0)
for i in range(8, 3, -1):
	llist2.push(i)
print("First Linked List:")
llist1.printList()
print("Second Linked List:")
llist2.printList()
llist1.merge(p=llist1, q=llist2)
print("Modified first linked list:")
llist1.printList()
print("Modified second linked list:")
llist2.printList()

# In an array, Count Pairs with given sum
def getPairsCount(arr, n, sum):
	count = 0 
	for i in range(0, n):
		for j in range(i + 1, n):
			if arr[i] + arr[j] == sum:
				count += 1

	return count
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
	getPairsCount(arr, n, sum))

#Find duplicates in an array

def find(array):
    duplicate_element_array = []
    for i in array:
        if array.count(i) > 1 and i not in duplicate_element_array:
            duplicate_element_array.append(i)
    print("Duplicate element in an array : ", end="")
    for i in sorted(duplicate_element_array):
        print(i, end=" ")
array = [-1, 8, 1, 8, -1, 5, 1, -3]
print("Array= ", array)
find(array)

#Find the Kth largest and Kth smallest number in an array

from typing import List
class Solution:
    def kth_Largest_And_Smallest_By_AscendingOrder(self, arr: List[int], k: int) -> None:
        arr.sort()
        n = len(arr)
        print(f"kth Largest element {arr[n - k]}, kth Smallest element {arr[k - 1]}")
if __name__ == "__main__":
    arr = [1, 2, 6, 4, 5, 3]
    Solution().kth_Largest_And_Smallest_By_AscendingOrder(arr, 3)

#Move all the negative elements to one side of the array
def shift_negatives(arr) :
    first_positive = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[first_positive]
            arr[first_positive]= temp
            
            first_positive += 1
    return arr
 
arr = input().split()
arr = [int(i) for i in arr]
print("Original Array:", arr)

rearranged_array = shift_negatives(arr)
print("Rearranged Array:", rearranged_array)

#Reverse a string using a stack data structure

def createStack():
	stack = []
	return stack
def size(stack):
	return len(stack)
def isEmpty(stack):
	if size(stack) == 0:
		return true
def push(stack, item):
	stack.append(item)
def pop(stack):
	if isEmpty(stack):
		return
	return stack.pop()
def reverse(string):
	n = len(string)
	stack = createStack()
	for i in range(0, n, 1):
		push(stack, string[i])

	string = ""
	for i in range(0, n, 1):
		string += pop(stack)
	return string
string = "GeeksQuiz"
string = reverse(string)
print("Reversed string is " + string)

#Evaluate a postfix expression using stack
class Evaluate:

	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		self.array = []
	def isEmpty(self):
		return True if self.top == -1 else False
	def peek(self):
		return self.array[-1]
	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"
	def push(self, op):
		self.top += 1
		self.array.append(op)
	def evaluatePostfix(self, exp):
		for i in exp:
			if i.isdigit():
				self.push(i)
			else:
				val1 = self.pop()
				val2 = self.pop()
				self.push(str(eval(val2 + i + val1)))
		return int(self.pop())
if __name__ == '__main__':
	exp = "231*+9-"
	obj = Evaluate(len(exp))
	print("postfix evaluation: %d" % (obj.evaluatePostfix(exp)))

#Implement a queue using the stack data structure

class Queue:
	def __init__(self):
		self.s1 = []
		self.s2 = []
	def enQueue(self, x):
		while len(self.s1) != 0:
			self.s2.append(self.s1[-1])
			self.s1.pop()
		self.s1.append(x)
		while len(self.s2) != 0:
			self.s1.append(self.s2[-1])
			self.s2.pop()
	def deQueue(self):
		if len(self.s1) == 0:
			print("Q is Empty")
		x = self.s1[-1]
		self.s1.pop()
		return x
if __name__ == '__main__':
	q = Queue()
	q.enQueue(1)
	q.enQueue(2)
	q.enQueue(3)

	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())


