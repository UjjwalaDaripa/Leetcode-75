class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=list(word1)
        l2=list(word2)
        l3=[]
        s=''

        for i in range(0,len(l1)):
            l3.append(l1[i])
            for j in range(0,len(l2)):
                if i==j:
                    l3.append(l2[j])
                    break
            
        if len(l1)>=len(l2):
            s=s.join(l3)
        elif len(l1)<len(l2):
            s=s.join(l3)
            s=s+word2[len(l1):]
        return s
