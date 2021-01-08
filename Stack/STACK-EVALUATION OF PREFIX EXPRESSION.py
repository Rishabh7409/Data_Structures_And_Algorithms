'''In Postfix Expression Evaluation The First Element Popped Will be The Second Operand and The Second Element Will Be The First Operand
The Prefix Expression Is Evaluated From Right To Left'''

def Prefix_Evaluation(exp,D):
    
    st = False
    S=[]
    for i in exp:
        if i in '+-*^/':  # If i is operator
            try:
                a = S.pop()  # Second Operand
                b = S.pop()  # First Operand
                if i == '^': i = '**'
                if a in D: a = D[a]  # If The a is operand then get its value from Dictionary
                if b in D: b = D[b]  # If The b is operand then get its value from Dictionary
                S.append(eval(f'{a}{i}{b}'))
            except:
                # If The Expression is not valid
                st = True
                break
        else:
            # If The i is operand
            S.append(i)

    if not st:
        return S[0]
    else:
        return ("Invalid Prefix Expression")
if __name__=='__main__':
    # D={'a':20,'b':50,'c':3,'d':6,'e':300,'f':2}
    # exp='-/*a*b+cdef'

    # Every Expression will have its dictionary of values
    D={'a':9,'b':2,'c':6}
    exp='+a*bc'
    
    exp=exp[::-1]# #This Is Done Because The Prefix Expression Is Evaluated from right to left
    
    res=Prefix_Evaluation(exp,D)
    print("\nThe Result After Evaluation Of Given Prefix Expression Is:",res)