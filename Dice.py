import random
print "This game is for 2 players."
game = 0
user_points = 0
user2_points = 0
while game != 100:
    print "Rolling Dice..."
    num = random.randint(1, 6)
    if num % 2 == 0:
        user2_points = user2_points + 1
        print "Player 2 won!"
    else:
        user_points = user_points + 1
        print "Player 1 won!"
    game = game + 1
print "Player 1 points: ", user_points
print "Player 2 points: ", user2_points



