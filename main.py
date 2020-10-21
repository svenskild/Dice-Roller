import numpy as np
import random
import os
import time


def dice(faces, dices=1):
    throw = np.zeros(dices)
    for i in range(dices):
        throw[i] = random.randint(1, faces)
    return throw


type_dice = {
    '1': {
        'd4': 4
    },
    '2': {
        'd6': 6
    },
    '3': {
        'd8': 8
    },
    '4': {
        'd10': 10
    },
    '5': {
        'd12': 12,
    },
    '6': {
        'd20': 20
    }
}

user_dice = []
dice_face = []

on = True
while on:
    os.system('cls||clear')
    print('-'*10, 'DICE ROLLER', '-'*10)

    print('\n\nTypes of dices: \n')
    for i in type_dice:
        for j in type_dice[i]:
            print(str(i) + ')', j)

    what_dice = input('What dices do you want? continue=q\n')
    if what_dice in type_dice:
        os.system('cls||clear')
        ammount = int(input('How many?\n'))
        for i in type_dice[what_dice]:
            arr = type_dice[what_dice]
            for j in range(ammount):
                user_dice.append(i)
                dice_face.append(arr[i])

    elif what_dice == 'q'.lower():
        display = True
        while display:
            os.system('cls||clear')
            print('Your dices:', user_dice)
            print('1) Roll')
            print('2) Restart')
            user = int(input('\n:'))
            if user == 2:
                user_dice = []
                break

            elif user == 1:
                roll = True
                while roll:
                    os.system('cls||clear')
                    print('1) Roll again')
                    print('2) Restart\n\n')

                    dice_rolled = []
                    for i in range(len(user_dice)):
                        tmp_rolled = dice(dice_face[i])
                        print(user_dice[i], 'rolled:', int(tmp_rolled))
                        dice_rolled.append(tmp_rolled)

                    print('\nSum =', int(sum(dice_rolled)))

                    user = input('\n:')
                    if user == '2':
                        roll = False
                        display = False
                        user_dice = []
                        break
                    elif user == '':
                        print('')

    elif what_dice == 'exit':
        on = False
        break

    else:
        os.system('cls||clear')
        print('Invalid input')
        time.sleep(1)
