class Solution:
    def containsPattern(self, arr, m, k):
        for i in range(len(arr)-m+1):   
            model = arr[i:i+m]
            count = 0
            j = 0
            while(j<len(arr)-m+1):
                if(model == arr[j:j+m]):
                    # print(arr[j:j+m])

                    count += 1
                    j = j+m
                    if(count>=k):
                        return True
                    # print(j)
                else:
                    j = j+1
                    count = 0
        return False

# def containsPattern(arr,m,k):
#     for i in range(len(arr)-m+1):   
#         model = arr[i:i+m]
#         count = 0
#         j = 0
#         while(j<len(arr)-m+1):
#             if(model == arr[j:m]):

#                 count += 1
#                 j = j+m-1
#                 print(j)
#             else:
#                 j = j+1


#         # for j in range(len(arr)-m+1):
#         #     if(model == arr[j:j+m]):
#         #         count += 1
#         #         j=j+m
#         if(count>=k):
#             return True
#     return False

def containsPattern(arr,m,k):
    j = 0
    while(j<len(arr)-m+1):
        print(arr[j:j+m])
        j = j+m
        
        
          
    return False
        
arr = [1,2,4,4,4,4]
m = 2
k = 3

# [1,2,4,4,4,4] len = 6
# 1,3
# range(5) 0,1,2,3,4
# model = arr[0] arr[1] arr[2] arr[3] arr[4] 
# range(4) 0,1,2,3
# model arr[0:2] arr[1:3] arr[2:4] arr[3:5]


# 10 4 0,1,2,3,4,5.   0,1,2,3,4,5 5,6,7,8
print(containsPattern(arr,m,k))




# for i in range(10):
#     print(i)
#     i = i+2