

class Node:
    def __init__(self,num,size,next):
        self.num = num
        self.size = size
        self.next = next


class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        head = Node(boxTypes[0][0],boxTypes[0][1],None) #第一
        ahead = Node(0,0,head)　#头节点
        for i in range(1,len(boxTypes)):
            tmp = Node(boxTypes[i][0],boxTypes[i][1],None)
            pos_a = ahead
            pos_b = head
            while tmp.size<=head.size:
                
                if pos_b != None:
                    pos_a = pos_a.next
                    pos_b = pos_b.next
                else:
                    break        
            tmp.next = pos_b
            pos_a.next = tmp
        
        loadbox = ahead.next
        allsize=0
        while truckSize >= loadbox.num:
            weights = loadbox.num*loadbox.size
            allsize += weights
            truckSize -= loadbox.num 
            loadbox = loadbox.next
        allsize += loadbox.size * truckSize
        return allsize
             



            






