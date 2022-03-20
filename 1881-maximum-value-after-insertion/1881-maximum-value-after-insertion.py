class Solution:
    def maxValue(self, n: str, x: int) -> str:
        flag = 0
        x_s = str(x)
        if int(n) < 0:
            n = str(int(n[1:]))
            flag = 1
        for i in range(0,len(n)):
            if flag == 0 and int(n[i]) < x:                
                if i > 0:
                    # print("positive large index>0 ")
                    return n[:i]+x_s+n[i:]
                elif i == 0:
                    # print("positive large index=0 ")
                    return x_s+n
            elif flag == 1 and x < int(n[i]):
                if i > 0:
                    # print("negative small index>0 ")
                    return "-"+n[:i]+x_s+n[i:]
                elif i == 0:
                    # print("negative small index=0 ")
                    return "-"+x_s+n
        return "-"+n+str(x) if flag == 1 else n+str(x)
            
        