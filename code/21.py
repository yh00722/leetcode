# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if len(list1)==0 or len(list2)==0:
            return list1+list2
        else:
            times = len(list1) if len(list1)<=len(list2) else:len(list2)
            head = ListNode()
            tmplist = []
            for i in range(times):
                
                tmp1 = ListNode()
                head.next = tmp1
                tmp2 = ListNode()
                tmp1.val = list1[i].val
                tmp1.next = tmp2
                tmp2.val = list2[i].val
                head = tmp2
                tmplist.append(tmp1)
                tmplist.append(tmp2)
            if(len(list1)<=len(list2)):
                head.next = list2[len(list1)]
                tmplist = tmplist+list2[len(list1):]
            else:
                head.next = list1[len(list2)]
                tmplist = tmplist+list1[len(list2):]
            
        return tmplist

def mergeTwoLists(list1,list2):
    if list1.next == None:
        return list2
    elif list2.next ==
    else:
        times = len(list1) if len(list1)<=len(list2) else:len(list2)
        head = ListNode()
        tmplist = []
        for i in range(times):
            
            tmp1 = ListNode()
            head.next = tmp1
            tmp2 = ListNode()
            tmp1.val = list1[i].val
            tmp1.next = tmp2
            tmp2.val = list2[i].val
            head = tmp2
            tmplist.append(tmp1)
            tmplist.append(tmp2)
        if(len(list1)<=len(list2)):
            head.next = list2[len(list1)]
            tmplist = tmplist+list2[len(list1):]
        else:
            head.next = list1[len(list2)]
            tmplist = tmplist+list1[len(list2):]
        
    return tmplist

class Solution:
    def mergeTwoLists(self,l1,l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val<=l2.val:
            l1.next =self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

            