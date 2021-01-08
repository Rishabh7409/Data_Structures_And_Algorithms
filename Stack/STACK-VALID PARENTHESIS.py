class Parenthesis:
    def isValid(self,st):
        self.S=[]
        m=0
        for i in st:
            if i in '({[':
                self.S.append(i) # if it is open bracket then push it
            else:
                if self.S!=[]:
                    a=self.S.pop()
                    if a=='(' and i==')':
                        continue
                    elif a=='[' and i==']':
                        continue
                    elif a=='{' and i=='}':
                        continue
                    else:
                        # if any matching brackets are not found
                        m=1
                        break
                else:
                    # if stack is empty but closing bracket is found, therefore it is invalid
                    m=1
                    break

        if m==1 or self.S!=[]:
            # if stack is not empty it means that any extra bracket is remaining
            print('Invalid')
        else:
            print('Valid')

if __name__ == "__main__":
    
    S=Parenthesis()
    S.isValid('[()]{}{[()()]()}')
    # S.isValid('[(])')