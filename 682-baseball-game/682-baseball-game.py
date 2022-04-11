class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # Method 1:
        # l=[]
        # for i in ops:
        #     if i=='+':
        #         l.append(l[-1]+l[-2])
        #     elif i=='D':
        #         l.append(2*l[-1])
        #     elif i=='C':
        #         l.pop()
        #     else:
        #         l.append(int(i))
        # return sum(l)
        # Method 2:
        ops[0] = int(ops[0])
        if len(ops) == 1:
            return ops[0]
        elif len(ops) == 2:
            return ops[0]+int(ops[1])                   
        if ops[1] != "C" and ops[1] != 'D' and ops[1] != "+":
            ops[1] = int(ops[1])
        i = 1
        while i < len(ops):
            if ops[i] == 'C':
                ops.pop(i)
                ops.pop(i-1)
                i -= 2
            elif ops[i] == 'D':
                ops[i] = int(ops[i-1])*2
            elif ops[i] == '+':
                ops[i] = int(ops[i-1]) + int(ops[i-2])
            else:
                ops[i] = int(ops[i])
            i +=1
        return sum(ops)