from linked_list.LinkedList import LinkedList

def printCurrentValues():
    print( 'Lenght: ' , ll.length )
    print( 'Head: ' , ll.head.value )
    print( 'Tail: ' , ll.tail.value )

# Create a new LinkedList
ll = LinkedList()

#printCurrentValues()

#print( 'None existing values: ' , ll.get( 0 ) )

#ll.append(1)

#print( 'Existing Value: ' , ll.get( 0 ).value ) 

print( 'Inserting Value: ' , ll.insert( 0 , 2 ) )
print( 'Inserting Value: ' , ll.insert( 1 , 3 ) )

ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print( 'Deleted Node at Index: 2 -> ', ll.deleteIndex( 2 ).value )
