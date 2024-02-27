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
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.nextNode
        return count

