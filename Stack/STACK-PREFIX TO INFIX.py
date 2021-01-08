# Prefix To Infix Conversion Of A String

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
    print("The Resultant Infix Expression Of The Given Prefix Expression Is:",S[0])

if __name__=='__main__':
    Prefix_To_Infix('-/+ab*cde')
