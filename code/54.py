# (4,3)

# 4(0,3) ,2(2,3),3(2,0),1(1,0),2(1,2)
# (5,4)
# 5,3,4,2,3,1,2,
# [r,d,l,u]

def travel(matrix):
    tmp = []
    order = []
    w = len(matrix[0])
    h = len(matrix)
    tmpw = w
    tmph = h-1
    print(w,h)
    flag = 0 #0横着 1竖着

    while(sum(order)!=w*h):
        # print(order)
        if flag==0:
            order.append(tmpw)
            tmpw = tmpw-1
            flag = 1
        else:
            order.append(tmph)
            tmph = tmph-1
            flag = 0
    
    direction = [1,2,3,0] #右，下，左，上
    verticalr = 0 #从横着开始遍历
    startw = -1
    starth = 0 #起点
    order.reverse()
    for i in range(len(order)): #i+1%4 选择方向
        step = order.pop()
        for j in range(step):
            if (i+1)%4 == 1:  #右
                startw = startw + 1 
                tmp.append(matrix[starth][startw])
            elif (i+1)%4 == 2: #下
                starth = starth + 1
                tmp.append(matrix[starth][startw])
            elif (i+1)%4 ==3 : #左面
                startw = startw - 1
                tmp.append(matrix[starth][startw])
            else:
                starth = starth - 1
                tmp.append(matrix[starth][startw])

    return tmp

class Solution:
    def spiralOrder(self, matrix):
        tmp = []
        order = []
        w = len(matrix[0])
        h = len(matrix)
        tmpw = w
        tmph = h-1
        print(w,h)
        flag = 0 #0横着 1竖着

        while(sum(order)!=w*h):
            # print(order)
            if flag==0:
                order.append(tmpw)
                tmpw = tmpw-1
                flag = 1
            else:
                order.append(tmph)
                tmph = tmph-1
                flag = 0
        
        direction = [1,2,3,0] #右，下，左，上
        verticalr = 0 #从横着开始遍历
        startw = -1
        starth = 0 #起点
        order.reverse()
        for i in range(len(order)): #i+1%4 选择方向
            step = order.pop()
            for j in range(step):
                if (i+1)%4 == 1:  #右
                    startw = startw + 1 
                    tmp.append(matrix[starth][startw])
                elif (i+1)%4 == 2: #下
                    starth = starth + 1
                    tmp.append(matrix[starth][startw])
                elif (i+1)%4 ==3 : #左面
                    startw = startw - 1
                    tmp.append(matrix[starth][startw])
                else:
                    starth = starth - 1
                    tmp.append(matrix[starth][startw])

        return tmp


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(travel(matrix))

# direction = [1,2,3,0]
# print(1%len(direction))
        


