class Solution:
    def nearestValidPoint(self, x, y, points):
        length = []
        pos = []
        for i in range(len(points)):
            if points[i][0] == x or points[i][1]==y:
                distance = abs(points[i][0]-x)+abs(points[i][1]-y)
                length.append(distance)
                pos.append(i)
        if len(length)==0:
            return -1
        else:
            position = length.index(min(length))
            posofmin = pos[position]
        
            
            return posofmin




def nearestValidPoint(x,y,points):
    length = []
    pos = []
    for i in range(points):
        if points[i][0] == x or points[i][1]==y:
            distance = abs(points[i][0]-x)+abs(points[i][1]-y)
            length.append(distance)
            pos.append(i)
    position = length.index(min(length))
    return pos[position]

# lis = [2,2,3,4,5]
# print(min(lis))
# print(lis.index(min(lis)))

        
