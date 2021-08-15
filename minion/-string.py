def minion_game(string):
    player1=0
    player2=0
    len_str=len(s)
    for i in range(len_str):
        if s[i] in "AEIOU":
            player1+=(len_str)-i
            print('1',player1)
        else :
            player2+=(len_str)-i
            print('2',player2)
    if player1>player2:
        print("Kevin",player1)
    elif player1<player2:
        print("Stuart",player2)
    elif player1==player2:
        print("Draw")
    else:
        print("Draw")
s = input()
minion_game(s)
