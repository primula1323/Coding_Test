# 최종 구현
from ListNode import ListNode

class LinkedListBasic :
    def __init__(self) :
        self.__head = ListNode('dummy', None) # 노드의 시작은 더미 노드
        self.__numItems = 0 # 총 아이템 수 : 0개.

    def __getNode(self, idx : int) -> ListNode :
        '''
        Linked List의 index로부터 그 자리에 있는 value를 찾는 함수. 이 구현이 비효율적인 이유. 
        인덱스에 해당하는 노드를 찾아가기 위해 모든 노드를 방문해야 하고, 이 함수를 많은 작업에서 쓰니까.
        '''
        curr = self.__head #head에서 시작
        for i in range(0, idx+1) :
            curr = curr.next
        return curr

    def __findNode(self, x) -> ListNode :
        '''
        node의 value x로부터 그 x가 담긴 인덱스를 찾는 함수.
        '''
        prev = self.__head
        curr = prev.next
        while curr != None :
            if curr.item == x :
                return prev, curr
            else :
                prev = curr
                curr = curr.next
        return None, None

    def insert(self, idx : int, newItem) :
        if idx >= 0 and idx <= self.__numItems :
            prev = self.__getNode(idx-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
        else : print(f'index {idx} : out of bound')

    def append(self, newItem) :
        prev = self.__getNode(self.__numItems-1)
        newNode = ListNode(newItem, prev.next)
        prev.next = newNode
        self.__numItems += 1

    def pop(self, idx) :
        if idx >= 0 and idx <= self.__numItems-1 :
            prev = self.__getNode(idx - 1) 
            curr = prev.next
            prev.next = prev.next.next
            returnItem = curr.item
            self.__numItems -= 1
            return returnItem
        else :
            return None
        
    def remove(self, x) :
        prev, curr = self.__findNode(x)
        if curr != None :
            prev.next = curr.next
            self.__numItems -= 1

    def get(self, idx : int) :
        if self.isEmpty() :
            return None
        else :
            if idx >= 0 and idx <= self.__numItems-1 :
                return self.__getNode(idx).item
            else :
                return None
            
    def index(self, x) -> int :
        curr = self.__head.next
        for i in range(0, self.__numItems) :
            if curr.item == x :
                return i
            else :
                curr = curr.next
        return -987654321
    
    def isEmpty(self) :
        return self.__numItems == 0
    
    def size(self) :
        return self.__numItems
    
    def clear(self) :
        self.__head = ListNode('dummy', None)
        self.__numItems = 0

    def count(self, x) :
        cnt = 0
        curr = self.__head
        while curr != None :
            if curr.item == x :
                cnt += 1
                curr = curr.next
            else :
                curr = curr.next
        return cnt
    
    def extend(self, a) :
        for idx in range(0, a.size()) :
            self.append(a.get(idx)) 

    def copy(self) :
        a = LinkedListBasic() #LL 초기화. 이로 인해 a의 __numItems는 0, a.__head는 'dummy'로 맞춰짐.
        for i in range(0, self.__numItems) :
            a.append(self.get(i))
        return a
    
    def reverse(self) :
        a = LinkedListBasic()
        for i in range(0, self.__numItems) :
            a.insert(0, self.get(i)) 
        self.clear()
        for i in range(a.size()) :
            self.append(a.get(i))

    def sort(self) :
        a = []
        for i in range(0, self.__numItems) :
            a.append(self.get(i)) 
        a.sort()
        self.clear()
        for i in range(0, len(a)) :
            self.append(a[i])