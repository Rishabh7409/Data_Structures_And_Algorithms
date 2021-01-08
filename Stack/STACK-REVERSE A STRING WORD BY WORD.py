class stack:
    st=''
    w=[]
    def __init__(self):
        self.S=[]

    def push(self,l):
        self.w=[]
        self.st=l
        print(self.st)
        for s in self.st:
            if s!=' ':
                self.w.append(s)
            else:
                self.S.append(''.join(self.w[::-1]))
                self.S.append(s)
                self.w=[]
    def showrev(self):
        print("Reverse Word By Word: ",''.join(self.S))

if __name__ == "__main__":
    S=stack()
    st=input("Enter The String To Be Reversed Word By Word: ")
    S.push(st+' ')  # extra space is to determine the last word of the string
    S.showrev()
