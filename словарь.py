import random

s = True

revolver_drum = [0, 0, 0, 0, 0, 1]

while s:
    shot = random.choice(revolver_drum)
    if shot == 1:
        s = False
        print('Убит!')
    else:
        print('Живой!')
