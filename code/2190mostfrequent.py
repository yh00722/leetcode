

# class Solution:
#     def mostFrequent(self, nums, key) -> int:
        
#         nnumm = []
#         times = []
#         for i in range(len(nums)-1):
#             if(nums[i]==key):
#                 if(nums[i+1] not in nnumm):
#                     nnumm.append(nums[i+1])
#                     times.append(1)
#                 else:
#                     pos = nnumm.index(nums[i+1])
#                     times[pos] = times[pos]+1
#             else:
#                 continue
#         mmax = max(times)
#         ppos = times.index(mmax)
#         print(nnumm[ppos])


# slo= Solution()
# slo.mostFrequent([1,100,200,1,100],1)
            

# class Solution:
#     def mostFrequent(self, nums, key) -> int:
#         n = len(nums)
#         freq = Counter()   # 统计出现次数的哈希表
#         for i in range(n - 1):
#             if nums[i] == key:
#                 freq[nums[i+1]] += 1
#         return freq.most_common(1)[0][0]   # 计算并返回最高频元素

# slo= Solution()
# print(slo.mostFrequent([1,100,200,1,100],1))

class Solution:
    def mostFrequent(self, nums, key) -> int:
        dicct={}
        for i in range(len(nums)-1):
            if(nums[i])
