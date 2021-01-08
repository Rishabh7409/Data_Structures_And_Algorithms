# This Program Is For Postfix To Infix Conversion Of An Expression

def Postfix_To_Infix(exp):
    S=[]
    for char in exp:
        if char.isalnum():
            S.insert(0,char)
        else:
            a=S.pop(0)
            b=S.pop(0)
            S.insert(0,f'({b} {char} {a})')
    print("The Resultant Infix Expression Of The Given Postfix Expression Is:",*S)

if __name__=='__main__':
    Postfix_To_Infix('abd^+ef-/g+')
    Postfix_To_Infix('abd+*e/f-ghk/+-')