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
    

