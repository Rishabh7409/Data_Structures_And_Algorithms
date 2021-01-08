'''Infix To Postfix Conversion Algorithm:
1. Scan the infix expression from left to right.
2. If the scanned character is an operand, output it.
3. Else,
--  3.1 If the precedence of the scanned operator is greater than the precedence of the operator in the stack(or the stack is empty or the stack contains a ‘(‘ ), push it.
--  3.2 Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. After doing that Push the scanned operator to the stack. (If you encounter parenthesis while popping then stop there and push the scanned operator in the stack.)
4. If the scanned character is an ‘(‘, push it to the stack.
5. If the scanned character is an ‘)’, pop the stack and and output it until a ‘(‘ is encountered, and discard both the parenthesis.
6. Repeat steps 2-6 until infix expression is scanned.
7. Print the output
8. Pop and output from the stack until it is not empty.'''

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
    exp='a+(b*c-(d/e^f)*g)*h'
    exp='(a+b^d)/(e-f)+g'
    exp='a*(b+d)/e-f-(g+h/k)'
    exp='((a + b) / (c * d)) - e'
    # exp='(a+b^d)/(e-f)+g'
    # exp='(a+b)*(c-d)'
    # exp='a*b-c/d+e'
    # exp='h*(g*(f^e/d)-c*b)+a'
    post=Infix_To_Postfix(exp)
    print("\nThe Resultant Postfix Expression Of Infix Expression {} Is:{}".format(exp,post))