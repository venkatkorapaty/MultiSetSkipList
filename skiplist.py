import random


class SLNode():
    '''
    A base node class for SkipLists
    '''
    def __init__(self, down=None):
        '''(SLNode, SLNode) -> NoneType
        Initiates the base node with a down attribute, data, and a node type
        to keep track of what type of node it is
        '''
        self.down = down
        self.data = None
        self.node_type = None

    def __str__(self):
        '''
        '''
        return str(self.data)


class TailNode(SLNode):
    '''
    The tail node put at the end of the SkipList
    '''
    def __init__(self, down=None):
        '''(TailNode, TailNode) -> NoneType
        Initiates a tail node with the same properties of base node
        and a node type of tail
        '''
        SLNode.__init__(self, down)
        self.node_type = 'tail'


class HeadNode(SLNode):
    '''
    The head node used as the first node of each level for SkipLists
    '''
    def __init__(self, next_node=None, down=None):
        '''(HeadNode, HeadNode or TailNode, HeadNode) -> NoneType
        Initiates the headnode which has the same properties as SLNode
        except it's node type is head
        '''
        TailNode.__init__(self, down)
        self.next_node = next_node
        self.node_type = 'head'


class MiddleNode(HeadNode):
    '''
    The middle node for the middle of SkipLists that actually hold the data
    '''
    def __init__(self, data, next_node=None, down=None):
        '''(MiddleNode, Object, MiddleNode or TailNode, MiddleNode or TailNode)
        -> NoneType
        Initiates the middlenode which has the same properties as HeadNode
        except it's node type is head and holds data
        '''
        HeadNode.__init__(self, next_node, down)
        self.data = data
        self.node_type = 'middle'


