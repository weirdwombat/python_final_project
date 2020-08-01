import matplotlib.pyplot as plt

switch_wins = []
user_input = random.randrange(1,4)
prize_door = random.randrange(1,4)

#need a for loop with a range
class InvalidDoorSelection(Exception):
    passs

def door_selection():
    if user_input not in [1,2,3]:
        raise  InvalidDoorSelection
    else:
        final()

#i want the program to be able to be able to reveal a remaining door that does not have the prize
#behind it

def final():
    if(user_pick != 1 and prize_door != 1):
        doors[0] = 'host revealed'
    elif(user_pick != 2 and prize_door != 2):
        doors[1] = 'host revealed'
    elif(user_pick != 3 and prize_door != 3):
        doors[1] = 'host revealed'

    def switch_or_stay():
        if user_input != prize_door:
            switch_wins += 1
    switch_or_stay()
    #gui()


#switch_wins_percentage = (switch_wins[0]/number of times I run the loop)

#plt.plot(decimal on x axis, ?? on y-axis)

#plt.xlabel("Wins by switching")
#plt.ylabel(not sure what y axis will be yet)

