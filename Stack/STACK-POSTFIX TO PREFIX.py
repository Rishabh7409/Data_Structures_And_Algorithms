'''In Postfix To Prefix Conversion:
    1.Convert The Given Postfix Expression To Infix Expression.
    2.Now Convert The New Infix Expression To Prefix Expression'''


def Postfix_To_Infix(exp):
    S=[]
    for char in exp:
        if char.isalnum():
            S.insert(0,char)
        else:
            a=S.pop(0)
            b=S.pop(0)
            S.insert(0,f'({b} {char} {a})')
    return S[0]


def Precedence(a,b):
    pre='LR'
    if a=='^' and b=='^': #Associativity of ^ is from right to left
        pre='RL'
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3} #precedence of all operators
    if precedence[a]>=precedence[b] and pre!='RL': #If The Associativity is from right to left then nothing is to be done
        return True
    return False


def Infix_To_Prefix(exp):
    post = ''
    St = []
    for char in exp:
        if char.isalnum():#Is char is operand
            post += char
        elif char in '^+-*/':
            while St != [] and St[-1] != '(' and Precedence(St[-1], char): #If Stack is not empty and top of stack is not (
                post += St.pop()
            St.append(char)
        elif char == '(':
            St.append(char)
        elif char == ')':
            while St != [] and St[-1] != '(':
                post += St.pop()
            St.pop()

    while St:
        #Popping out the remaining elements of the stack
        post += St.pop()
    return post

if __name__=='__main__':
    exp=Postfix_To_Infix('abd^+ef-/g+')

    m_exp=exp
    
    # Reversing the expression
    exp=[i for i in exp][::-1]
    for i in range(len(exp)):
        if exp[i]=='(':exp[i]=')'
        elif exp[i]==')':exp[i]='('
    exp=''.join(exp)

    print("The Resultant Prefix Expression Of The Given Postfix Expression Is:",Infix_To_Prefix(exp)[::-1])