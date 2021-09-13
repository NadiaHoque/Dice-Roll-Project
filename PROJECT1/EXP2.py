import numpy as np
import random
#we will use a dictionary for keeping the balls
basket = {}
#we will fill the basket with total of 60 balls as per the questions
for i in range(60):
    if i < 10:
        basket[i] = 'white'
    elif i > 9 and i < 30:
        basket[i] = 'red'
    else:
        basket[i] = 'green'
#initializing variables
n_simulation = 1000
part_a_total = 0
part_b_total = 0

for i in range(n_simulation):
#make an array of colors that we chose
    array_of_balls = []
    for i in range(5):
         array_of_balls.append(basket[random.randint(0, 59)])
#converting the array to a numpy array
    array_of_balls = np.array(array_of_balls)
#lets find the number of balls that we picked
    white = sum(array_of_balls == 'white')
    red = sum(array_of_balls == 'red')
    green = sum(array_of_balls == 'green')
#now lets keep track of the combinations for the question
    if white == 3 and red == 2:
        part_a_total += 1
    if red == 5 or white == 5 or green == 5:
        part_b_total += 1
print('The probability of 3 white and 2 red is: ',part_a_total/
n_simulation*100,'%')
print('The probability of all the same color is: ',part_b_total/
n_simulation*100,'%')