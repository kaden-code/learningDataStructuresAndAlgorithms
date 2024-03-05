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