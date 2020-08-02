import random
import matplotlib.pyplot as plt

switch_wins = 0
stay_wins = 0

for x in range(5):
    #need a for loop with a range
    user_input = random.randrange(1,4)
    prize_door = random.randrange(1,4)

    doors = ['goat', 'goat', 'goat']

    doors[prize_door-1] = 'car'

    class InvalidDoorSelection(Exception):
        pass

    def door_selection(user_input):
        if user_input not in [1,2,3]:
            raise  InvalidDoorSelection
        else:
            return(switch_or_stay())

    #i want the program to be able to be able to reveal a remaining door that does not have the prize
    #behind it

    #not sure if i need this component
    #def final():
        #if(user_input != 1 and prize_door != 1):
            #doors[0] = host_revealed
        #elif(user_input != 2 and prize_door != 2):
            # doors[1] = host_revealed
        #elif(user_input != 3 and prize_door != 3):
            # doors[2] = 'host revealed'

    def switch_or_stay():
        if user_input != prize_door:
            switch_wins += 1
        elif user_input == prize_door:
            stay_wins += 1

    door_selection(user_input)

switch_wins_percentage = (switch_wins/5)
stay_wins_percentage = (stay_wins/5)
names = ['wins by keeping door', 'wins by changing door']
values = [stay_wins_percentage, switch_wins_percentage]

def gui_graph():
    plt.bar(names,values, color=['red','blue'])
    plt.title("Winning Decisions - Monty Hall Problem")
    plt.xlabel("Games Played : 5")
    plt.show()

gui_graph()





#switch_wins_percentage = (switch_wins[0]/number of times I run the loop)

#plt.plot( ?? on x-axis, decimal percentage on y axis)

#plt.ylabel("Wins percentage")
#plt.xlabel(not sure what x axis will be yet)


#if __name__ == '__main__':
    #print('user input is: ' + str(user_input))
    #try:
    #this time we used random number generator to mock user input
    #i turned the parts of this try except that would interfere with running the for loop
    #into comments
        #door_selection(user_input)
        #actual_user_input = int(input('please guess door 1, 2, or 3: '))
        #door_selection(actual_user_input)
    #this time we hard coded a 'bad' mocked user input
       # door_selection(15)
   # except InvalidDoorSelection:
        #print('The door selection was invalid!')

