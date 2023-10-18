**INTUTION:
-----------------------------------
<br> binary addition </br>
 1+1=1,c=1
1+0=1 ,c=0
0+1=1,c=0
<h1>we can see that input in  string format to perform addition on this input the length of two numbers should be same .</h1>
<h1> so we first take each right most digit from two strings a,b and check above condition .<h1>
<h1> becoz of diff length of strings </h1>
<h1> we will use a while loop where condition length a or length b </h1>
<h1> individually we will check rightmost bit of each input is 1 or not </h1>
<h1> after checking both x and y we will update our ans and carry too</h1>
<h1> updation of ans=(x+y+c)%2 and c=(x+y+c)//2<h1>
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

