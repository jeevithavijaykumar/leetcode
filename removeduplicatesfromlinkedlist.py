#Remove Duplicates from Sorted List
#Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

class Removeduplicates():
    def removeduplicate(self,head):
        temp = head
        while(temp and temp.next):
            if(temp.val == temp.next.val):
                temp.next = temp.next.next
            else:
                temp=temp.next
        return(head)