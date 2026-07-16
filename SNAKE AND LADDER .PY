import random
snakes = {
    98: 79,
    91: 73,
    84: 60,
    76: 55,
    69: 48,
    63: 42,
    52: 31,
    37: 18
}
ladders = {
    3: 22,
    8: 29,
    14: 35,
    21: 41,
    28: 50,
    44: 66,
    57: 77,
    71: 92
}
player1=input('enter a name :- ')
player2=input('enter a name :- ')

player_position1 = 0
player_position2 = 0 

player1_started = False
player2_started = False

players = [player1,player2]
start = [1,6]
while True:
    if not player1_started:
        dice = (random.randint(1,6))

        if dice == 6 or dice == 1:
            player1_started = True
            print(player1, "has entered the board!")
    if player1_started :

        print(f"\n{player1} 's turn")
        dice = (random.randint(1,6))
        print("rolled",dice)
        if player_position1 + dice <= 100:
            player_position1 += dice
        else:
            print("Need an exact roll to reach 100")    

        if player_position1 in snakes:
            print(" swallowed by snake ",snakes[player_position1])
            player_position1 = snakes[player_position1]
        if player_position1 in ladders:
            print(" you have climbed the ladder",ladders[player_position1])
            player_position1 = ladders[player_position1]
    else:
        print("1 or 6 required to join ")


   
    if not player2_started:
        dice = (random.randint(1,6))

        if dice == 6 or dice == 1:
                player2_started = True
                print(f"\n{player2} has entered the board")
    if player2_started:

            dice = random.randint(1,6)
            print("rolled",dice)
            if player_position2 + dice <= 100:
                player_position2 += dice
            else:
                print("Need an exact roll to reach 100")

            if player_position2 in snakes:
                print(" swallowed by snake ",snakes[player_position2])
                player_position2 = snakes[player_position2]
            if player_position2 in ladders:
                print(" you have climbed the ladder",ladders[player_position2])
                player_position2 = ladders[player_position2]
    else:
        print("1 or 6 required to join ")




    if player_position1 == 100:
        print(player1, "has won the game!")
        break

    if player_position2 == 100:
        print(player2, "has won the game!")
        break
    