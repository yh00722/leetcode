
str = input()
dic = {}
class Solution:
 
    def longestPalindrome(self, s):
        if(s in dic):
            return dic[s]
        elif(len(s)==2 and s[0]==s[1]):
            dic[s]=s
            return dic[s]
        elif(len(s)==2 and s[0]!=s[1]):
            dic[s] = s[0]
            return dic[s]
        elif(len(s)==3 and s[0]==s[2]):
            dic[s]=s
            return dic[s]
        # elif(len(s)==3 and s[0]==s[1]):
        #     dic[s] = 0
        #     return dic[s]
        elif(len(s)==1):
            dic[s]=s
            return dic[s]
        else:
            for i in range(len(s)):
                for j in range(len(s)-1,i,-1):
                    if(s[i]==s[j]):
                        
                        if(len(s[i:j+1])==2):
                            dic[s[i:j+1]]= s[i]+s[j]
                            return dic[s[i:j+1]]
                        else:
                            
                        # print(result)
                            result = self.longestPalindrome(s[i+1:j])
                            if(result!=0 and len(result)==len(s)-2):
                                dic[s[i:j+1]] = s[i] + result + s[j]
                            
                                return dic[s[i:j+1]]
                            
    def printre(self,s):
        print(self.longestPalindrome(s))
        # print(dic[s])
                     
    
s = Solution()
s.printre(str)

    
                    

                


