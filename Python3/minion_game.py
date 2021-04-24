def minion_game(string):
    # your code goes here
    vowels = ['A','E','I','O','U']
    sc = 0
    kc = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kc += (len(string)-i)
        else:
            sc +=(len(string)-i)          
            
        
    if sc > kc:
        print("Stuart",sc)
    elif sc < kc :
        print("Kevin ",kc)
    else:
        print("Draw")

    
    