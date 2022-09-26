

class Solution:
    def findLength(self, nums1, nums2) -> int:
        if(len(nums1)<=len(nums2)):
            for i in range(len(nums1),0,-1):
                spos1 = 0
                epos1 = i-1
                while(epos1 != len(nums1)):
                    tmp1 = nums1[spos1:epos1+1]  #前闭后开
                    spos2 = 0
                    epos2 = i-1 
                
                    while(epos2 != len(nums2)):
                        tmp2 = nums2[spos2:epos2+1]
                        if(tmp1==tmp2):
                            return len(tmp1)
                        else:
                            spos2 += 1
                            epos2 += 1
                    spos1 += 1
                    epos1 += 1
            
        else:
            for i in range(len(nums2),0,-1):
                spos1 = 0
                epos1 = i-1
                while(epos1 != len(nums1)):
                    tmp1 = nums1[spos1:epos1+1]  #前闭后开
                    spos2 = 0
                    epos2 = i-1 
                
                    while(epos2 != len(nums2)):
                        tmp2 = nums2[spos2:epos2+1]
                        if(tmp1==tmp2):
                            return len(tmp1)
                        else:
                            spos2 += 1
                            epos2 += 1
                    spos1 += 1
                    epos1 += 1
        return 0
            


        
s = Solution()
print(s.findLength([70,39,25,40,7],[52,20,67,5,31]))

