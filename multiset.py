from skiplist import *


class MultiSet():

    def __init__(self):
        '''
        Initiates the MultiSet with a SkipList
        '''
        self.sl = SkipList()

    def __contains__(self, e):
        '''(MultiSet, Object) -> bool
        Takes in an element and a MultiSet, checks if the element is contained
        within the MultiSet
        '''
        if self.sl.search_vert(e) is not None:
            return True
        return False

    def count(self, e):
        '''(MultiSet, Object) -> int
        Takes in a MultiSet and an element, and returns the amount of times
        that element occurs in the MultiSet
        '''
        return self.sl.occurrences(e)

    def insert(self, e):
        '''(MultiSet, Object) -> NoneType
        Takes in a MultiSet and an element, and inserts the element into the
        MultiSet
        '''
        self.sl.insert(e)

    def remove(self, e):
        '''(MultiSet, Object) -> NoneType
        Takes in a MultiSet and an element, and removes the element if it
        is within the MultiSet, otherwise it does nothing
        '''
        self.sl.remove(e)

    def clear(self):
        '''(MultiSet) -> NoneType
        Takes in a MultiSet and empties it of all elements
        '''
        self.sl = SkipList()

    def __len__(self):
        '''(MultiSet) -> int
        Takes in a MultiSet and returns the total amount of elements
        '''
        return len(self.sl)

    def __repr__(self):
        '''(MultiSet) -> str
        Takes in a MultiSet and returns a string representation of that
        MultiSet
        '''
        return 'MultiSet([' + self.sl.level_string() + '])'

    def __eq__(self, other, self_current=None):
        '''(MultiSet, MultiSet) -> bool
        Takes in two MultiSets and checks if they have the same amount of each
        element, returns True if they do, False otherwise
        '''
        # if the lenght is not the same, then two MultiSets can't be equal
        if len(self) is not len(other):
            return False
        # retrieves the bottom level of self
        if self_current is None:
            self_current = self.sl.bottom_level()
        # if the next node is not a tail
        if not isinstance(self_current.next_node, TailNode):
            # checks if the amount of times a value that occurs in self
            # also occurs in other, then continues recursing through the set
            data = self_current.next_node.data
            if self.count(data) == other.count(data):
                return self.__eq__(other, self_current.next_node)
            # returns false if the amount of values of each one is different
            # among the two sets
            else:
                return False
        # the end of the set has been reached, meaning they are equal
        return True

    def __le__(self, other, self_current=None):
        '''(MultiSet, MultiSet) -> bool
        Takes in two MultiSets, checks if self is a subset of other, meaning
        if all the elements in self are also in other
        '''
        # retrieves the bottom level of self
        if self_current is None:
            self_current = self.sl.bottom_level()
        # if the next node is a tail, it has either reached the end of a set
        # or the the set has no values, either way self is a subset of other
        if isinstance(self_current.next_node, TailNode):
            return True
        # checks if the occurrence of a value is less than or equal to than
        # that of other, if true, then it continues recursion
        elif self.count(self_current.next_node.data) <= other.count(
                self_current.next_node.data):
            return self.__le__(other, self_current.next_node)
        # other wise false, and self is not a subset of other
        else:
            return False

    def __sub__(self, other):
        '''(MultiSet, MultiSet) -> MultiSet
        Takes in two MultiSets, subtracts all values in other from self and
        returns a new MultiSet
        '''
        # creates a MultiSet to return
        ms = MultiSet()
        # gets the bottom levels for the SkipLists of the MultiSets
        self_current = self.sl.bottom_level()
        other_current = other.sl.bottom_level()
        # interates through the level adding all of the values in self
        # into the MultiSet
        while not isinstance(self_current.next_node, TailNode):
            ms.insert(self_current.next_node.data)
            self_current = self_current.next_node
        # iterates through the level subtracting any values in self that
        # are in other
        while not isinstance(other_current.next_node, TailNode):
            if other_current.next_node.data in ms:
                ms.remove(other_current.next_node.data)
            other_current = other_current.next_node
        return ms

    def __isub__(self, other, other_current=None):
        '''(MultiSet, MultiSet) -> NoneType
        This takes in two Multisets, removes all the elements that are in other
        from self and mutates self instead of returning a new MultiSet
        '''
        # starts from the head of the bottom level of MultiSet's skiplist
        if other_current is None:
            other_current = other.sl.bottom_level()
        # if the next node on the bottom level is not a tail node
        if not isinstance(other_current.next_node, TailNode):
            # if the next node's element is in self, it removes it from self
            if other_current.next_node.data in self:
                self.remove(other_current.next_node.data)
            # recurses to next node
            return self.__isub__(other, other_current.next_node)
        return self

    def __add__(self, other):
        '''(MultiSet, MultiSet) -> MultiSet
        Takes in two MultiSets and adds the elements of both the MultiSets
        and returns it in a new MultiSet
        '''
        # creates a new MultiSet to return
        ms = MultiSet()
        # retrieves the bottom level of the SkipLists of both MultiSets
        self_current = self.sl.bottom_level()
        other_current = other.sl.bottom_level()
        # iterates and adds the value of other into the new MultiSet
        while not isinstance(other_current.next_node, TailNode):
            ms.insert(other_current.next_node.data)
            other_current = other_current.next_node
        # iterates and adds the value of self into the new MultiSet
        while not isinstance(self_current.next_node, TailNode):
            ms.insert(self_current.next_node.data)
            self_current = self_current.next_node
        return ms

    def __iadd__(self, other):
        '''(MultiSet, MultiSet) -> NoneType
        Takes in two MultiSets and updates self such that all the elements
        in other are also in self
        '''
        # finds the bottom level of the SkipList in other MultiSet
        other_current = other.sl.bottom_level()
        # iterates until it reaches the end of the set
        while not isinstance(other_current.next_node, TailNode):
            # adds every value thats in other, into self
            self.insert(other_current.next_node.data)
            # moves onto the next node
            other_current = other_current.next_node
        return self

    def __and__(self, other, self_current=None, ms=None):
        '''(MultiSet, MultiSet) -> MultiSet
        Takes in two MultiSets and returns a new MultiSet that contains the
        intersection of self and other
        '''
        # initialize the MultiSet
        if ms is None:
            ms = MultiSet()
        # get the bottom level of self
        if self_current is None:
            self_current = self.sl.bottom_level()
        # if the next node is not a tail node
        if not isinstance(self_current.next_node, TailNode):
            # finds the amount of times the value is in both MultiSets
            self_amount = self.count(self_current.next_node.data)
            other_amount = other.count(self_current.next_node.data)
            # checks if the value exists in both sets more than 0 and if the
            # the value has not already been inserted into MultiSet
            if self_amount > 0 and other_amount > 0 and \
               self_current.next_node.data not in ms:
                # finds the amount each Multiset has the values
                self_amount = self.count(self_current.next_node.data)
                other_amount = other.count(self_current.next_node.data)
                # if self has more of the values than other
                if self_amount >= other_amount:
                    # inserts the value the amount of times it exists by the
                    # amount other has the value
                    while other_amount > 0:
                        other_amount -= 1
                        ms.insert(self_current.next_node.data)
                    # recurses through the rest of the MultiSets
                    return self.__and__(other, self_current.next_node, ms)
                # if other has more of the values than self
                else:
                    # inserts the value the amount of times it exists by the
                    # amount self has the value
                    while self_amount > 0:
                        self_amount -= 1
                        ms.insert(self_current.next_node.data)
                    # recurses through the rest of the MultiSets
                    return self.__and__(other, self_current.next_node, ms)
            # if the value isnt in both MultiSets, continue recursing
            else:
                return self.__and__(other, self_current.next_node, ms)
        else:
            return ms

    def __iand__(self, other, self_current=None):
        '''(MultiSet, MultiSet) -> NoneType
        Takes in two MultiSets and updates self so that it only contains the
        intersection of self and other
        '''
        self = self & other
        return self

    def isdisjoint(self, other, self_current=None):
        '''(MultiSet, MultiSet) -> bool
        Takes in two MultiSets and returns true iff the MultiSets have no
        elements in common
        '''
        # retrieves the bottom of the SkipList in the self MultiSet
        if self_current is None:
            self_current = self.sl.bottom_level()
        # if the next node is not a tail node
        if not isinstance(self_current.next_node, TailNode):
            # if both of them have the same value, returns false
            if self_current.next_node.data in other:
                return False
            # else it continues recursing through the MultiSet
            else:
                return self.isdisjoint(other, self_current.next_node)
        # It has reached the end of the set, meaning none of the values
        # are shared between the sets, returning True
        return True
