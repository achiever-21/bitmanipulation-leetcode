class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        c=0
        k=""
        while i>=0 or j>=0 or c:
            x=0
            if i>=0 and a[i]=="1":
                x=1 
            y=0
            if j>=0 and b[j]=='1':
                y=1 
            k+=str((x+y+c)%2)
            c=(x+y+c)//2 
            i-=1
            j-=1
        return k[::-1]

