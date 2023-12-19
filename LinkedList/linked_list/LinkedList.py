from node.Node import Node

class LinkedList():
    
    # Default values of the LinkedList
    length = 0
    head = None
    tail = None
    
    def __init_( self ):
        pass
    
    # Method to add a node to the end of the LinkedList
    def append( self , value ):
        newNode = Node( value )
        
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
            
        self.tail = newNode
        self.length += 1
    
    # Method to add a node to the beginning of the LinkedList
    def prepend( self , value ):
        newNode = Node( value )
        
        if self.head is None: self.append( newNode.value )
        
        temp = self.head
        newNode.next = temp
        self.head = newNode
        self.length += 1
    
    # Method to delete the first node of the LinkedList
    def deleteFirst( self ):
        temp = None
        
        if self.head is not None:
            temp = self.head
            self.head = temp.next
            self.length -= 1       
        
        return temp
    
    # Method to delete the last node of the LinkedList
    def deleteLast( self ):       
        if self.head is None: return None
        if self.head.next is None: return self.deleteFirst()
        
        temp = None        
        current = self.head
        
        while current.next.next is not None:
            current = current.next
        
        temp = current.next
        current.next = None
        self.tail = current
        length -= 1
                
        return temp
    
    # Method to get the node at the given index
    def get( self , index ):
        if index < 0 or index >= self.length: return None
        
        count = 0
        temp = self.head
        
        while count != index:
            temp = temp.next
            count += 1  
        
        return temp
    
    # Method to insert a node at the given index
    def insert( self , index , value ):
        if index < 0 or index > self.length: return None
        if index == 0 and self.length == 0 : return self.append( value )
        
        newNode = Node( value )
        temp = self.get( index - 1 )
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1