class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        el = []
        word = ''
        d= {}
        for i in range(len(s)-1):
            if word != '':
                if s[i+1] == ')':
                    el.append(word)
                    word = ''
                    continue
                else:
                    word+=s[i+1]
            elif s[i] == '(' and word == '' :
                word+=s[i+1]
            else:
                continue                
        d = dict(knowledge)          
        for e in el:
            if e in d:
                s= s.replace(f"({e})", d[e])
            else:
                s= s.replace(f"({e})", '?')                
        return s
        