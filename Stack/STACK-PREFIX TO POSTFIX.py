'''In Prefix To Postfix Conversion:
    1.Convert The Given Prefix Expression To Infix Expression.
    2.Now Convert The New Infix Expression To Postfix Expression'''

def Prefix_To_Infix(exp):
    S=[]
    for char in exp[::-1]:
        if char.isalnum():
            S.append(char)
        else:
            a=S.pop()
            b=S.pop()
            if S==[]:S.append(f'{a} {char} {b}')
            else:S.append(f'({a} {char} {b})')
    return S[0]


def Precedence(a,b):
    pre='LR'
    if a=='^' and b=='^':
        pre='RL' #Associativity of ^ symbol is from Right to Left

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3} #Precedence of operators
    if precedence[a]>=precedence[b] and pre!='RL': #If The Associativity is from right to left then nothing is to be done
        return True
    return False

def Infix_To_Postfix(exp):
    post=''
    St=[]
    for char in exp:
        if char.isalnum(): #Is char is operand
            post+=char
        elif char in '^+-*/':
            while St!=[] and St[-1]!='(' and Precedence(St[-1],char): #If Stack is not empty and top of stack is not (
                post+=St.pop()
            St.append(char)
        elif char=='(':
            St.append(char)
        elif char==')':
            while St!=[] and St[-1]!='(':
                post+=St.pop()
            St.pop()

    while St: #Popping out the remaining elements of the stack
        post+=St.pop()
    return post

if __name__=='__main__':
    exp=Prefix_To_Infix('-/+ab*cde') # Convert The Given Prefix Expression To Infix Expression.
    print("The Resultant Postfix Expression Of The Given Prefix Expression Is:",Infix_To_Postfix(exp)) # Now Convert The New Infix Expression To Postfix Expression