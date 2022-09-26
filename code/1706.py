
import copy

def Min(lst):
    tmp = copy.copy(lst)
    for i in range(len(tmp)):
        if tmp[i]<0:
            tmp[i] = 9999
    return min(tmp)

def Max(lst):
    tmp = copy.copy(lst)
    for i in range(len(tmp)):
        if tmp[i]==9999:
            tmp[i]=-9999
    return max(tmp)


# class Solution:
def findBall(grid):
    initial = []
    for k in range(len(grid[0])):
        initial.append(k)    #下标对应球的起始位置 对应数值是现在所在位置 落不下去就是 -1
    # print(initial)
    for i in range(len(grid)):
        tmp = copy.copy(initial)
        start = Min(tmp) #每下降一行就要找新的遍历的起点位置 下标
        end = Max(tmp)
        # print(f"start:{start},end:{end}")
        for j in range(start,end+1):
            #球在两端
            if(j == 0 and grid[i][j]==-1):
                indexx = tmp.index(j)
                # print(indexx)
                initial[indexx] = -1 
                
            elif(j==len(grid[i])-1 and grid[i][j]==1):
                indexx = tmp.index(j)
                initial[indexx] = -1
            #球在中间
            elif(j not in tmp):
                continue
            else:
                #向右下滑动
                if(grid[i][j]==1 and grid[i][j+1]==1):
                    indexx = tmp.index(j)
                    # print(f"indexx:{indexx}")
                    initial[indexx] += 1
                    print("sdfada",tmp)
                elif(grid[i][j]==-1 and grid[i][j-1]==-1):
                    indexx = tmp.index(j)
                    initial[indexx] += -1
                else:
                    indexx = tmp.index(j)
                    # print(indexx)
                    initial[indexx] = -1
        # print(f"every time{initial}")
    return print(initial)







findBall(grid)


# lst = [-1,999,999,3,4,6]

# print(lst.index(Min(lst)))
# print(Min(lst))
# print(lst)


# print(lst.index(Max(lst)))
# print(Max(lst))
# print(lst)

#球从两端 球从中间