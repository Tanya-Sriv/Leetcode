class Solution:
    def maxValue(self, n: str, x: int) -> str:
        flag = "-" in n
        x = str(x)
        if not flag:
            for i, s in enumerate(n):
                if s >= x:
                    continue
                else:
                    return n[:i]+ x + n[i:]
        else:
            for i,s in enumerate(n[1:]):
                if s <= x:
                    continue
                else:
                    return "-" + n[1:i+1]+ x + n[i+1:]
        return n + x
#         Method 1: Brute Force
#         flag = 0
#         x_s = str(x)
#         if int(n) < 0:
#             n = str(int(n[1:]))
#             flag = 1
#         for i in range(0,len(n)):
#             if flag == 0 and int(n[i]) < x:                
#                 if i > 0:
#                     # print("positive large index>0 ")
#                     return n[:i]+x_s+n[i:]
#                 elif i == 0:
#                     # print("positive large index=0 ")
#                     return x_s+n
#             elif flag == 1 and x < int(n[i]):
#                 if i > 0:
#                     # print("negative small index>0 ")
#                     return "-"+n[:i]+x_s+n[i:]
#                 elif i == 0:
#                     # print("negative small index=0 ")
#                     return "-"+x_s+n
#         return "-"+n+str(x) if flag == 1 else n+str(x)
            
            
        