class Node:
    """
    A object for storing a single node a linked list 
    Stores data and link to the next node in the list. 
    """
    data = None
    nextNode = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" %self.data
    

class linkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        """
        Returns number of node in the list 
        """
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.nextNode
        return count

    def prepend(self,data):
        """
        Adds new node containing data at the head of the list
        Take O(1) / constant time
        """
        newNode = Node(data)
        newNode.nextNode = self.head
        self.head = newNode
    
    
    def search(self,key):
        """
        Search for the first node containing data that matches the key 
        Return the node or None if not found
        Takes O(N)/linear time
        """

        current = self.head
        while current:
            if current.data == key:
              return current
            else:
              current = current.nextNode
        return None
    
    def insert(self,data,index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1)/Constant time
        Searching for node at insertion point takes O(n)/Linear time
        Overall takes O(N)/Linear time
        """
        if index == 0:
            self.add(data)
            return
        
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
               current = current.nextNode
               position -= 1
            
            prevNode = current
            nextNode = current.nextNode

            prevNode.nextNode = new
            new.nextNode = nextNode



    def __repr__(self):
        """
        returns a sgring representation of the linked list
        Takes O(n) / linear time
        """

        nodes = []
        current = self.head

        while current:
            if current == self.head:
                nodes.append("[Heads: %s]" %current.data)
            elif current.nextNode == None:
                 nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" %current.data)

            current = current.nextNode
        return "-> ".join(nodes)