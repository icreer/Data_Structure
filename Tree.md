# Tree

## Questions

###	What is the purpose of the data structure?
A Tree is like a linked list with nodes that are connected together by pointers. THough unlike a linked list a tree can hav multiple different nodes. 

The Advantages of a tree are that a tree reflects the data structural connections, tree is used for hierarchy, it offers an efficient search, it offers efficient insertion procedure, and tress are flexible.

###	What is the performance of the data structure (Big O)?
Now the performance of a tree is depednent on many factors. In general if a tree is balance  then the the performance is O(log N).

###	What kind of problem can be solved using the data structure?
Trees are really powerful. Some of the problem that a tree can be used to in storing hierarchecal data, create faster searching through the data, and can help with indexing in a database. With the amount of differne trees out there probalbly tree out there that could solve your problem if it is dealing with data.

###	How would the data structure be used in Python (recursion)?
Here is the basic of a Binary Search Tree
```python
class BST:
    class Node:

        def __init__(self, data):
           
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
       
        self.root = None

    def insert(self, data):
        
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root 
   
    def _insert(self, data, node):
       
        if node.data == data:
            return True
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
           
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
```

###	What kind of errors are common when using the data structure?
Well a common error that is that the tree is unbalance and there is a recerson error in the set up of said tree.

###	What are the different types of trees?
There a ton of different types of trees but here are some of the major gouping of trees:
* Binary Trees
* B-trees
* Heaps
* Bit-slice trees
* Multi-way trees
* Space-partitioning trees
* Application-specific trees
###	What are nodes and how do they make a tree?
A node is a basic unit of a data structure. So I have a piece of data link a list of corradant of a bunch of objects. A node would be a individal corradant. How  they make a tree is though how pointers point to certenat nodes witch leads nodes being linked togeather.

###	What are subtrees?
Well lets go over some basic tree vocab. So the top node is called the root. So a node is not connect to no other nodes is called a leaf. A parent node are a node that has connecting nodes. As a child nodes are the nodes that conect to the parent. So that leads us to What is a Subtrees? So in simple terms a subtree are any group of nodes that are left and right of the parent node.

###	Can a node have more than two branches?
Yes out side of a binary tree most trees can have more then two branches or nodes. 
The main reason I say binary tree  by deffinition is a tree that links no more than two other nodes.

###	Do trees need to be balance?
Well they don't nessaly need to be balanceed but if a tree is not balance it can really hurts the efficienty of the tree. Now what is the difference betwwen a balance and unbalcance tree? A unbalance tree is a tree that the hight is to tall for the number of data points you have. So a way to think about it is a wood plank that is balcaning on a point. Assumine that the mass of the wood plank is evenly diribluted the balance point is in the middle. So a tree needs to be like that piece of wood on said balacne point. 

## Skills

###	Know how to get the height of a tree
```python
class Node:
    def _init_(self,data):
        self.data = data
        self.left = None
        self.right = None

def hight(node):
    if node is None:
        return 0
    else:
         lhight = hight(node.left)
         rhight = hight(node.right)

         if lhight > rhight:
            return lhight+1
        else:
            return rhight+1

root = Node(50)
root.left = Node(75)
root.right = Node(25)
root.left.left = Node(85)
root.left.right = Node(65)
root.right.left = Node(35)
root.right.right = Node(15)
root.left.left.left = Node(95)
root.left.left.right = Node(80)
root.left.right.left = Node(70)
root.left.right.right = Node(55)
root.right.left.left = Node(40)
root.right.left.right = Node(30)
root.right.right.left = Node(20)
root.right.right.right = Node(10)
root.left.left.left.left = Node(100)
root.left.left.left.right = Node(90)
root.left.right.right.right = Node(60)
root.right.left.left.left = Node(45)
root.right.right.right.right = Node(5)

print(f"Height of the tree is {height(root)}")
```
###	Figure out the number of nodes at each level of a tree
```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def left_height(node):
    ht = 0
    while(node):
        ht += 1
        node = node.left
         
    return ht

def right_height(node):
    ht = 0
    while(node):
        ht += 1
        node = node.right
        
    return ht

def TotalNodes(root):
   
  # Base case
    if(root == None):
        return 0
       
     # Find the left height and the
    # right heights
    lh = left_height(root)
    rh = right_height(root)
     
     # If left and right heights are
    # equal return 2^height(1<<height) -1
    if(lh == rh):
        return (1 << lh) - 1
       
     # Otherwise, recursive call
    return 1 + TotalNodes(root.left) + TotalNodes(root.right)

root = Node(50)
root.left = Node(75)
root.right = Node(25)
root.left.left = Node(85)
root.left.right = Node(65)
root.right.left = Node(35)
root.right.right = Node(15)
root.left.left.left = Node(95)
root.left.left.right = Node(80)
root.left.right.left = Node(70)
root.left.right.right = Node(55)
root.right.left.left = Node(40)
root.right.left.right = Node(30)
root.right.right.left = Node(20)
root.right.right.right = Node(10)
root.left.left.left.left = Node(100)
root.left.left.left.right = Node(90)
root.left.right.right.right = Node(60)
root.right.left.left.left = Node(45)
root.right.right.right.right = Node(5)

print(TotalNodes(root))
```
## Problem

