'''Infix To Prefix Conversion Algorithm:
Step 1: Reverse the infix expression i.e A+B*C will become C*B+A. Note while reversing each ‘(‘ will become ‘)’ and each ‘)’ becomes ‘(‘.
Step 2: Obtain the postfix expression of the modified expression i.e CB*A+.
Step 3: Reverse the postfix expression. Hence in our example prefix is +A*BC.'''

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

    while St:#Popping out the remaining elements of the stack
        post += St.pop()
    return post

if __name__ == '__main__':
    exp = 'x^y/(5*z)+2'

    '''Next 6 are used to reversing the expression for evaluating Prefix Expression Of The Infix Expression'''
    m_exp=exp 
    exp=[i for i in exp][::-1]
    for i in range(len(exp)):
        if exp[i]=='(':exp[i]=')'
        elif exp[i]==')':exp[i]='('
    exp=''.join(exp)

    post=Infix_To_Prefix(exp)
    print("\nThe Resultant Prefix Expression Of Infix Expression {} Is : {}".format(m_exp, post[::-1]))
