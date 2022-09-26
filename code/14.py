
class Solution:
    def longestCommonPrefix(self, strs):
        tmp = ""
        first = list(strs[0])
        first.reverse()
        # print(first)
        for i in range(len(first)):
            word = first.pop()
            tmp += word
            # print(tmp)
            for j in range(len(strs)):
                if(not strs[j].startswith(tmp)):
                    # print(tmp)
                    tmp = tmp[:-1]

                    return tmp

# def find(strs):
#     tmp = []
#     for i in range(len(strs))

#字符串前缀，后缀匹配
filename = 'spam.txt'
a=filename.endswith('.tt')#后缀匹配
b=filename.startswith('s')#前缀匹配
print(a,b)

def finds(strs):
    tmp = ""
    first = list(strs[0])
    first.reverse()
    if(first==[]):
        return ""
    for i in range(len(first)):
        word = first.pop()
        print(word)
        tmp += word
        print("dsfa",tmp)
        for j in range(len(strs)):
            if(not strs[j].startswith(tmp)):
                print(tmp)
                tmp = tmp[:-1]
                if(tmp == None):
                    print("yunxing")
                    return ""
                
                print("yunxing")
                return tmp
            
strs = [""]
# tmp = list(strs[0])
# tmp.reverse()
# print(tmp)
print(finds(strs))


    