###	Convert a Binary Tree into a set of linked lists
```python
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
class Binary_Tree_to_Double_Linked_list:
    def _init_(self):
        self.head = None
        self.tail = None

    def convert(self, root):
        if root is None:
            return

        self.convert(root.left)

        node = root
        if self.head is None:
            self.head = node
        else:
            self.tail.right = node
            node.left = self.tail
        
        self.tail = node

        self.convert(root.right)
        return self.head

def BTEDLL(root):
    converter = Binary_Tree_to_Double_Linked_list()
    return converter.convert(root)

def print_dll(head):
    while head is not None:
        print(head.data, end = " ")
        head = head.right

root = Node(10)
root.left = Node(13)
root.right = Node(17)
root.left.left = Node(56)
root.left.right = Node(57)
root.right.left = Node(60)

head = BTEDLL(root)

print_dll(head)
```
###	You are working on collison in a game. You deciede to use a K-d tree to sort through all the corrdinats you have for all your entities.
### Now used the check collision to use the K-d tree
```python
class KDT:
    """
    Implementation of the K-Dimensional Tree (KDT) data structure.  The Node 
    class below is an inner class. To create a Node object, we will 
    need to specify KDT.Node
    """

    class Node:
        """
        Each node of the KDT will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initializes an empty KDT.
        """
        self.root = None
    
    def get_root(self):
        return self.root

    def insert(self, data):
        """
        Insert 'data' into the KDT.  If the KDT
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = KDT.Node(data)
        else:
            self._insert(data, self.root, 0)  # Start at the root

    def _insert(self, data, node, axis):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data[axis] < node.data[axis]:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = KDT.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left, abs(axis - 1))
        elif data[axis] > node.data[axis]:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = KDT.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right, abs(axis - 1))
        

    def __contains__(self, data):
        """ 
        Checks if data is in the KDT.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_KDT:
            ("5 is in the KDT")

        """
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        #try/except for when the node is NoneType
        try:
            if data == node.data:
                # The tree contains the data
                return True
            if data < node.data:
                # The data belongs on the left side.
                # Need to keep looking.  Call _contains
                # recursively on the left sub-tree.
                return self._contains(data, node.left)
            elif data > node.data:
                # The data belongs on the right side.
                # Need to keep looking.  Call _contains
                # recursively on the right sub-tree.
                return self._contains(data, node.right)
        except:
            return False
        return False


    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the KDT.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_KDT:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a 
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.  
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def get_height(self):
        """
        Determine the height of the KDT.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def _get_height(self, node):
        """
        Determine the height of the KDT.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """
        if node is None:
            return 0
        else:
            if (1 + self._get_height(node.left)) > (1 + self._get_height(node.right)):
                return 1 + self._get_height(node.left)
            else:
                return 1 + self._get_height(node.right)


    def distance_squared(self, data, point2):
        try:
            x1, y1 = data.data
        except:
            x1, y1 = data
        try:
            x2, y2 = point2

        except:
            x2 = point2
            y2 = point2           

        dx = x1 - x2
        dy = y1 - y2

        return dx * dx + dy * dy

    def closer_distance(self, data, p1, p2):
        if p1 is None:
            return p2
        if p2 is None:
            return p1

        d1 = self.distance_squared(data, p1)
        d2 = self.distance_squared(data, p2)

        if (d1 < d2 and d1 != 0) or d2 == 0:
            return p1
        else:
            return p2


    def closest_point(self,data):
        if self.root is None:
            return None
        else:
            return self._closest_point(self.root, data, 0)

    def _closest_point(self, node, data, axis):
        
        try:
            next_branch = None
            opposite_branch = None

            if data[axis] < node.data[axis]:
                next_branch = node.left
                opposite_branch = node.right
            else:
                next_branch = node.right
                opposite_branch = node.left

            axis = abs(axis - 1)
            best = self.closer_distance(data, self._closest_point(next_branch, data, axis), node.data)

            if self.distance_squared(data, best) > (data[axis] - node.data[axis]) ** 2:
                best = self.closer_distance(data, self._closest_point(opposite_branch, data, axis), best)

            return best
        except:
            return None
    


# NOTE: Functions below are not part of the KDT class above. 


def create_kdt_from_sorted_list(sorted_list):
    """
    Given a sorted list (sorted_list), create a balanced KDT.  If 
    the values in the sorted_list were inserted in order from left
    to right into the KDT, then it would resemble a linked list (unbalanced). 
    To get a balanced KDT, the _insert_middle function is called to 
    find the middle item in the list to add first to the KDT.  The 
    _insert_middle function takes the whole list but also takes a 
    range (first to last) to consider.  For the first call, the full 
    range of 0 to len()-1 used.
    """
    kdt = KDT()  # Create an empty KDT to start with     
    #Make sure that the list has elements in it
    if len(sorted_list) > 0:
        _insert_middle(sorted_list, 0, kdt)
    return kdt

def _insert_middle(sorted_list, axis, kdt):
    """
    This function will attempt to insert the item in the middle
    of 'sorted_list' into the 'KDT' tree.  The middle is 
    determined by using indicies represented by 'first' and 'last'.
    For example, if the function was called on:

    sorted_list = [10, 20, 30, 40, 50, 60]
    first = 0
    last = 5

    then the value 30 (index 2 which is the middle) would be added 
    to the 'KDT' (the insert function above can be used to do this).   

    Subsequent recursive calls are made to insert the middle from the values 
    before 30 and the values after 30.  If done correctly, the order
    in which values are added (which results in a balanced KDT) will be:

    30, 10, 20, 50, 40, 60

    This function is intended to be called the first time by 
    create_KDT_from_sorted_list.

    The purpose for having the first and last parameters is so that we do 
    not need to create new sublists when we make recursive calls.  Avoid 
    using list slicing to create sublists to solve this problem.

    """

    
    n = len(sorted_list)
    if n <= 0:
        return None
    sorted_list.sort(key = lambda sorted_list:sorted_list[axis])
    median = n // 2
    kdt.insert(sorted_list[median])


    
    axis = abs(axis - 1)
    #recursion
    #left branch
    _insert_middle(sorted_list[:median], axis, kdt)
    #right branch
    _insert_middle(sorted_list[median + 1:], axis, kdt)
    return kdt



def check_collision( coordinate_array, radius):
    # Put your code here
    pass
    


"""
Test 1
"""
radius_1 = 15

c_array1 = [(1,2),(3,5),(70,45),(34,67),(12,24),(90,32),(1,2),(34,89),(39,21)]

print(check_collision(c_array1,radius_1))
# True

"""
Test 2
"""
radius_2 = 2

c_array2 =[(45,52),(96,45),(78,5),(45,45)]

print(check_collision(c_array2,radius_2))
# False

"""
Test 3
"""
radius_3 = 50

c_array3 = [(89,5),(89,100),(89,151),(89,201),(89,260),(89,-360)]

print(check_collision(c_array3, radius_3))
# True

```
### [Solution](Tree_Student_Problem_Solution.py)
