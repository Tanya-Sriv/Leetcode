class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ptr = len(digits)-1
        carry = 0
        while ptr >=0:
            if len(digits) == 1 and digits[ptr] == 9:
                digits[ptr] = 0
                digits = [1]+digits
            if ptr == 0 and carry == 1 and digits[ptr] == 9:
                digits[ptr] = 0
                digits = [1]+digits
                ptr -=1
                continue
            if ptr == len(digits)-1:
                digits[ptr] = digits[ptr] + 1 
                carry = digits[ptr]//10
                digits[ptr] = digits[ptr]%10
            elif carry ==1:
                digits[ptr] = digits[ptr] + 1 
                carry = digits[ptr]//10
                digits[ptr] = digits[ptr]%10
            ptr -=1  
        return digits