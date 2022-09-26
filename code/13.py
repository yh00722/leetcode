class Solution:
    def romanToInt(self,s):
        num = 0
        flag = 0
        dic = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        dic2 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        tmp = list(s)
        chk = [0 for i in range(len(s))]
        for i in range(len(tmp)):
            if(i+1==len(s)):
                kw=None
            else:
                kw = tmp[i]+tmp[i+1]
                print(kw)
            if(chk[i]==0):
                if(kw in dic):
                    num = num+dic[kw]
                    chk[i]=1
                    chk[i+1]=1
            
                else:
                    num = num+dic2[tmp[i]]
                    chk[i]=1
            else:
                continue      
        return num




