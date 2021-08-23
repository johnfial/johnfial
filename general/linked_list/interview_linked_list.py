

# coded by grant, me talking:

class LinkListNode:
    # track all created nodes and provide unique identifiers for each node
    id = 0

    def __init__(self, data=None):
        LinkListNode.id += 1
        self.id = LinkListNode.id
        self.next = None
        self.data = data

    def __repr__(self):
        n = "None"
        if self.next is not None:
            n = self.next.id
        return f"<id: {self.id}, next: {n}, data: {self.data}>"

class LinkedList:

    def __init__(self, seed=None):
        # seed is beginning of list
        if seed is not None:
            self.head = seed
        else:
            # empty ll
            self.head = None

    def __repr__(self):
        ll = []
        cur = self.head
        while cur:
            ll.append(str(cur))
            cur = cur.next
        #ll.append(str(self.tail))
        return " ~>> ".join(ll)

    @property
    def tail(self):
        cur = self.head
        while cur:
            if cur.next is None:
                return cur
            else:
                cur = cur.next

    def push(self, n):
        n.next = self.head
        self.head = n

    def link(self, n1, n2):
        if n1.id == n2.id:
            raise ValueError("cannot link node to itself")
        n1.next = n2

    def delete(self, n):
        cur = self.head
        if cur is not None:
            if cur.id == n.id:
                # head is being deleted
                self.head = cur.next
                return
        while cur is not None:
            if cur.id == n.id:
                break
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def unlink(self, n):
        # just like delete but different
        cur = self.head
        while cur.next:
            if cur.id == n.id:
                # head is being deleted
                self.head = cur.next
            elif cur.next.id == n.id:
                if n.id != self.tail.id:
                    # some middle node is being deleted
                    cur.next = n.next
                else:
                    # tail is being deleted
                    cur.next = None
                    break
            cur = cur.next

    def rev(self):
        cur = self.head
        prev = None
        while cur is not None:
            # store current next 
            suc = cur.next
            # update current link back to previous node or None
            cur.next = prev
            # shift forward
            prev = cur
            cur = suc
        self.head = prev

    def print_list(self):
        temp = self.head
        while temp:
            print(temp)
            temp = temp.next

# delete a node and re-link the list
def test_ll_remove():
    n1 = LinkListNode() # id: 1
    n2 = LinkListNode() # id: 2
    n3 = LinkListNode() # id: 3
    n4 = LinkListNode() # id: 4
    n5 = LinkListNode() # id: 5

    ll = LinkedList(n1) # 1 ~>>
    ll.link(n1, n2) # 1 ~>> 2
    ll.link(n2, n3) # 1 ~>> 2 ~>> 3
    ll.link(n3, n4) # 1 ~>> 2 ~>> 3 ~>> 4
    ll.link(n4, n5) # 1 ~>> 2 ~>> 3 ~>> 4 ~>> 5

    ll.unlink(n5) # 1 ~>> 2 ~>> 3 ~>> 4

    print(ll.tail.id == 4)
    print(ll.head.id == 1)

    ll.unlink(n1) # 2 ~>> 3 ~>> 4

    print(ll.tail.id == 4)
    print(ll.head.id == 2)

    ll.delete(n3) # 2 ~>> 4

    print(ll.tail.id == 4)
    print(ll.head.id == 2)
    
# reverse the link list
def test_ll_rev():
    n1 = LinkListNode()
    n2 = LinkListNode()
    n3 = LinkListNode()
    n4 = LinkListNode()

    ll = LinkedList() # ()
    ll.push(n4) # 1 ~>>
    ll.push(n3) # 1 ~>> 2
    ll.push(n2) # 1 ~>> 2 ~>> 3
    ll.push(n1) # 1 ~>> 2 ~>> 3 ~>> 4

    #print(f"initial list ->dd {ll}")
    ll.rev() # 4 ~>> 3 ~>> 2 ~>> 1
    #print(f"final list -> {ll}")
    print(ll.head.id == 4)
    print(ll.tail.id == 1)