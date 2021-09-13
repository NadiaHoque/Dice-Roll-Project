import numpy as np
import random
#function that runs the experiment 1000 times
def roll_the_dice(n_simulations = 1000):
    count = 0
#iteration for the the function
    for i in range(n_simulations):
#rolling the dice
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
#for getting the score
        score = die1 + die2
#deciding if we need to add it to the count
        if score % 2 == 0 or score > 7:
            count += 1
    return count/n_simulations
string = "The probability of rolling an even number or greater than 7 is:"
print(string ,np.round(roll_the_dice()*100,2),'%')