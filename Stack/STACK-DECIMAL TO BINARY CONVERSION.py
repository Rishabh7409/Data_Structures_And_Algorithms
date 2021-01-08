
# Convert A Decimal Number To Binary Form
class stack:
    
    def __init__(self):
        self.S=[]

    def dec_to_bin(self,n):
        W=[]
        self.n=n
        while self.n>0:
            W.append(self.n%2)
            self.n=self.n//2
        print("Binary Form: ",end=' ')
        while W!=[]:
            print(W.pop(),end=' ')

S=stack()
n=int(input("Enter The Decimal No."))
S.dec_to_bin(n)
        
