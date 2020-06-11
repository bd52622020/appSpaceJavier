import random

# Rock paper scissors

print('Welcome to the game Rock Paper and Scissors')
player = input('Write one that you want to be: rock, paper and scissors: \n')

machine = ['rock', 'paper', 'scissors']
machine = random.choices(machine, k=1)[0]

print('You choosed ' + player + ' and the machine randomly choosed ' + machine)

if (player == 'rock' and machine == 'scissors') or (player == 'paper' and machine == 'rock') or (player == 'scissors' and machine == 'paper'):
    print('You WIN!')
elif (machine == 'rock' and player == 'scissors') or (machine == 'rock' and player == 'scissors') or (machine == 'rock' and player == 'scissors'):
    print('You LOSE!')
else:
    print('Draw!')

