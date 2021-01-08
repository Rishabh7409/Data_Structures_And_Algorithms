'''In Postfix Expression Evaluation The First Element Popped Will be The Second Operand and The Second Element Will Be The First Operand
The Postfix Expression Is Evaluated from left to right'''

def Evaluate_Postfix(exp,D):
    st=False
    S=[]
    for i in exp:
        if i in '+-*^/': #If i is operator
            try:
                a=S.pop() #Second Operand
                b=S.pop() #First Operand
                if i=='^':i='**'
                if a in D:
                    a=D[a] #If The a is operand then get its value from Dictionary
                if b in D:
                    b=D[b] #If The b is operand then get its value from Dictionary
                S.append(eval(f'{b}{i}{a}'))
            except:
                #If The Expression is not valid
                st=True
                break
        else:
            #If The i is operand
            S.append(i)

    if not st:return S[0]
    else:
        return  "Invalid Postfix Expression"

if __name__=='__main__':
    
    exp='ab+cd+*'
    D={'a':1,'b':1,'c':1,'d':1,'e':1,'g':1}  # values of the characters used in expression

    res=Evaluate_Postfix(exp,D)
    print("\nThe Result After Evaluation Of Given Expression Is:",res)