class SkipList():
    '''
    This is a SkipList class that uses the idea of linked lists and nodes
    to store data.
    '''
    def __init__(self, probability=0.5):
        '''
        '''
        # make a tail node
        self.tail = TailNode()
        # make a head node and point it to the tail node
        self.head = HeadNode(self.tail, None)
        self.probability = probability

    def __str__(self, current=None):
        '''(SkipList) -> str
        Returns a string of SkipList
        '''
        # starts from head
        if current is None:
            current = self.head
        # calls helper function to get the string of the middle nodes
        string = self.__str__helper(current)
        # adds tail node to the end and a new line
        string += 'tail\n'
        # adds head node at the beginning
        string = ('head->' + string)
        if current.down is None:
            # if it reaches the end of a list, returns the string
            return string
        else:
            # else it keeps recursing to add the bottom levels to the string
            return string + self.__str__(current.down)

    def __str__helper(self, current):
        '''(SkipList, HeadNode or MiddleNode) -> str
        This function returns the string of the middle nodes in a list
        '''
        # if it reached the end of the list, returns an empty string
        if isinstance(current.next_node, TailNode):
            return ''
        # else it keeps recursing down the level adding onto the string
        else:
            return str(current.next_node) + '->' + \
                self.__str__helper(current.next_node)

    def __len__(self, current=None):
        '''(SkipList, MiddleNode) -> int
        Returns the number of nodes on the bottom level, being the length
        '''
        # starts from the head of the bottom level
        if current is None:
            current = self.bottom_level()
        # if the node after is a tail, do not add onto the length
        if isinstance(current.next_node, TailNode):
            return 0
        # else it keeps recursing down the level adding to the int
        else:
            return 1 + self.__len__(current.next_node)

    def search_vert(self, obj, current=None):
        '''(SkipList, Object, Node) -> HeadNode or MiddleNode or NoneType
        This function searches down the list calling a helper function to
        search for a node on the list. Returns None if it is not found.
        '''
        # starts from the head of the list
        if current is None:
            current = self.head
        # searches the skip list level
        current_middle = self.search_hori(obj, current)
        # returns none, meaning value was not found
        if current_middle is None:
            return None
        # if the value returned has a tail node after it, it means it must
        # if a tail is returns, it means it must start from the next head node
        elif isinstance(current_middle, TailNode):
            return self.search_vert(obj, current.down)
        # if the value was found, return the node before it
        elif current_middle.next_node.data is obj:
            return current_middle

    def search_hori(self, obj, current):
        '''(SkipList, Object, HeadNode or MiddleNode) -> HeadNode or MiddleNode
        or NoneType
        Searches a level for a node and returns the one behind the desired
        one. Returns None if not found
        '''
        # if the value was found or if the next value is a tail, meaning the
        # value is not on this level
        if isinstance(current.next_node, TailNode):
            # returns none as the end of the list has been reached
            if current.down is None:
                return None
            elif current.node_type == 'middle':
                if current.data < obj:
                    return self.search_hori(obj, current.down)
            # case where the level is only a head and node
            elif isinstance(current, HeadNode):
                return self.tail
            # case where the list must be recursed down
            elif current.data < obj:
                return self.search_hori(obj, current.down)
        # returns the node before the wanted one
        if current.next_node.data is obj:
            return current
        # recurses the current level
        elif current.next_node.data < obj:
            return self.search_hori(obj, current.next_node)
        # recurses to the next level underneath
        elif current.next_node.data > obj:
            if current.down is None:
                return None
            return self.search_hori(obj, current.down)

    def remove_empty_levels(self, current):
        '''(SkipList, HeadNode) -> NoneType
        This function removes any empty levels in the list, meaning there
        exists levels that only contain a head and tail node, zero middle nodes
        should be present, with the exception that there is only one level
        with no middle nodes, then nothing is done
        '''
        # if there is no level beneath, does nothing
        if current.down is None:
            return None
        # if the current level has is an empty level, it gets removed
        elif isinstance(current.next_node, TailNode):
            # makes the new self.head
            self.head = current.down
            # removes the links from the removed head
            current.down = None
            current.next_node = None

    def remove(self, obj, current=None):
        '''(SkipList, Object, HeadNode) -> NoneType
        This function recursively removes the wanted value/node from the
        SkipList
        '''
        if current is None:
            # start from beginning of list
            current = self.head
        # gets the node before wanted node to be removed
        node = self.search_vert(obj, current)
        # checks for the occurrence of the value
        if node is not None:
            temp_node = node.next_node.next_node
            # the node being removed down value points to none
            node.next_node.down = None
            # the node being removed next value points to none
            node.next_node.next_node = None
            # the node before the removed node points to the node after the
            # removed node
            node.next_node = temp_node
            if current.down is None:
                return None
            # recurses to remove the nodes on lower levels
            self.remove(obj, current.down)
        # removes empty levels after node is removed
        self.remove_empty_levels(self.head)

    def insert_amount(self, amount=1):
        '''(SkipList, int) -> int
        Returns the amount of times a node should be inserted
        '''
        rand = random.random()
        # stops increasing amount if random is greater then or equal to zero
        if rand >= self.probability:
            return amount
        # calls increase amount by 1 and recurses
        else:
            return self.insert_amount(amount + 1)

    def level_amount(self, levels=1, current=None):
        '''(SkipList, int, HeadNode) -> int
        Returns the amount of levels a SkipList has
        '''
        # starts from the head of the list
        if current is None:
            current = self.head
        # if there is not level underneath, return levels
        if current.down is None:
            return levels
        # if there is a level underneath, adds 1 to levels and recurses
        else:
            return self.level_amount(levels + 1, current.down)

    def add_levels(self, amount):
        '''(SkipList, int) -> NoneType
        Adds levels to the SkipList
        '''
        # no levels need to be added
        if amount == 0:
            return None
        # creates a head node
        temp = HeadNode()
        # creates the link to the current self.head
        temp.down = self.head
        # creates the link to the tail of the list
        temp.next_node = self.tail
        # makes the new self.head the head node created
        self.head = temp
        # recurses reducing the amount of levels needed to be added by 15
        self.add_levels(amount - 1)

    def insert(self, obj):
        '''(SkipList, Object) -> NoneType
        Inserts the wanted value into the SkipList
        '''
        # returns amount of times to insert object
        amount_insert = self.insert_amount() + 1
        # returns the amount of levels in the function
        levels = self.level_amount()
        current = self.head
        if amount_insert > levels:
            self.add_levels(amount_insert - levels)
            current = self.head
        elif levels > amount_insert:
            # makes current equal to the head node of the level it should
            # start inserting from
            while levels - amount_insert > 0:
                levels -= 1
                current = current.down
        temp = amount_insert
        # while the amount to insert the node is greater than 0
        while temp != 0:
            temp -= 1
            self.insert_helper(obj, current)
            current = current.down
        # if amount of levels is greater than amount of nodes inserted, it must
        # start at the level it was inserted
        if levels > amount_insert:
            current = self.head
            while levels - amount_insert > 0:
                levels -= 1
                current = current.down
            self.point_down(obj, current)
        # else it starts pointing down all the inserted nodes
        else:
            self.point_down(obj, self.head)

    def insert_helper(self, obj, current):
        '''(SkipList, Object, HeadNode or MiddleNode) -> NoneType
        This function creates the node to be inserted and inserts it in the
        current level
        '''
        # if the next node is a tail node, the value gets adde before it
        if isinstance(current.next_node, TailNode):
            current.next_node = MiddleNode(obj, self.tail)
        # else if the value is less than or equal to  the next node, it will
        # get inserted before that node
        elif current.next_node.data >= obj:
            current.next_node = MiddleNode(obj, current.next_node)
        # else if the value is greater than the next, continue recursing
        else:
            self.insert_helper(obj, current.next_node)

    def point_down(self, obj, current):
        '''(SkipList, Object, HeadNode) -> NoneType
        This function connects column nodes that have the same value
        if it already has not been connected
        '''
        # if there are no more levels underneath the current one
        if current.down is None:
            return None
        # if there there is only one level underneath
        elif current.down.down is None:
            # finds the node before the desired one
            current_middle = self.search_vert(obj, current)
            # finds the node that should be underneath it
            current_middle_down = self.search_vert(obj, current.down)
            # makes the desired node down point to the node underneath it
            current_middle.next_node.down = current_middle_down.next_node
        # else same process as above but recurses because there are more levels
        # to connect the nodes column-wise
        else:
            current_middle = self.search_vert(obj, current)
            current_middle_down = self.search_vert(obj, current.down)
            current_middle.next_node.down = current_middle_down.next_node
            self.point_down(obj, current.down)

    def bottom_level(self, current=None):
        '''(SkipList, HeadNode) -> NoneType
        Returns the head of the bottom level of a SkipList
        '''
        # starts from the first level
        if current is None:
            current = self.head
        # if there are no more levels underneath
        if current.down is None:
            return current
        # else recurses until it gets to the bottom and returns bottom level
        else:
            return self.bottom_level(current.down)

    def occurrences(self, obj, current=None):
        '''(SkipList, Object, HeadNode or MiddleNode) -> NoneType
        Returns the number of occurrences an element is in the node
        at the bottom level
        '''
        # starts from the head of the bottom level
        if current is None:
            current = self.bottom_level()
        # if the end of the level has been reached
        if isinstance(current.next_node, TailNode):
            return 0
        # if the next node's data is equal to the value, increase occurrence
        # by 1 and recurse
        elif current.next_node.data == obj:
            return 1 + self.occurrences(obj, current.next_node)
        # if the next node has a value greater than the value returns 0
        # or value is not in the list
        elif current.next_node.data > obj:
            return 0
        # continues recursing if the next node is is a
        else:
            return self.occurrences(obj, current.next_node)

    def level_string(self, current=None):
        '''(SkipList, HeadNode or MiddleNode) -> NoneType
        Returns the string of the bottom level of the SkipList
        '''
        # starts from the head of the bottom level of the SkipList
        if current is None:
            current = self.bottom_level()
        # if the next node is a tail node, returns an empty string
        if isinstance(current.next_node, TailNode):
            return ''
        # deals with lists that contain strings
        elif type(current.next_node.data) == str:
            # if the next next node is a tail node it stops recursing
            if isinstance(current.next_node.next_node, TailNode):
                return "\'" + current.next_node.data + "\'"
            # else it continues recursing with a coma in the string to show
            # seperation in the string output
            return "\'" + current.next_node.data + "\', " + self.level_string(
                current.next_node)
        # deals with numbers
        else:
            # if the next next node is a tail, stops recursing
            if isinstance(current.next_node.next_node, TailNode):
                return str(current.next_node.data)
            # else it continues recursing with a coma seperating the values
            else:
                return str(current.next_node.data) + ", " + self.level_string(
                    current.next_node)
